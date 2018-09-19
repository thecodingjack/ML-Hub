import os
import sys
from app import app

PORT = os.environ.get('PORT')
if __name__ == '__main__':
    print(PORT)
    app.run(host='0.0.0.0', port=int(PORT), debug=True) # Run the app