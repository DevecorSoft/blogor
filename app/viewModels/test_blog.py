import os
from unittest import TestCase
from . import blog


class TestBlog(TestCase):
    def setUp(self) -> None:
        super().setUp()
        os.environ['blog_home'] = './test'
        os.system("mkdir test")
        os.system("echo '# test 1\n\na line of summary' > test/test1.md")
        os.system("echo '# test 2\n\na line of summary 2' > test/test2.md")

    def tearDown(self) -> None:
        super().tearDown()
        os.system("rm -rf test")

    def test_list_blog(self):
        blog_list = blog.list_blog()
        self.assertListEqual(
            [
                {
                    'id': 'test2',
                    'summary': ['# test 2\n', '\n', 'a line of summary 2\n']
                },
                {
                    'id': 'test1',
                    'summary': ['# test 1\n', '\n', 'a line of summary\n']
                },
            ],
            blog_list
        )

    def test_should_return_relative_path_of_blogs(self):
        blogs = blog.locate_blog()
        self.assertListEqual(blogs, ['./test/test2.md', './test/test1.md'])

    def test_should_return_summary_of_a_blog(self):
        summary = blog.get_blog_summary('./test/test1.md')
        self.assertListEqual(
            ['# test 1\n', '\n', 'a line of summary\n'],
            summary
        )

    def test_get_blog_content(self):
        def should_return_the_content_of_blog_when_it_exists():
            content = blog.get_blog_content('test1')
            self.assertEqual(content, '# test 1\n\na line of summary\n')

        def should_return_none_when_blog_is_not_existed():
            content = blog.get_blog_content('test')
            self.assertIsNone(content)

        should_return_none_when_blog_is_not_existed()
        should_return_the_content_of_blog_when_it_exists()
