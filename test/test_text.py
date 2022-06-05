from __future__ import absolute_import

from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestText(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_text_get(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.get_presentation_text_items(file_name, None, password, folder_name)
        result_with_empty = BaseTest.slides_api.get_presentation_text_items(file_name, True, password, folder_name)
        slide_result = BaseTest.slides_api.get_slide_text_items(file_name, slide_index, None, password, folder_name)
        slide_result_with_empty = BaseTest.slides_api.get_slide_text_items(file_name, slide_index, True, password, folder_name)
        self.assertLess(len(result.items), len(result_with_empty.items))
        self.assertLess(len(slide_result.items), len(result.items))
        self.assertLess(len(slide_result.items), len(slide_result_with_empty.items))

    def test_text_replace_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        old_value = "text"
        new_value = "new_text"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.replace_presentation_text(file_name, old_value, new_value, None, password, folder_name)
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result_with_empty = BaseTest.slides_api.replace_presentation_text(file_name, old_value, new_value, True, password, folder_name)
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        slide_result = BaseTest.slides_api.replace_slide_text(file_name, slide_index, old_value, new_value, None, password, folder_name)
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        slide_result_with_empty = BaseTest.slides_api.replace_slide_text(file_name, slide_index, old_value, new_value, True, password, folder_name)
        self.assertLess(result.matches, result_with_empty.matches)
        self.assertLess(slide_result.matches, result.matches)
        self.assertLess(slide_result.matches, slide_result_with_empty.matches)

    def test_text_replace_request(self):
        password = "password"
        slide_index = 1
        old_value = "text"
        new_value = "new_text"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.replace_presentation_text_online(source, old_value, new_value, None, password)
        BaseTest.slides_api.replace_presentation_text_online(source, old_value, new_value, True, password)
        BaseTest.slides_api.replace_slide_text_online(source, slide_index, old_value, new_value, None, password)
        BaseTest.slides_api.replace_slide_text_online(source, slide_index, old_value, new_value, True, password)

    def test_highlight_shape_text(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        text_to_highlight = "highlight"
        BaseTest.slides_api.highlight_shape_text(constant.FILE_NAME, slide_index, shape_index, text_to_highlight,
                                                 constant.COLOR, None, False, constant.PASSWORD, constant.FOLDER_NAME)
        para = BaseTest.slides_api.get_paragraph(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                 constant.PASSWORD, constant.FOLDER_NAME)
        self.assertNotEqual(para.portion_list[0].text, text_to_highlight)
        self.assertNotEqual(para.portion_list[0].highlight_color, constant.COLOR)
        self.assertEqual(para.portion_list[1].text, text_to_highlight)
        self.assertEqual(para.portion_list[1].highlight_color, constant.COLOR)

    def test_highlight_shape_regex(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        text_to_highlight = "highlight"
        regex = "h.ghl[abci]ght"
        BaseTest.slides_api.highlight_shape_regex(constant.FILE_NAME, slide_index, shape_index, regex,
                                                 constant.COLOR, None, False, constant.PASSWORD, constant.FOLDER_NAME)
        para = BaseTest.slides_api.get_paragraph(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                 constant.PASSWORD, constant.FOLDER_NAME)
        self.assertNotEqual(para.portion_list[0].text, text_to_highlight)
        self.assertNotEqual(para.portion_list[0].highlight_color, constant.COLOR)
        self.assertEqual(para.portion_list[1].text, text_to_highlight)
        self.assertEqual(para.portion_list[1].highlight_color, constant.COLOR)