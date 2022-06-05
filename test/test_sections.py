from __future__ import absolute_import

from asposeslidescloud import Sections, Section
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestSections(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_sections_get(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.get_sections(file_name, "password", folder_name)
        self.assertEqual(3, len(result.section_list))

    def test_sections_replace(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = Sections()
        section1 = Section()
        section1.name = "Section1"
        section1.first_slide_index = 1
        section2 = Section()
        section2.name = "Section2"
        section2.first_slide_index = 3
        dto.section_list = [ section1, section2 ]
        result = BaseTest.slides_api.set_sections(file_name, dto, "password", folder_name)
        self.assertEqual(len(dto.section_list), len(result.section_list))
        self.assertEqual(section2.first_slide_index - section1.first_slide_index, len(result.section_list[0].slide_list))

    def test_sections_post(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.create_section(file_name, "NewSection", 5, "password", folder_name)
        self.assertEqual(4, len(result.section_list))

    def test_sections_put(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        section_index = 2
        section_name = "UpdatedSection"
        result = BaseTest.slides_api.update_section(file_name, section_index, section_name, "password", folder_name)
        self.assertEqual(3, len(result.section_list))
        self.assertEqual(section_name, result.section_list[section_index - 1].name)

    def test_sections_move(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.move_section(file_name, 1, 2, "password", folder_name)
        self.assertEqual(3, len(result.section_list))

    def test_sections_clear(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_sections(file_name, None, None, "password", folder_name)
        self.assertEqual(0, len(result.section_list))

    def test_sections_delete_many(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_sections(file_name, [ 2, 3 ], None, "password", folder_name)
        self.assertEqual(1, len(result.section_list))

    def test_sections_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_section(file_name, 2, None, "password", folder_name)
        self.assertEqual(2, len(result.section_list))