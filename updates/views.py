from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json

# Create your views here.
#def detail_view(request):
#    return HttpResponse(get_template().render({{})) # return JSON data --> JS object Notion

def json_example_view(request):
    # URL -- for a REST API
    
    data = {
        "count": 1000,
        "content": "Some new"
    }
    
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')