from django.http import HttpResponse
import json
import glob
import os
from .viewModels.blog import list_blog


def blog_list(request):
    return HttpResponse(json.dumps(list_blog()))
