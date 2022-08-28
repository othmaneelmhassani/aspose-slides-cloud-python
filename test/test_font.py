from __future__ import absolute_import

from asposeslidescloud.rest import ApiException
from test import constant
from test.base_test import BaseTest
import asposeslidescloud

class TestFont(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_fonts(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        response = BaseTest.slides_api.get_fonts(constant.FILE_NAME, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(3, len(response.list))

    def test_get_fonts_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.get_fonts_online(source, constant.PASSWORD)
        self.assertEqual(3, len(response.list))

    def test_set_embedded_font(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        font_name = "Calibri"
        response = BaseTest.slides_api.set_embedded_font(constant.FILE_NAME, font_name, False, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(None, response.list[0].is_embedded)
        self.assertEqual(None, response.list[1].is_embedded)
        self.assertEqual(True, response.list[2].is_embedded)

    def test_set_embedded_font_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        font_name = "Calibri"
        response = BaseTest.slides_api.set_embedded_font_online(source, font_name, False, constant.PASSWORD)

    def test_delete_embedded_font(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        font_name = "Calibri"
        response = BaseTest.slides_api.set_embedded_font(constant.FILE_NAME, font_name, False, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(True, response.list[2].is_embedded)
        response = BaseTest.slides_api.delete_embedded_font(constant.FILE_NAME, font_name, constant.PASSWORD,
                                                         constant.FOLDER_NAME)
        self.assertEqual(None, response.list[2].is_embedded)

    def test_delete_embedded_font_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        font_name = "Calibri"
        response = BaseTest.slides_api.set_embedded_font_online(source, font_name, False, constant.PASSWORD)
        with open(response, 'rb') as f:
            source_embedded = f.read()
        BaseTest.slides_api.delete_embedded_font_online(source_embedded, font_name, constant.PASSWORD)
