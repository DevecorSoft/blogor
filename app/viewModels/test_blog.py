import os
from unittest import TestCase
from . import blog


class TestBlog(TestCase):
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

    def test_should_return_content_of_a_blog(self):
        content = blog.get_blog_content('test1.md')
        self.assertEqual(content, '# test 1\n\na line of summary\n')

    def test_should_return_None_when_blog_is_not_existed(self):
        content = blog.get_blog_content('test.md')
        self.assertIsNone(content)