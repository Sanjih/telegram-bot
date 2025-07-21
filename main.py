import os, asyncio
from flask import Flask, request, abort
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8092994458:AAHI1Ud1fh2E06VaXy6826Db0KH4KAstn6E"         # ← ton TOKEN exact
WEBHOOK_URL = "https://web-production-760a2.up.railway.app/webhook"  # ← ton URL Railway

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salama! VintsyBot no nandray anao.")

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.route("/webhook", methods=["POST"])
def webhook():
    json_data = request.get_json(force=True)
    update = Update.de_json(json_data, application.bot)
    asyncio.run(application.process_update(update))
    return "ok", 200

if __name__ == "__main__":
    asyncio.run(application.initialize())
    asyncio.run(application.bot.set_webhook(WEBHOOK_URL))
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
