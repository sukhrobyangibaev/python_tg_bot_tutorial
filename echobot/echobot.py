from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters


async def start(update, _):
    # update parametri kiruvchi yangilanishni ifodalaydi
    await update.message.reply_text("Hello!")


async def echo(update, _):
    await update.message.reply_text(update.message.text)


def main():
    # Application class'ining namunasini yaratish
    application = (
        Application.builder()
        .token("")
        .build()
    )

    # "/start" buyrug'i uchun bajaruvchi funksiyani qo'shish
    application.add_handler(CommandHandler("start", start))

    # matnli xabarlarni qayta ishlash uchun funksiyani qo'shish
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # botni 'long polling' usuli yordamida ishga tushirish
    application.run_polling()


# print('__name__ =', __name__)
if __name__ == "__main__":
    main()
