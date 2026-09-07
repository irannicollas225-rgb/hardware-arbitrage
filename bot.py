import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def receber_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message.text
    print(f"Mensagem recebida: {mensagem}")

    await update.message.reply_text("✅ Recebi sua mensagem!")


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, receber_mensagem)
)

print("🤖 Bot iniciado. Aguardando mensagens...")

app.run_polling()