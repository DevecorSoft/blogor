import json
import os

from django.test import TestCase
from django.test import Client


class GetBlogListApiTest(TestCase):
    client = Client()

    def setUp(self) -> None:
        super().setUp()
        os.environ['blog_home'] = '.'
        os.system("echo '# test 1\n\na line of summary' > test1.md")
        os.system("echo '# test 2\n\na line of summary 2' > test2.md")

    def tearDown(self) -> None:
        super().tearDown()
        os.system("rm test1.md")
        os.system("rm test2.md")

    def test_then_should_return_200(self):
        response = self.client.get("/blog/list/")
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.content)
        self.assertIsInstance(body, list)
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
            body
        )


class GetBlogApiTest(TestCase):
    client = Client()

    def setUp(self) -> None:
        super().setUp()
        os.environ['blog_home'] = '.'
        os.system("echo '# test 1\n\na line of summary' > test1.md")
        os.system("echo '# test 2\n\na line of summary 2' > test2.md")

    def tearDown(self) -> None:
        super().tearDown()
        os.system("rm test1.md")
        os.system("rm test2.md")

    def test_should_return_text_file_with_200(self):
        response = self.client.get('/blog/blog-test2.md/')
        blog = response.content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'# test 2\n\na line of summary 2\n', blog)

    def test_should_return_400_when_blog_is_not_existed(self):
        response = self.client.get('/blog/blog-test.md/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'')
