from os import getenv

API_ID = 24620300
API_HASH = "9a098f01aa56c836f2e34aee4b7ef963"
BOT_TOKEN = "7810188596:AAF-7JouiEvT9atoQA7NPooqqkDb0UfbT3I"
BOT_COMMANDS = (
    ("start", "Initialize the bot and check its status"),
    ("settings", "Configure and manage bot settings"),
    ("help", "Get information on how to use the bot"),
    ("about", "Learn more about the bot and its features"),
)

DATABASE_URL = "mongodb+srv://tusar:tusar1@cluster0.guw5d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "0"))
