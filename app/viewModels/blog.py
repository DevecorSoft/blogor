import glob
import os
import threading
from typing import Dict, List


class SupportedLang(object):
    lang_zh = '_zh.md'
    lang_en = '.md'

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(SupportedLang, "_instance"):
            with SupportedLang._instance_lock:
                if not hasattr(SupportedLang, "_instance"):
                    SupportedLang._instance = object.__new__(cls)
        return SupportedLang._instance

    def map_from(self, lang):
        if lang == 'zh':
            return self.lang_zh
        else:
            return self.lang_en


def identify_by_id(path):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            return fun(args, kwargs)

        return wrapper

    return decorator


def locate_blog() -> List:
    blog_home = os.getenv('blog_home')
    return glob.glob(f'{blog_home}/*.md')


def get_blog_summary(path) -> List:
    with open(path, 'r') as f:
        summary = [f.readline() for _ in range(3)]
        f.close()
    return summary


def get_blog_content(blog_id) -> str:
    blog_home = os.getenv('blog_home')
    blog_file_path = f'{blog_home}/{blog_id}'
    if os.path.exists(blog_file_path):
        with open(blog_file_path, 'r') as f:
            return f.read()


def list_blog(lang='en') -> List:
    blog_set = merge_blog_by(lang)
    blog_list = [{'id': blog_id, 'summary': summary} for blog_id, summary in blog_set.items()]
    return blog_list


def _get_lang_from(path, **kwargs) -> None:
    on_zh = kwargs.get('on_zh', lambda: None)
    on_en = kwargs.get('on_en', lambda: None)
    if path.endswith(SupportedLang.lang_zh):
        on_zh()
        return SupportedLang.lang_zh
    else:
        on_en()
        return SupportedLang.lang_en


def _get_blog_id_from(path):
    suffix_size = len(_get_lang_from(path))
    return os.path.basename(path)[0:-suffix_size]


def merge_blog_by(lang) -> Dict:
    blog_set = {}
    supported_lang = SupportedLang().map_from(lang)

    for path in locate_blog():
        blog_id = _get_blog_id_from(path)

        if not blog_set.get(blog_id):
            blog_set[blog_id] = get_blog_summary(path)

        if _get_lang_from(path) == supported_lang:
            blog_set[blog_id] = get_blog_summary(path)

    return blog_set
