import os
from unittest import TestCase
from . import blog


class Test(TestCase):
    def setUp(self) -> None:
        super().setUp()
        os.environ['blog_home'] = '.'
        os.system("echo '# test 1\n\na line of summary' > test1.md")
        os.system("echo '# test 2\n\na line of summary 2' > test2.md")

    def tearDown(self) -> None:
        super().tearDown()
        os.system("rm test1.md")
        os.system("rm test2.md")

    def test_list_blog(self):
        blog_list = blog.list_blog()
        self.assertListEqual(
            [
                {
                    'id': 'test2.md',
                    'summary': ['# test 2\n', '\n', 'a line of summary 2\n']
                },
                {
                    'id': 'test1.md',
                    'summary': ['# test 1\n', '\n', 'a line of summary\n']
                },
            ],
            blog_list
        )

    def test_should_return_relative_path_of_blogs(self):
        blogs = blog.locate_blog()
        self.assertListEqual(blogs, ['./test2.md', './test1.md'])

    def test_should_return_summary_of_a_blog(self):
        summary = blog.get_blog_summary('./test1.md')
        self.assertDictEqual(
            {
                'id': 'test1.md',
                'summary': ['# test 1\n', '\n', 'a line of summary\n']
            },
            summary
        )
