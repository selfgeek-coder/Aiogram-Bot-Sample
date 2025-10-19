from typing import Optional, Dict, List
from .database import get_connection

class DatabaseRepository:
    @staticmethod
    async def add_user(chat_id: int, username: Optional[str] = None,
                       first_name: Optional[str] = None,
                       last_name: Optional[str] = None) -> bool:
        """Функция добавления пользователя в базу данных"""
        
        async with get_connection() as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("""
                INSERT OR IGNORE INTO users (chat_id, username, first_name, last_name) 
                VALUES (?, ?, ?, ?)
                """, (chat_id, username, first_name, last_name))

                conn.commit()

                return True
            except Exception as e:
                print(f"Ошибка при добавлении пользователя: {e}")
                return False

    @staticmethod
    async def check_user(chat_id: int) -> bool:
        """Функция проверки, есть ли пользователь в базе данных"""
        
        async with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM users WHERE chat_id = ?", (chat_id,))
            
            return cursor.fetchone() is not None
        
    @staticmethod
    async def delete_user(chat_id: int) -> bool:
        """Функция удаления пользователя из БД по chat_id: int"""

        async with get_connection() as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("DELETE FROM users WHERE chat_id = ?", (chat_id,))
                conn.commit()
                return True
            
            except Exception as e:
                print(f"Ошибка при удалении пользователя: {e}")
                return False

    @staticmethod
    async def get_users() -> Dict[str, List[Dict[str, Optional[str]]]]: 
        """Функция для получения всех пользователей с БД"""

        async with get_connection() as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("""
                    SELECT chat_id, username, first_name, last_name 
                    FROM users 
                    ORDER BY chat_id
                """)

                users_data = cursor.fetchall()

                users_list = []

                for user in users_data:
                    users_list.append(
                        {
                            "chat_id": user[0],
                            "username": user[1],
                            "first_name": user[2],
                            "last_name": user[3]
                        }
                    )

                return {
                    "users": users_list
                }

            except Exception as e:
                print(f"Ошибка при получении пользователей: {e}")
                return {"users": []}