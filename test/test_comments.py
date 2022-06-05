from __future__ import absolute_import

from asposeslidescloud import SlideComment, SlideModernComment
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestComments(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_create_comment(self):
        dto = SlideComment()
        dto.text = constant.COMMENT_TEXT
        dto.author = constant.COMMENT_AUTHOR
        child_comment = SlideComment()
        child_comment.text = constant.CHILD_COMMENT_TEXT
        child_comment.author = constant.COMMENT_AUTHOR
        dto.child_comments = [child_comment]

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 3
        response = BaseTest.slides_api.create_comment(constant.FILE_NAME, slide_index, dto, None, constant.PASSWORD,
                                                      constant.FOLDER_NAME)
        self.assertEqual(1, len(response.list))
        self.assertEqual(constant.COMMENT_AUTHOR, response.list[0].author)
        self.assertEqual(constant.COMMENT_TEXT, response.list[0].text)
        self.assertEqual(constant.CHILD_COMMENT_TEXT, response.list[0].child_comments[0].text)
        self.assertEqual(constant.COMMENT_AUTHOR, response.list[0].child_comments[0].author)

    def test_create_comment_online(self):
        dto = SlideComment()
        dto.text = constant.COMMENT_TEXT
        dto.author = constant.COMMENT_AUTHOR
        child_comment = SlideComment()
        child_comment.text = constant.CHILD_COMMENT_TEXT
        child_comment.author = constant.COMMENT_AUTHOR
        dto.child_comments = [child_comment]

        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            document = f.read()
        slide_index = 3
        output_document = BaseTest.slides_api.create_comment_online(document, slide_index, dto, None, constant.PASSWORD)

        self.assertIsNotNone(output_document)


    def test_get_slide_comments(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,  constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        response = BaseTest.slides_api.get_slide_comments(constant.FILE_NAME, slide_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.list))
        self.assertEqual(1, len(response.list[0].child_comments))

    def test_delete_comments(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        BaseTest.slides_api.delete_comments(constant.FILE_NAME, None, constant.PASSWORD, constant.FOLDER_NAME)
        response = BaseTest.slides_api.get_slide_comments(constant.FILE_NAME, slide_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(0, len(response.list))

    def test_delete_comments_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            document = f.read()
        output_document = BaseTest.slides_api.delete_comments_online(document, None, constant.PASSWORD)
        self.assertIsNotNone(output_document)

    def test_delete_slide_comments(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        BaseTest.slides_api.delete_slide_comments(constant.FILE_NAME, slide_index, None, constant.PASSWORD, constant.FOLDER_NAME)
        response = BaseTest.slides_api.get_slide_comments(constant.FILE_NAME, slide_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(0, len(response.list))

    def test_delete_slide_comments_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            document = f.read()
        slide_index = 1
        outputDocument = BaseTest.slides_api.delete_slide_comments_online(document, slide_index, None, constant.PASSWORD)
        self.assertIsNotNone(outputDocument)

    def test_create_modern_comment(self):
        text_selection_start_index = 1
        text_selection_length = 5

        child_comment = SlideModernComment()
        child_comment.author = constant.COMMENT_AUTHOR
        child_comment.text = constant.CHILD_COMMENT_TEXT
        child_comment.status = "Resolved"

        comment = SlideModernComment()
        comment.author = constant.COMMENT_AUTHOR
        comment.text = constant.COMMENT_TEXT
        comment.status = "Active"
        comment.text_selection_start = text_selection_start_index
        comment.text_selection_length = text_selection_length
        comment.child_comments = [child_comment]

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 3
        response = BaseTest.slides_api.create_comment(constant.FILE_NAME, slide_index, comment, None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(response.list))
        self.assertEqual("Modern", response.list[0].type)

    def test_create_shape_modern_comment(self):
        text_selection_start_index = 1
        text_selection_length = 5

        child_comment = SlideModernComment()
        child_comment.author = constant.COMMENT_AUTHOR
        child_comment.text = constant.CHILD_COMMENT_TEXT
        child_comment.status = "Resolved"

        comment = SlideModernComment()
        comment.author = constant.COMMENT_AUTHOR
        comment.text = constant.COMMENT_TEXT
        comment.status = "Active"
        comment.text_selection_start = text_selection_start_index
        comment.text_selection_length = text_selection_length
        comment.child_comments = [child_comment]

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 3
        shape_index = 1
        response = BaseTest.slides_api.create_comment(constant.FILE_NAME, slide_index, comment, shape_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(response.list))
        self.assertEqual("Modern", response.list[0].type)