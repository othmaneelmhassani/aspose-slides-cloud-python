from __future__ import absolute_import

import base64
import os

from asposeslidescloud import PictureFrame, PictureFill, Shape
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestWatermark(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_watermark_text_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        watermark_text = "watermarkText"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        get1_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        BaseTest.slides_api.create_watermark(file_name, None, None, watermark_text, None, None, password, folder_name)
        get2_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(file_name, slide_index, shape_count, password, folder_name)
        self.assertEqual("watermark", shape.name)
        self.assertEqual(watermark_text, shape.text)
        BaseTest.slides_api.delete_watermark(file_name, None, password, folder_name)
        get3_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_dto_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        watermark_text = "watermarkText"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        get1_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        watermark = Shape()
        watermark.text = watermark_text
        BaseTest.slides_api.create_watermark(file_name, watermark, None, None, None, None, password, folder_name)
        get2_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(file_name, slide_index, shape_count, password, folder_name)
        self.assertEqual("watermark", shape.name)
        self.assertEqual(watermark_text, shape.text)
        BaseTest.slides_api.delete_watermark(file_name, None, password, folder_name)
        get3_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_image_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        get1_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/watermark.png", 'rb') as f:
            source = f.read()
        BaseTest.slides_api.create_image_watermark(file_name, source, None, password, folder_name)
        get2_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(file_name, slide_index, shape_count, password, folder_name)
        self.assertEqual("watermark", shape.name)
        BaseTest.slides_api.delete_watermark(file_name, None, password, folder_name)
        get3_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_image_dto_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        watermark_name = "myWatermark"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        get1_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/watermark.png", 'rb') as f:
            source = f.read()
        watermark = PictureFrame()
        fill_format = PictureFill()
        fill_format.base64_data = base64.b64encode(source).decode('utf-8')
        watermark.fill_format = fill_format
        watermark.name = watermark_name
        BaseTest.slides_api.create_image_watermark(file_name, None, watermark, password, folder_name)
        get2_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(file_name, slide_index, shape_count, password, folder_name)
        self.assertEqual(watermark_name, shape.name)
        BaseTest.slides_api.delete_watermark(file_name, watermark_name, password, folder_name)
        get3_result = BaseTest.slides_api.get_shapes(file_name, slide_index, password, folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_text_request(self):
        password = "password"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        post_result = BaseTest.slides_api.create_watermark_online(source, None, None, "watermarkText", None, None, password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))

    def test_watermark_dto_request(self):
        password = "password"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        watermark = Shape()
        watermark.text = "watermarkText"
        post_result = BaseTest.slides_api.create_watermark_online(source, watermark, None, None, None, None, password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))

    def test_watermark_image_request(self):
        password = "password"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/watermark.png", 'rb') as f:
            watermark = f.read()
        post_result = BaseTest.slides_api.create_image_watermark_online(source, watermark, None, password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))

    def test_watermark_image_dto_request(self):
        password = "password"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/watermark.png", 'rb') as f:
            watermark_source = f.read()
        watermark = PictureFrame()
        fill_format = PictureFill()
        fill_format.base64_data = base64.b64encode(watermark_source).decode('utf-8')
        watermark.fill_format = fill_format
        post_result = BaseTest.slides_api.create_image_watermark_online(source, None, watermark, password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))
