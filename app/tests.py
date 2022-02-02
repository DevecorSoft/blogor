import json
import os

from django.test import TestCase
from django.test import Client


class GetBlogListApiTest(TestCase):
    client = Client()

    def setUp(self) -> None:
        super().setUp()
        os.environ['blog_home'] = './test'
        os.system("mkdir test")
        os.system("echo '# test 1\n\na line of summary' > test/test1.md")
        os.system("echo '# test 2\n\na line of summary 2' > test/test2.md")
        os.system("echo '# test 3\n\na line of summary 3' > test/test3.md")
        os.system("echo '# 测试 1\n\n一行简介' > test/test1_zh.md")
        os.system("echo '# 测试 2\n\n一行摘要' > test/test2_zh.md")

    def tearDown(self) -> None:
        super().tearDown()
        os.system("rm -rf test")

    def test_then_should_return_200(self):
        response = self.client.get("/blog/list/")
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.content)
        self.assertIsInstance(body, list)
        self.assertListEqual(
            [
                {
                    'id': 'test3',
                    'summary': ['# test 3\n', '\n', 'a line of summary 3\n']
                },
                {
                    'id': 'test2',
                    'summary': ['# test 2\n', '\n', 'a line of summary 2\n']
                },
                {
                    'id': 'test1',
                    'summary': ['# test 1\n', '\n', 'a line of summary\n']
                },
            ],
            body
        )

    def test_should_return_blog_list_in_zh_cn(self):
        response = self.client.get('/blog/list/?lang=zh')
        body = json.loads(response.content)
        self.assertListEqual(
            body,
            [
                {
                    'id': 'test3',
                    'summary': ['# test 3\n', '\n', 'a line of summary 3\n']
                },
                {
                    'id': 'test2',
                    'summary': ['# 测试 2\n', '\n', '一行摘要\n']
                },
                {
                    'id': 'test1',
                    'summary': ['# 测试 1\n', '\n', '一行简介\n']
                }
            ]
        )


class GetBlogApiTest(TestCase):
    client = Client()

    def setUp(self) -> None:
        super().setUp()
        os.environ['blog_home'] = './test'
        os.system("mkdir test")
        os.system("echo '# test 1\n\na line of summary' > test/test1.md")
        os.system("echo '# test 2\n\na line of summary 2' > test/test2.md")

    def tearDown(self) -> None:
        super().tearDown()
        os.system("rm -rf test")

    def test_should_return_text_file_with_200(self):
        response = self.client.get('/blog/blog-test2.md/')
        blog = response.content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'# test 2\n\na line of summary 2\n', blog)

    def test_should_return_400_when_blog_is_not_existed(self):
        response = self.client.get('/blog/blog-test.md/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'')
