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

class AvatarPredictorBot:
    """Telegram bot for avatar prediction and joke generation"""
    
    def __init__(self, token: str):
        self.token = token
        self.app = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Register command handlers"""
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("joke", self.joke_command))
        self.app.add_handler(CommandHandler("programmer_joke", self.programmer_joke_command))
        self.app.add_handler(CommandHandler("knock_knock", self.knock_knock_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    
    async def joke_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /joke command - random joke"""
        await update.message.reply_text("🤣 Fetching a joke for you...")
        
        result = JokeGenerator.get_random_joke()
        
        if result['success']:
            await update.message.reply_text(result['joke'])
        else:
            await update.message.reply_text(result['error'])
    
    async def programmer_joke_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /programmer_joke command"""
        await update.message.reply_text("💻 Fetching a programmer joke...")
        
        result = JokeGenerator.get_programmer_joke()
        
        if result['success']:
            await update.message.reply_text(result['joke'])
        else:
            await update.message.reply_text(result['error'])
    
    async def knock_knock_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /knock_knock command"""
        await update.message.reply_text("🚪 Here's a knock-knock joke!")
        
        result = JokeGenerator.get_knock_knock_joke()
        
        if result['success']:
            await update.message.reply_text(result['joke'])
        else:
            await update.message.reply_text(result['error'])
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    
    def run(self):
        """Start the bot"""
        logger.info("Starting Avatar Predictor Bot...")
        self.app.run_polling()

if __name__ == "__main__":
    bot = AvatarPredictorBot(BOT_TOKEN)
    bot.run()
