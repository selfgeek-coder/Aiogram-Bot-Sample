from typing import Optional
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

            cursor.execute("DELETE FROM users WHERE chat_id = ?", (chat_id,))

            conn.commit()

    