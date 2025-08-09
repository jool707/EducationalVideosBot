from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

main_buttons = [
    [InlineKeyboardButton("البرمجة", callback_data='programming')],
    [InlineKeyboardButton("من نحن", callback_data='about')]
]

programming_sub_buttons = [
    [InlineKeyboardButton("أساسيات البرمجة", callback_data='basics')],
    [InlineKeyboardButton("HTML", callback_data='html')],
    [InlineKeyboardButton("CSS", callback_data='css')],
    [InlineKeyboardButton("JavaScript", callback_data='javascript')],
    [InlineKeyboardButton("بايثون", callback_data='python')],
    [InlineKeyboardButton("سي شارب", callback_data='csharp')],
    [InlineKeyboardButton("رجوع", callback_data='back_main')]
]

def start(update: Update, context: CallbackContext):
    keyboard = InlineKeyboardMarkup(main_buttons)
    update.message.reply_text("اختر القسم:", reply_markup=keyboard)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = query.data

    if data == 'programming':
        keyboard = InlineKeyboardMarkup(programming_sub_buttons)
        query.edit_message_text(text="اختر قسم البرمجة:", reply_markup=keyboard)

    elif data == 'about':
        query.edit_message_text(text="هذا بوت لتقديم الفيديوهات التعليمية. تواصل معنا لأي استفسار.")

    elif data == 'back_main':
        keyboard = InlineKeyboardMarkup(main_buttons)
        query.edit_message_text(text="اختر القسم:", reply_markup=keyboard)

    else:
        videos_links = {
            'basics': "رابط فيديوهات أساسيات البرمجة: https://example.com/basics",
            'html': "رابط فيديوهات HTML: https://example.com/html",
            'css': "رابط فيديوهات CSS: https://example.com/css",
            'javascript': "رابط فيديوهات JavaScript: https://example.com/javascript",
            'python': "رابط فيديوهات بايثون: https://example.com/python",
            'csharp': "رابط فيديوهات سي شارب: https://example.com/csharp"
        }

        response = videos_links.get(data, "القسم غير معروف.")
        query.edit_message_text(text=response)

def main():
    updater = Updater("7375638976:AAE1ZVC4wTjZ4Hry4WdyiMy1OoXtgubOxYY", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
