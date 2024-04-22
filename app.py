from flask import Flask, request
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

# Replace 'YOUR_BOT_TOKEN' with the token provided by the BotFather
TOKEN = '7049373526:AAFn3M07oWdImldj7iZAus7hhVZefW6NPYo'

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Telegram bot running in a Flask application.")

def echo(update, context):
    """Echo the user message."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def setup_bot():
    """Set up the Telegram bot handlers."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers for the /start command and for echoing messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    return updater

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming Telegram updates."""
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    setup_bot().dispatcher.process_update(update)
    return 'OK'