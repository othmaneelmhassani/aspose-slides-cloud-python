from __future__ import absolute_import

from asposeslidescloud import SlideAnimation, Effect, Portion, Paragraph, Shape
from test import constant
from test.base_test import BaseTest
import asposeslidescloud

class TestMasterSlides(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_master_slides(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        source_file = "TemplateCV.pptx"
        source_path = folder_name + "/" + source_file
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.copy_file("TempTests/" + source_file, source_path)

        master_slides = BaseTest.slides_api.get_master_slides(file_name, password, folder_name)
        self.assertEqual(1, len(master_slides.slide_list))

        master_slide = BaseTest.slides_api.get_master_slide(file_name, 1, password, folder_name)
        self.assertEqual("Office Theme", master_slide.name)

        master_slide = BaseTest.slides_api.copy_master_slide(file_name, source_path, 1, None, None, None, password, folder_name)
        self.assertEqual("Digital portfolio", master_slide.name)

        master_slides = BaseTest.slides_api.get_master_slides(file_name, password, folder_name)
        self.assertEqual(2, len(master_slides.slide_list))

    def test_master_slide_shapes(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        shape_count = 6
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'masterSlide', password, folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

        dto = Shape()
        dto.x = 100
        dto.y = 100
        dto.width = 500
        dto.height = 200
        dto.shape_type = "Rectangle"
        dto.text = "New shape"
        shape = BaseTest.slides_api.create_special_slide_shape(file_name, slide_index, 'masterSlide', dto, None, None, password, folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'masterSlide', password, folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        dto.Text = "updated shape"
        shape = BaseTest.slides_api.update_special_slide_shape(file_name, slide_index, 'masterSlide', shape_count + 1, dto, password, folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'masterSlide', password, folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        BaseTest.slides_api.delete_special_slide_shape(file_name, slide_index, 'masterSlide', shape_count + 1, password, folder_name)
        shapes = BaseTest.slides_api.get_special_slide_shapes(file_name, slide_index, 'masterSlide', password, folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

    def test_master_slide_paragraphs(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        shape_index = 2
        paragraph_count = 5
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'masterSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

        portion = Portion()
        portion.text = "New Paragraph"
        dto = Paragraph()
        dto.alignment = "Right"
        dto.portion_list = [ portion ]
        paragraph = BaseTest.slides_api.create_special_slide_paragraph(file_name, slide_index, 'masterSlide', shape_index, dto, None, password, folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'masterSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        dto = Paragraph()
        dto.alignment = "Center"
        paragraph = BaseTest.slides_api.update_special_slide_paragraph(file_name, slide_index, 'masterSlide', shape_index, paragraph_count + 1, dto, password, folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'masterSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        BaseTest.slides_api.delete_special_slide_paragraph(file_name, slide_index, 'masterSlide', shape_index, paragraph_count + 1, password, folder_name)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(file_name, slide_index, 'masterSlide', shape_index, password, folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

    def test_master_slide_portions(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        shape_index = 2
        paragraph_index = 3
        portion_count = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count, len(portions.items))

        dto = Portion()
        dto.text = "New portion"
        dto.font_bold = "True"
        portion = BaseTest.slides_api.create_special_slide_portion(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, dto, None, password, folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        dto2 = Portion()
        dto2.text = "Updated portion"
        dto2.font_height = 22
        portion = BaseTest.slides_api.update_special_slide_portion(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, portion_count + 1, dto2, password, folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto2.font_height, portion.font_height)
        self.assertEqual(dto2.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        BaseTest.slides_api.delete_special_slide_portion(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, portion_count + 1, password, folder_name)
        portions = BaseTest.slides_api.get_special_slide_portions(file_name, slide_index, 'masterSlide', shape_index, paragraph_index, password, folder_name)
        self.assertEqual(portion_count, len(portions.items))

    def test_master_slide_animation(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        animation = BaseTest.slides_api.get_special_slide_animation(file_name, slide_index, 'masterSlide', None, None, password, folder_name)
        self.assertEqual(1, len(animation.main_sequence))

        effect1 = Effect()
        effect1.type = "Blink"
        effect1.shape_index = 2

        effect2 = Effect()
        effect2.type = "Appear"
        effect2.shape_index = 3

        dto = SlideAnimation()
        dto.main_sequence = [ effect1, effect2 ]
        animation = BaseTest.slides_api.set_special_slide_animation(file_name, slide_index, 'masterSlide', dto, password, folder_name)
        self.assertEqual(len(dto.main_sequence), len(animation.main_sequence))

        animation = BaseTest.slides_api.get_special_slide_animation(file_name, slide_index, 'masterSlide', 3, None, password, folder_name)
        self.assertEqual(1, len(animation.main_sequence))

        BaseTest.slides_api.delete_special_slide_animation_effect(file_name, slide_index, 'masterSlide', 2, password, folder_name)
        self.assertEqual(len(dto.main_sequence) - 1, len(animation.main_sequence))

        animation = BaseTest.slides_api.get_special_slide_animation(file_name, slide_index, 'masterSlide', 3, None, password, folder_name)
        self.assertEqual(0, len(animation.main_sequence))

        BaseTest.slides_api.delete_special_slide_animation(file_name, slide_index, 'masterSlide', password, folder_name)
        self.assertEqual(0, len(animation.main_sequence))

    def test_master_slide_delete_unused(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)

        result = BaseTest.slides_api.delete_unused_master_slides(constant.FILE_NAME, True, constant.PASSWORD,
                                                                 constant.FOLDER_NAME)
        self.assertEqual(1, len(result.slide_list))

    def test_master_slide_delete_unused_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            file = f.read()

        result = BaseTest.slides_api.delete_unused_master_slides_online(file, True, constant.PASSWORD)
        self.assertIsNotNone(result)
