from flask_restful import Resource, reqparse
from models import nlp_items
from nlp import summarize_text  # Assuming summarize_text is in nlp.py

class SummarizeResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text', type=str, required=True, help="Text cannot be blank.")

    def post(self):
        data = SummarizeResource.parser.parse_args()
        input_text = data['text']
        # Summarize the input text
        summary = summarize_text(input_text)
        
        return {'summary': summary}, 200

    
    


