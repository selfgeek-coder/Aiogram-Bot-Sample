from aiocryptopay import AioCryptoPay, Networks

from config import crypto_token, default_asset, invoice_expires

crypto = AioCryptoPay(token=crypto_token, network=Networks.MAIN_NET)

class PayRepository:
    @staticmethod
    async def create_invoice(amount: float,
                             asset: str = default_asset) -> dict:
        """Создает платеж amount в токене 'default_asset' по умолчению"""

        async with crypto:
            invoice = await crypto.create_invoice(asset=asset, amount=amount, expires_in=invoice_expires)

            return {
                "url": str(invoice.bot_invoice_url),
                "invoice_id": invoice.invoice_id
            }
        
    @staticmethod
    async def check_invoice(invoice_id: int) -> dict:
        """
        Проверяет инвойс по его invoice_id (возвращается в create_invoice)

        Returns:
            dict: {
                "status": "paid" | "active" | "expired",
                "paid": bool
            }
        """
        
        async with crypto:
            try:
                invoice = await crypto.get_invoices(invoice_ids=invoice_id)
                
                status_map = {
                    'active': 'active',
                    'paid': 'paid',
                    'expired': 'expired'
                }
                
                return {
                    "status": status_map.get(invoice.status, 'active'),
                    "paid": invoice.status == 'paid'
                }
            
            except Exception as e:
                return {
                    "status": "expired",
                    "paid": False,
                    "amount": 0
                }
        
    @staticmethod
    async def delete_invoice(invoice_id: int) -> dict:
        """
            Удаляет инвойс по его invoice_id

            Returns:
                dict: {
                    "success": bool
                }
        """
            
        async with crypto:
            try:
                result = await crypto.delete_invoice(invoice_id=invoice_id)
                    
                return {
                    "success": True
                    }
                
            except Exception as e:
                return {
                    "success": False
                }