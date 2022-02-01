from django.http import HttpResponse, HttpResponseBadRequest
import json
import os
from .viewModels.blog import list_blog, get_blog_content
from django.views.decorators.http import require_GET


@require_GET
def blog_list(request):
    return HttpResponse(json.dumps(list_blog()))


@require_GET
def blog(request, blogId):
    content = get_blog_content(blogId)
    if content:
        return HttpResponse(content)
    return HttpResponseBadRequest()
