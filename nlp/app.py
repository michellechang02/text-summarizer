from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import nltk
from resources import SummarizeResource

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
api = Api(app)

# Define API routes
api.add_resource(SummarizeResource, '/summarize')

if __name__ == '__main__':
    app.run(debug=True)