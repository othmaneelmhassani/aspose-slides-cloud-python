from __future__ import absolute_import

from asposeslidescloud import SlideComment, SlideModernComment, Slide, ResourceUri, SlideBackground, SolidFill, NoFill
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestSlides(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_slides(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slides = BaseTest.slides_api.get_slides(constant.FILE_NAME, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(7, len(slides.slide_list))

    def test_get_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        slide = BaseTest.slides_api.get_slide(constant.FILE_NAME, slide_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertIsNotNone(slide)

    def test_create_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        layout_slide_path = "layoutSlides/3"
        slides = BaseTest.slides_api.create_slide(constant.FILE_NAME, layout_slide_path, 1, constant.PASSWORD,
                                                  constant.FOLDER_NAME)
        self.assertEqual(8, len(slides.slide_list))
        slides = BaseTest.slides_api.create_slide(constant.FILE_NAME, None, None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(9, len(slides.slide_list))

    def test_copy_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_to_copy_index = 3
        slides = BaseTest.slides_api.copy_slide(constant.FILE_NAME, slide_to_copy_index, None, None, None, None,
                                                constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(8, len(slides.slide_list))

    def test_copy_slide_from_source(self):
        source_file_name = "TemplateCV.pptx"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        BaseTest.slides_api.copy_file("TempTests/" + source_file_name,
                                      constant.FOLDER_NAME + "/" + source_file_name)
        slides = BaseTest.slides_api.copy_slide(constant.FILE_NAME, slide_index, 1, constant.FOLDER_NAME + "/" +
                                                source_file_name, None, None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(8, len(slides.slide_list))

    def test_move_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        slides = BaseTest.slides_api.move_slide(constant.FILE_NAME, slide_index, 2, constant.PASSWORD,
                                                constant.FOLDER_NAME)
        self.assertEqual(7, len(slides.slide_list))

    def test_reorder_slides(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        old_positions = [1, 2, 3, 4, 5, 6]
        new_positions = [6, 5, 4, 3, 2, 1]
        slides = BaseTest.slides_api.reorder_slides(constant.FILE_NAME, old_positions, new_positions, constant.PASSWORD,
                                                    constant.FOLDER_NAME)
        self.assertEqual(7, len(slides.slide_list))

    def test_update_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        layout_slide_path = "layoutSlides/3"
        dto = Slide()
        dto.layout_slide = ResourceUri()
        dto.layout_slide.href = layout_slide_path
        slide_index = 1
        slide = BaseTest.slides_api.update_slide(constant.FILE_NAME, slide_index, dto, constant.PASSWORD,
                                                 constant.FOLDER_NAME)
        self.assertTrue(layout_slide_path in slide.layout_slide.href)

    def test_delete_slides(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slides = BaseTest.slides_api.delete_slides(constant.FILE_NAME, None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(slides.slide_list))

    def test_delete_slide_indexes(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        indexes = [1, 3, 5]
        slides = BaseTest.slides_api.delete_slides(constant.FILE_NAME, indexes, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(4, len(slides.slide_list))

    def test_delete_slide(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        slides = BaseTest.slides_api.delete_slide(constant.FILE_NAME, slide_index, constant.PASSWORD,
                                                  constant.FOLDER_NAME)
        self.assertEqual(6, len(slides.slide_list))

    def test_get_background(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 5
        response = BaseTest.slides_api.get_background(constant.FILE_NAME, slide_index, constant.PASSWORD,
                                                      constant.FOLDER_NAME)
        self.assertTrue(isinstance(response.fill_format, SolidFill))

    def test_set_background(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        dto = SlideBackground()
        fill_format = SolidFill()
        fill_format.color = constant.COLOR
        dto.fill_format = fill_format
        slide_index = 1
        response = BaseTest.slides_api.set_background(constant.FILE_NAME, slide_index, dto, constant.PASSWORD,
                                                      constant.FOLDER_NAME)
        self.assertTrue(isinstance(response.fill_format, SolidFill))
        self.assertEqual(constant.COLOR, response.fill_format.color)

    def test_set_background_color(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        response = BaseTest.slides_api.set_background_color(constant.FILE_NAME, slide_index, constant.COLOR,
                                                            constant.PASSWORD, constant.FOLDER_NAME)
        self.assertTrue(isinstance(response.fill_format, SolidFill))
        self.assertEqual(constant.COLOR, response.fill_format.color)

    def test_delete_background(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 5
        response = BaseTest.slides_api.delete_background(constant.FILE_NAME, slide_index, constant.PASSWORD,
                                                         constant.FOLDER_NAME)
        self.assertTrue(isinstance(response.fill_format, NoFill))