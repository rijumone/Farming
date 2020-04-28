import os
import dotenv

dotenv.load_dotenv()

class Config:
    CREDENTIALS = {
        'INSTAGRAM': {
            'USERNAME': os.environ.get('CREDENTIALS__INSTAGRAM__USERNAME'),
            'PASSWORD': os.environ.get('CREDENTIALS__INSTAGRAM__PASSWORD'),
        }
    }
    
