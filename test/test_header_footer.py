from __future__ import absolute_import

from asposeslidescloud import NotesSlideHeaderFooter, HeaderFooter
from test.base_test import BaseTest
import asposeslidescloud

class TestHeaderFooter(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_header_footer_all_slides(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = HeaderFooter()
        dto.is_footer_visible = True
        dto.footer_text = "footer"
        dto.is_date_time_visible = False
        BaseTest.slides_api.set_presentation_header_footer(file_name, dto, "password", folder_name)
        result = BaseTest.slides_api.get_slide_header_footer(file_name, 1, "password", folder_name)
        self.assertTrue(result.is_footer_visible)
        self.assertFalse(result.is_date_time_visible)

    def test_header_footer_slide(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = HeaderFooter()
        dto.is_footer_visible = True
        dto.footer_text = "footer"
        dto.is_date_time_visible = False
        result = BaseTest.slides_api.set_slide_header_footer(file_name, slide_index, dto, "password", folder_name)
        self.assertTrue(result.is_footer_visible)
        self.assertFalse(result.is_date_time_visible)
        result = BaseTest.slides_api.get_slide_header_footer(file_name, slide_index, "password", folder_name)
        self.assertTrue(result.is_footer_visible)
        self.assertFalse(result.is_date_time_visible)

    def test_header_footer_notes_slide(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = NotesSlideHeaderFooter()
        dto.is_header_visible = True
        dto.footer_text = "footer"
        dto.is_date_time_visible = False
        result = BaseTest.slides_api.set_notes_slide_header_footer(file_name, slide_index, dto, "password", folder_name)
        self.assertTrue(result.is_header_visible)
        self.assertFalse(result.is_date_time_visible)
        result = BaseTest.slides_api.get_notes_slide_header_footer(file_name, slide_index, "password", folder_name)
        self.assertTrue(result.is_header_visible)
        self.assertFalse(result.is_date_time_visible)