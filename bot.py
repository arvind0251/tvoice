import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Heroku environment variable se token lein

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Send me a voice message and I will clone it!')

async def handle_voice(update: Update, context: CallbackContext) -> None:
    voice_file = await update.message.voice.get_file()
    await voice_file.download('user_voice.ogg')  # Voice file ko download karein

    # Yahan aapki voice cloning logic aayegi
    # cloned_voice_path = clone_voice('user_voice.ogg')

    # Cloned voice ko bhejein
    # with open(cloned_voice_path, 'rb') as audio:
    #     await update.message.reply_voice(audio)

async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))

    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
