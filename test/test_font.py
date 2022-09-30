from __future__ import absolute_import

from asposeslidescloud import FontSubstRule, ImageExportOptions
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
        response = BaseTest.slides_api.set_embedded_font(constant.FILE_NAME, constant.FONT_NAME_CALIBRI, False,
                                                         constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(None, response.list[0].is_embedded)
        self.assertEqual(True, response.list[1].is_embedded)
        self.assertEqual(True, response.list[2].is_embedded)

    def test_set_embedded_font_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_online(source, constant.FONT_NAME_CALIBRI, False,
                                                                constant.PASSWORD)

    def test_set_embedded_font_from_request(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FONT_FILE_NAME, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_from_request(source, constant.FILE_NAME, False,
                                                                      constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(None, response.list[0].is_embedded)
        self.assertEqual(True, response.list[1].is_embedded)
        self.assertEqual(True, response.list[2].is_embedded)
        self.assertEqual(constant.FONT_NAME_CALIBRI, response.list[2].font_name)

    def test_set_embedded_font_from_request_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source_file = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FONT_FILE_NAME, 'rb') as f:
            source_font_file = f.read()
        response = BaseTest.slides_api.set_embedded_font_from_request_online(source_file, source_font_file, False,
                                                                      constant.PASSWORD)

    def test_delete_embedded_font(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        response = BaseTest.slides_api.set_embedded_font(constant.FILE_NAME, constant.FONT_NAME_CALIBRI, False,
                                                         constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(True, response.list[2].is_embedded)
        response = BaseTest.slides_api.delete_embedded_font(constant.FILE_NAME, constant.FONT_NAME_CALIBRI, constant.PASSWORD,
                                                         constant.FOLDER_NAME)
        self.assertEqual(None, response.list[2].is_embedded)

    def test_delete_embedded_font_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_online(source, constant.FONT_NAME_CALIBRI, False, constant.PASSWORD)
        with open(response, 'rb') as f:
            source_embedded = f.read()
        BaseTest.slides_api.delete_embedded_font_online(source_embedded, constant.FONT_NAME_CALIBRI, constant.PASSWORD)

    def test_replace_font(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        response = BaseTest.slides_api.replace_font(constant.FILE_NAME, constant.FONT_NAME_CALIBRI,
                                                      constant.FONT_NAME_TIMES, True, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(True, response.list[2].is_embedded)
        self.assertEqual(constant.FONT_NAME_TIMES, response.list[2].font_name)

    def test_replace_font_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.replace_font_online(source, constant.FONT_NAME_CALIBRI,
                                                      constant.FONT_NAME_TIMES, True, constant.PASSWORD, constant.FOLDER_NAME)

    def test_font_substitution(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        font_rule1 = FontSubstRule()
        font_rule1.source_font = constant.FONT_NAME
        font_rule1.target_font = constant.FONT_NAME_TIMES
        font_rule1.not_found_only = False
        font_rule2 = FontSubstRule()
        font_rule2.source_font = constant.FONT_NAME_CALIBRI
        font_rule2.target_font = constant.FONT_NAME_TIMES

        exportOptions = ImageExportOptions()
        exportOptions.font_subst_rules = [font_rule1, font_rule2]
        response = BaseTest.slides_api.download_presentation(constant.FILE_NAME, "PNG", exportOptions,
                                                             constant.PASSWORD, constant.FOLDER_NAME)
