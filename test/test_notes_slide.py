from __future__ import absolute_import

from test import constant
from asposeslidescloud import Portion, Paragraph, Shape, NotesSlide
from test.base_test import BaseTest
import asposeslidescloud

class TestNotesSlide(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_notes_slide_get_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.get_notes_slide(file_name, 1, "password", folder_name)
        self.assertTrue(result.text)

    def test_notes_slide_exists_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.notes_slide_exists(file_name, 1, "password", folder_name)
        self.assertTrue(result.exists)

    def test_notes_slide_download_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.download_notes_slide(file_name, 1, 'png', None, None, "password", folder_name)

    def test_notes_slide_get_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.get_notes_slide_online(source, 1, "password")
        self.assertTrue(result.text)

    def test_notes_slide_exists_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.notes_slide_exists_online(source, 1, "password")
        self.assertTrue(result.exists)

    def test_notes_slide_download_from_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.download_notes_slide_online(source, 1, 'png', None, None, "password")

    def test_notes_slide_shapes(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        shape_count = 3
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'notesSlide', password, folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

        dto = Shape()
        dto.x = 100
        dto.y = 100
        dto.width = 500
        dto.height = 200
        dto.shape_type = "Rectangle"
        dto.text = "New shape"
        shape = BaseTest.slides_api.create_special_slide_shape(file_name, slide_index, 'notesSlide', dto, None, None, password, folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'notesSlide', password, folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        dto.Text = "updated shape"
        shape = BaseTest.slides_api.update_special_slide_shape(file_name, slide_index, 'notesSlide', shape_count + 1, dto, password, folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'notesSlide', password, folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        BaseTest.slides_api.delete_special_slide_shape(file_name, slide_index, 'notesSlide', shape_count + 1, password, folder_name)
        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'notesSlide', password, folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

    def test_notes_slide_paragraphs(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        shape_index = 2
        paragraph_count = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'notesSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

        portion = Portion()
        portion.text = "New Paragraph"
        dto = Paragraph()
        dto.alignment = "Right"
        dto.portion_list = [ portion ]
        paragraph = BaseTest.slides_api.create_special_slide_paragraph(file_name, slide_index, 'notesSlide', shape_index, dto, None, password, folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'notesSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        dto = Paragraph()
        dto.alignment = "Center"
        paragraph = BaseTest.slides_api.update_special_slide_paragraph(file_name, slide_index, 'notesSlide', shape_index, paragraph_count + 1, dto, password, folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'notesSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        BaseTest.slides_api.delete_special_slide_paragraph(file_name, slide_index, 'notesSlide', shape_index, paragraph_count + 1, password, folder_name)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'notesSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

    def test_notes_slide_portions(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        shape_index = 2
        paragraph_index = 1
        portion_count = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count, len(portions.items))

        dto = Portion()
        dto.text = "New portion"
        dto.font_bold = "True"
        portion = BaseTest.slides_api.create_special_slide_portion(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, dto, None, password, folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        dto2 = Portion()
        dto2.text = "Updated portion"
        dto2.font_height = 22
        portion = BaseTest.slides_api.update_special_slide_portion(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, portion_count + 1, dto2, password, folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto2.font_height, portion.font_height)
        self.assertEqual(dto2.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        BaseTest.slides_api.delete_special_slide_portion(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, portion_count + 1, password, folder_name)
        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'notesSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count, len(portions.items))

    def test_create_notes_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        dto = NotesSlide()
        dto.text = constant.NOTES_SLIDE_TEXT
        slide_index = 1
        response = BaseTest.slides_api.create_notes_slide(constant.FILE_NAME, slide_index, dto, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)

    def test_update_notes_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        dto = NotesSlide()
        dto.text = constant.NOTES_SLIDE_TEXT
        slide_index = 1
        response = BaseTest.slides_api.update_notes_slide(constant.FILE_NAME, slide_index, dto, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)

    def test_delete_notes_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        response = BaseTest.slides_api.delete_notes_slide(constant.FILE_NAME, slide_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertIsNone(response.notes_slide)