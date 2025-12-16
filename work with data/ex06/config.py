import os 
from dotenv import load_dotenv
load_dotenv() 

# config.py - Create the expected attributes

# Analytics parameters
num_of_steps = 12
forecast_steps = 3

# Report template
report_template = """We made {observations} observations by tossing a coin: {tails} were tails and {heads} were heads. The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively. Our forecast is that the next {forecast_steps} observations will be: {forecast_tails} tail(s) and {forecast_heads} head(s)."""

# Telegram configuration - CREATE THE EXPECTED ATTRIBUTES
telegram_bot_token = os.getenv("TELE")    
telegram_chat_id = os.getenv("tele")      

# Configuration parameters
NUM_OF_STEPS = 3
REPORT_TEMPLATE = """We made {total_observations} observations by tossing a coin: {tails_count} were tails and {heads_count} were heads. The probabilities are {tail_percentage:.2f}% and {head_percentage:.2f}%, respectively. Our forecast is that the next {num_predictions} observations will be: {prediction_summary}."""

# Telegram configuration
TELEGRAM_WEBHOOK_URL =f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
TELEGRAM_ID = telegram_chat_id