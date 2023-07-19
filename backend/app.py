from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/check_connection')
def check_connection():
    try:
        mongo.db.command('ping')
        return 'Database connection successful'
    except Exception as e:
        return f'Error connecting to database: {str(e)}'


if __name__ == "__main__":
    app.run()
