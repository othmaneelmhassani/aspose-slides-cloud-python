from __future__ import absolute_import

from asposeslidescloud import PictureFrame, Hyperlink, Portion, Shape
from test.base_test import BaseTest
import asposeslidescloud

class TestHyperlink(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_hyperlink_get_shape(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        shape = BaseTest.slides_api.get_shape(file_name, 2, 2, "password", folder_name)
        self.assertIsNotNone(shape.hyperlink_click)
        self.assertEqual("Hyperlink", shape.hyperlink_click.action_type)
        self.assertIsNone(shape.hyperlink_mouse_over)

    def test_hyperlink_get_portion(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        portion = BaseTest.slides_api.get_portion(file_name, 2, 1, 1, 2, "password", folder_name)
        self.assertIsNone(portion.hyperlink_click)
        self.assertIsNotNone(portion.hyperlink_mouse_over)
        self.assertEqual("JumpLastSlide", portion.hyperlink_mouse_over.action_type)

    def test_hyperlink_create_shape(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        shape = Shape()
        hyperlink = Hyperlink()
        hyperlink.action_type = "Hyperlink"
        hyperlink.external_url = "https://docs.aspose.cloud/slides"
        shape.hyperlink_click = hyperlink
        updated_shape = BaseTest.slides_api.update_shape(file_name, 2, 2, shape, "password", folder_name)
        self.assertIsNotNone(updated_shape.hyperlink_click)
        self.assertEqual(shape.hyperlink_click.external_url, updated_shape.hyperlink_click.external_url)

    def test_hyperlink_create_portion(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = Portion()
        dto.text = "Link text"
        hyperlink = Hyperlink()
        hyperlink.action_type = "JumpLastSlide"
        dto.hyperlink_mouse_over = hyperlink
        updated_portion = BaseTest.slides_api.create_portion(file_name, 1, 1, 1, dto, None, "password", folder_name)
        self.assertIsNotNone(updated_portion.hyperlink_mouse_over)
        self.assertEqual(dto.hyperlink_mouse_over.action_type, updated_portion.hyperlink_mouse_over.action_type)

    def test_hyperlink_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        shape = PictureFrame()
        hyperlink = Hyperlink()
        hyperlink.is_disabled = True
        shape.hyperlink_click = hyperlink
        updated_shape = BaseTest.slides_api.update_shape(file_name, 2, 2, shape, "password", folder_name)
        self.assertIsNone(updated_shape.hyperlink_click)