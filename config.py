from dotenv import load_dotenv
import os

load_dotenv()

crypto_token = os.getenv("CRYPTO_PAY_TOKEN")
bot_token = os.getenv("BOT_TOKEN")
owner_id = int(os.getenv("OWNER_ID"))

default_asset = os.getenv("DEFAULT_ASSET")
invoice_expires = os.getenv("INVOICE_EXPIRES")