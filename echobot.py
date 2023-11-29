from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters


async def start(update, _):
    await update.message.reply_text('Hello!')


async def echo(update, _):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token("5581179119:AAFd8Da6TQdmTwtGqdn-3QQp2vcsSDnDEms").build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
