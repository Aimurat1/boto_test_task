import logging
from typing import Tuple, Dict, Any
from credentials import telegram_bot_token

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
    CallbackContext,
)
from detector import is_meaningful

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Top level conversation callbacks
def start(update: Update, context: CallbackContext) -> str:
    chat_id = update.message.chat_id
    
    context.bot.send_message(chat_id, text = "Введите ваш текст, я определю имеют ли смысл фидбэк или нет")

    return "ANSWER"

def identify(update: Update, context: CallbackContext) -> str:
    chat_id = update.message.chat_id
    
    text = update.message.text
    
    try:
        answer = is_meaningful(text)
        if answer is True: answer = "✅ Да, имеет смысл" 
        elif answer is False: answer = "❌ Нет, не имеет"
    except:
        answer = "Ой-ой-ой, возникла проблема на стороне OpenAI"
        
    context.bot.send_message(chat_id, text = answer)

    



def main() -> None:
    updater = Updater(telegram_bot_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

 
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            "ANSWER": [      
                MessageHandler(Filters.text, identify)
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()