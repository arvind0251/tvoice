import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters  # Updated import for filters

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Heroku environment variable se token lein

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a voice message and I will clone it!')

def handle_voice(update: Update, context: CallbackContext) -> None:
    voice_file = update.message.voice.get_file()
    voice_file.download('user_voice.ogg')  # Voice file ko download karein

    # Yahan aapki voice cloning logic aayegi
    # cloned_voice_path = clone_voice('user_voice.ogg')

    # Cloned voice ko bhejein
    # with open(cloned_voice_path, 'rb') as audio:
    #     update.message.reply_voice(audio)

def main() -> None:
    updater = Updater(TOKEN)

    # Command handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(filters.VOICE, handle_voice))  # Updated to use filters

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
