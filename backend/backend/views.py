from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import TextSummary  # Import the model you just created
from .nlp import TextSummarizer

@csrf_exempt
def post_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text_to_summarize = data.get('text', '')
            print(text_to_summarize)
            ts = TextSummarizer()
            summary = ts.generate_summary(text_to_summarize)
            print(summary)
            
            # Create and save the new TextSummary instance to the database
            TextSummary.objects.create(original_text=text_to_summarize, summarized_text=summary)
            
            return JsonResponse({'summary': summary})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return HttpResponse("This endpoint only supports POST requests.", status=405)
    

def get_summary(request):
    # Fetch all text summaries from the database
    summaries = TextSummary.objects.all()
     # Prepare data to be JSON serializable
    data = list(summaries.values("original_text", "summarized_text"))

    # Return the data as a JSON response
    return JsonResponse(data, safe=False)
