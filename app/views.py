from django.http import HttpResponse, HttpResponseNotFound
import json
from .viewModels.blog import list_blog, get_blog_content
from django.views.decorators.http import require_GET


@require_GET
def blog_list(request):
    lang = request.GET.get('lang', 'en')
    return HttpResponse(json.dumps(list_blog(lang)))


@require_GET
def blog(request, blogId):
    lang = request.GET.get('lang', 'en')
    content = get_blog_content(blogId, lang)
    if content:
        return HttpResponse(content)
    return HttpResponseNotFound()
