from __future__ import absolute_import

import os

from asposeslidescloud import PdfExportOptions, ImageExportOptions, FontFallbackRule
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestConvert(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_convert_post_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.convert(source, 'pdf', "password")
        result_slides = BaseTest.slides_api.convert(source, 'pdf', "password", None, None, [ 2, 4 ])
        self.assertGreater(os.path.getsize(result), os.path.getsize(result_slides))

    def test_convert_put_from_request(self):
        out_path = "TestData/test.pdf"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.convert_and_save(source, 'pdf', out_path, "password")
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_post_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pdf"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.download_presentation(file_name, 'html5', None, "password", folder_name)

    def test_convert_put_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        out_path = "TestData/test.pdf"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.save_presentation(file_name, 'pdf', out_path, None, "password", folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_with_options_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.convert(source, 'pdf', "password")
        options = PdfExportOptions()
        options.draw_slides_frame = True
        result_with_options = BaseTest.slides_api.convert(source, 'pdf', "password", None, None, None, options)
        self.assertNotEqual(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_with_options_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.download_presentation(file_name, 'png', None, "password", folder_name)
        options = ImageExportOptions()
        options.width = 480
        options.height = 360
        result_with_options = BaseTest.slides_api.download_presentation(file_name, 'png', options, "password", folder_name)
        self.assertGreater(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_slide_post_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.download_slide_online(source, 1, 'pdf', None, None, "password")

    def test_convert_slide_put_from_request(self):
        out_path = "TestData/test.pdf"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.save_slide_online(source, 1, 'pdf', out_path, None, None, "password")
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_slide_post_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.download_slide(file_name, 1, 'pdf', None, None, None, "password", folder_name)

    def test_convert_slide_put_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        out_path = "TestData/test.pdf"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.save_slide(file_name, 1, 'pdf', out_path, None, None, None, "password", folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_slide_with_options_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.download_slide_online(source, 1, 'pdf', None, None, "password")
        options = PdfExportOptions()
        options.draw_slides_frame = True
        result_with_options = BaseTest.slides_api.download_slide_online(source, 1, 'pdf', None, None, "password", None, None, options)
        self.assertNotEqual(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_slide_with_options_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.download_slide(file_name, 1, 'pdf', None, None, None, "password", folder_name)
        options = PdfExportOptions()
        options.draw_slides_frame = True
        result_with_options = BaseTest.slides_api.download_slide(file_name, 1, 'pdf', options, None, None, "password", folder_name)
        self.assertNotEqual(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_shape_post_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.download_shape_online(source, 1, 3, 'png', None, None, None, "password")

    def test_convert_shape_put_from_request(self):
        out_path = "TestData/test.pdf"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.save_shape_online(source, 1, 1, 'png', out_path, None, None, None, "password")
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_shape_post_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.download_shape(file_name, 1, 1, 'png', None, None, None, None, "password", folder_name)

    def test_convert_shape_post_from_storage(self):
            BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
            slide_index = 1
            shape_index = 1
            path = "4/shapes"
            converted = BaseTest.slides_api.download_subshape(constant.FILE_NAME, slide_index, path, shape_index, 'png',
                                                              None, None, None, None, constant.PASSWORD, constant.FOLDER_NAME)
            self.assertIsNotNone(converted)

    def test_convert_shape_put_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        out_path = "TestData/test.png"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.save_shape(file_name, 1, 1, 'png', out_path, None, None, None, None, "password", folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_subshape_post_from_storage(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        out_path = "TestData/test.png"
        slide_index = 1
        shape_index = 1
        path = "4/shapes"
        BaseTest.slides_api.download_subshape(constant.FILE_NAME, slide_index, path, shape_index, 'png',
                                                        None, None, None, None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_with_font_fallback_rules(self):
        c_startUnicodeIndex = 0x0B80
        c_endUnicodeIndex = 0x0BFF

        font_rule1 = FontFallbackRule()
        font_rule1.range_start_index = c_startUnicodeIndex
        font_rule1.range_end_index = c_endUnicodeIndex
        font_rule1.fallback_font_list = ["Vijaya" ]

        font_rule2 = FontFallbackRule()
        font_rule2.range_start_index = c_startUnicodeIndex
        font_rule2.range_end_index = c_endUnicodeIndex
        font_rule2.fallback_font_list = ["Segoe UI Emoji", "Segoe UI Symbol", "Arial"]

        export_options = ImageExportOptions()
        export_options.font_fallback_rules = [font_rule1, font_rule2]

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        response = BaseTest.slides_api.download_presentation(constant.FILE_NAME, "png", export_options,
                                                             constant.PASSWORD, constant.FOLDER_NAME)
        self.assertIsNotNone(response)
