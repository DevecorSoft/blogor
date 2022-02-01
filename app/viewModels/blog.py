import glob
import os
from typing import Dict, List

def locate_blog() -> List:
    blog_home = os.getenv('blog_home')
    return glob.glob(f'{blog_home}/*.md')


def get_blog_summary(path) -> Dict:
    id = os.path.basename(path)
    with open(path, 'r') as f:
        summary = [f.readline() for _ in range(3)]
        f.close()
    return {'id': id, 'summary': summary}


def get_blog_content(blogId) -> str:
    blog_home = os.getenv('blog_home')
    blog_file_path = f'{blog_home}/{blogId}'
    if os.path.exists(blog_file_path):
        with open(blog_file_path, 'r') as f:
            return f.read()


def list_blog() -> List:
    blogs = locate_blog()
    blog_list = []
    for i in blogs:
        blog_list.append(get_blog_summary(i))
    return blog_list
