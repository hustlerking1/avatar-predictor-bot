import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from joke_generator import JokeGenerator

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables. Please set it in .env file")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    welcome_message = (
        f"👋 Welcome {user.first_name}!\n\n"
        "I'm your Avatar Predictor Bot! 🎨\n\n"
        "Here's what I can do:\n"
        "• Predict your perfect avatar based on your personality\n"
        "• Tell you random jokes to brighten your day\n\n"
        "Use /help to see all available commands!"
    )
    await update.message.reply_text(welcome_message)

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /joke command - random joke"""
    await update.message.reply_text("🤣 Fetching a joke for you...")
    
    result = JokeGenerator.get_random_joke()
    
    if result['success']:
        await update.message.reply_text(result['joke'])
    else:
        await update.message.reply_text(result['error'])

async def programmer_joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /programmer_joke command"""
    await update.message.reply_text("💻 Fetching a programmer joke...")
    
    result = JokeGenerator.get_programmer_joke()
    
    if result['success']:
        await update.message.reply_text(result['joke'])
    else:
        await update.message.reply_text(result['error'])

async def knock_knock_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /knock_knock command"""
    await update.message.reply_text("🚪 Here's a knock-knock joke!")
    
    result = JokeGenerator.get_knock_knock_joke()
    
    if result['success']:
        await update.message.reply_text(result['joke'])
    else:
        await update.message.reply_text(result['error'])

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_message = (
        "📋 Available Commands:\n\n"
        "/start - Start the bot and see welcome message\n"
        "/joke - Get a random joke\n"
        "/programmer_joke - Get a programmer-specific joke\n"
        "/knock_knock - Get a knock-knock joke\n"
        "/help - Show this help message\n\n"
        "More features coming soon! 🚀"
    )
    await update.message.reply_text(help_message)

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("joke", joke_command))
    app.add_handler(CommandHandler("programmer_joke", programmer_joke_command))
    app.add_handler(CommandHandler("knock_knock", knock_knock_command))
    app.add_handler(CommandHandler("help", help_command))
    
    logger.info("Starting Avatar Predictor Bot...")
    app.run_polling()

if __name__ == "__main__":
    main()
