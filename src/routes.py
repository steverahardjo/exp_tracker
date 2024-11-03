from enum import Enum
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hello! Welcome to your new bot!')
    
async def handle_user_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text

    
def main() -> None:
    """Start the bot."""
    # Create the Application (formerly called Updater)
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    
    app.run_polling()

if __name__ == '__main__':
    main()