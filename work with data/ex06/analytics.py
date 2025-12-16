import os
import logging
from random import randint
import requests
import json
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='analytics.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        logging.info(f"Research class initialized with file: {file_path}")
    
    def file_reader(self, has_header=True):
        logging.info("Reading file data")
        if not os.path.exists(self.file_path):
            error_msg = "File not found"
            logging.error(error_msg)
            raise Exception(error_msg)
        
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        
        data = []
        start_index = 1 if has_header else 0
        
        for i, line in enumerate(lines[start_index:], start_index + 1):
            values = line.strip().split(',')
            if len(values) != 2:
                raise Exception(f"Line {i} must contain exactly two values")
            try:
                data.append([int(values[0]), int(values[1])])
            except ValueError:
                raise Exception(f"Line {i} contains non-integer values")
        
        logging.info(f"Successfully read {len(data)} data points")
        return data
    
    def send_telegram_message(self, success):
        import config
        message = "The report has been successfully created" if success else "The report hasn't been created due to an error"
        
        try:
            # Check if Telegram is configured
            if not hasattr(config, 'TELEGRAM_WEBHOOK_URL') or "your_bot_token" in config.TELEGRAM_WEBHOOK_URL:
                logging.warning("Telegram not configured properly, skipping notification")
                return
            
            payload = {
                'chat_id': config.TELEGRAM_CHAT_ID,
                'text': message
            }
            response = requests.post(config.TELEGRAM_WEBHOOK_URL, data=payload, timeout=10)
            logging.info(f"Telegram message sent: {message}, Response: {response.status_code}")
        except Exception as e:
            logging.error(f"Failed to send Telegram message: {e}")

class Calculations:
    def __init__(self, data):
        self.data = data
        logging.info("Calculations class initialized with data")
    
    def counts(self):
        logging.info("Calculating counts of heads and tails")
        heads = sum(1 for row in self.data if row == [0, 1])
        tails = sum(1 for row in self.data if row == [1, 0])
        logging.info(f"Counts calculated: Heads={heads}, Tails={tails}")
        return heads, tails
    
    def fractions(self, heads, tails):
        logging.info("Calculating fractions/percentages")
        total = heads + tails
        if total == 0:
            logging.warning("No data available for fraction calculation")
            return 0, 0
        result = (heads / total) * 100, (tails / total) * 100
        logging.info(f"Fractions calculated: Heads={result[0]:.2f}%, Tails={result[1]:.2f}%")
        return result

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)
        logging.info("Analytics class initialized")
    
    def predict_random(self, num_predictions):
        logging.info(f"Generating {num_predictions} random predictions")
        predictions = []
        for _ in range(num_predictions):
            if randint(0, 1) == 0:
                predictions.append([0, 1])  # heads
            else:
                predictions.append([1, 0])  # tails
        logging.info(f"Generated predictions: {predictions}")
        return predictions
    
    def predict_last(self):
        logging.info("Retrieving last prediction from data")
        result = self.data[-1] if self.data else None
        logging.info(f"Last prediction: {result}")
        return result
    
    def save_file(self, data, filename, extension):
        logging.info(f"Saving file: {filename}.{extension}")
        full_filename = f"{filename}.{extension}"
        try:
            with open(full_filename, 'w') as file:
                file.write(str(data))
            logging.info(f"File saved successfully: {full_filename}")
            return full_filename
        except Exception as e:
            logging.error(f"Failed to save file: {e}")
            raise