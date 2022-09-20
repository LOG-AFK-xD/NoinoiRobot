import html
import random
import NoinoiRobot.modules.truth_and_dare_string as truth_and_dare_string
from NoinoiRobot import dispatcher
from telegram import ParseMode, Update, Bot
from NoinoiRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

@run_async
def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

    
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)


dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__mod_name__ = "ᴛ & ᴅ"

__help__ = """
Plugins From Azuka Bot 📚

/truth - `for play game truth and dare.`
/dare - `for play game truth and dare.`

"""
