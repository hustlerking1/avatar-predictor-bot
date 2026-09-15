import requests
import logging

logger = logging.getLogger(__name__)

class JokeGenerator:
    """Generate random jokes using external APIs"""
    
    # API endpoints for different joke types
    JOKE_API = "https://official-joke-api.appspot.com/random_joke"
    PROGRAMMER_JOKE_API = "https://official-joke-api.appspot.com/jokes/programming/random"
    KNOCK_KNOCK_API = "https://official-joke-api.appspot.com/jokes/knock-knock/random"
    
    @staticmethod
    def get_random_joke():
        """Fetch a random joke from the API"""
        try:
            response = requests.get(JokeGenerator.JOKE_API, timeout=5)
            response.raise_for_status()
            joke_data = response.json()
            
            setup = joke_data.get('setup', '')
            punchline = joke_data.get('punchline', '')
            joke_type = joke_data.get('type', 'general')
            
            return {
                'success': True,
                'joke': f"{setup}\n\n{punchline}",
                'type': joke_type
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching random joke: {e}")
            return {
                'success': False,
                'error': "Could not fetch joke at the moment. Try again later!"
            }
    
    @staticmethod
    def get_programmer_joke():
        """Fetch a programmer-specific joke"""
        try:
            response = requests.get(JokeGenerator.PROGRAMMER_JOKE_API, timeout=5)
            response.raise_for_status()
            joke_data = response.json()
            
            setup = joke_data.get('setup', '')
            punchline = joke_data.get('punchline', '')
            
            return {
                'success': True,
                'joke': f"👨‍💻 {setup}\n\n{punchline}",
                'type': 'programming'
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching programmer joke: {e}")
            return {
                'success': False,
                'error': "Could not fetch programmer joke at the moment. Try again later!"
            }
    
    @staticmethod
    def get_knock_knock_joke():
        """Fetch a knock-knock joke"""
        try:
            response = requests.get(JokeGenerator.KNOCK_KNOCK_API, timeout=5)
            response.raise_for_status()
            joke_data = response.json()
            
            setup = joke_data.get('setup', '')
            punchline = joke_data.get('punchline', '')
            
            return {
                'success': True,
                'joke': f"🚪 Knock knock!\n{setup}\n{punchline}",
                'type': 'knock-knock'
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching knock-knock joke: {e}")
            return {
                'success': False,
                'error': "Could not fetch knock-knock joke at the moment. Try again later!"
            }

if __name__ == "__main__":
    # Test the joke generator
    print("Random Joke:")
    print(JokeGenerator.get_random_joke()['joke'])
    print("\n" + "="*50 + "\n")
    
    print("Programmer Joke:")
    print(JokeGenerator.get_programmer_joke()['joke'])
    print("\n" + "="*50 + "\n")
    
    print("Knock-Knock Joke:")
    print(JokeGenerator.get_knock_knock_joke()['joke'])
