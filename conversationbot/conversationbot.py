from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

GENDER = 1
PHOTO = 2
LOCATION = 3
BIO = 4


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(update.message.from_user)
    reply_keyboard = [["O'g'il", "Qiz", "Boshqa"]]

    await update.message.reply_text(
        "Salom! Mening ismim professor Bot. Men siz bilan suhbat quraman.\n"
        "Men bilan gaplashishni to'xtatish uchun yuboring /cancel yuboring.\n\n"
        "Siz o'g'ilmisiz yoki qizmi?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="O'g'ilmisiz yoki Qizmi",
        ),
    )

    return GENDER


async def gender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(update.message.text)
    await update.message.reply_text(
        "Iltimos, menga o'zingizning suratingizni yuboring,"
        "yoki xohlamasangiz, yuboring /skip yuboring",
        reply_markup=ReplyKeyboardRemove(),
    )

    return PHOTO


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    photo_file = await update.message.photo[-1].get_file()
    print(photo_file)
    await photo_file.download_to_drive("user_photo.jpg")
    await update.message.reply_text(
        "Ajoyib! Endi, iltimos, menga joylashuvingizni yuboring yoki xohlamasangiz, /skip yuboring."
    )

    return LOCATION


async def skip_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Endi, iltimos, menga joylashuvingizni yuboring yoki /skip yuboring."
    )

    return LOCATION


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(update.message.location)
    await update.message.reply_text("O'zingiz haqingizda biror narsa ayting.")

    return BIO


async def skip_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Nihoyat, o'zingiz haqingizda biror narsa ayting.")

    return BIO


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(update.message.text)
    await update.message.reply_text("Rahmat! Umid qilamanki, bir kun yana gaplashamiz.")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Xayr! Umid qilamanki, bir kun yana gaplashamiz.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END


def main() -> None:
    application = (
        Application.builder()
        .token("")
        .build()
    )

    # ConversationHandler class'ini yaratish (Suhbat boshqaruvchisi)
    conv_handler = ConversationHandler(
        # Suhbatga kirish nuqtasini o'rnatish
        entry_points=[CommandHandler("start", start)],
        # Suhbat holatlari
        states={
            GENDER: [MessageHandler(filters.Regex("^(O'g'il|Qiz|Boshqa)$"), gender)],
            PHOTO: [
                MessageHandler(filters.PHOTO, photo),
                CommandHandler("skip", skip_photo),
            ],
            LOCATION: [
                MessageHandler(filters.LOCATION, location),
                CommandHandler("skip", skip_location),
            ],
            BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
        },
        # Zapasnoy mehanizm
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
