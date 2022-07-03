
from __future__ import absolute_import

from asposeslidescloud import Portion, SolidFill
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestPortions(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_portions(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        response = BaseTest.slides_api.get_portions(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                    constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.items))

    def test_get_sub_shape_portions(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.get_subshape_portions(constant.FILE_NAME, slide_index, shape_path, shape_index,
                                                             paragraph_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.items))

    def test_get_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        portion_index = 1
        response = BaseTest.slides_api.get_portion(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                   portion_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertTrue(constant.PORTION_TEXT in response.text)

    def test_get_sub_shape_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        portion_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.get_subshape_portion(constant.FILE_NAME, slide_index, shape_path, shape_index,
                                                             paragraph_index, portion_index, constant.PASSWORD,
                                                             constant.FOLDER_NAME)
        self.assertTrue(constant.PORTION_TEXT in response.text)

    def test_create_portion(self):
        dto = Portion()
        dto.text = constant.PORTION_TEXT
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = constant.FONT_NAME
        fill_format = SolidFill()
        fill_format.color = constant.COLOR
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        response = BaseTest.slides_api.create_portion(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                      dto, None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_create_sub_shape_portion(self):
        dto = Portion()
        dto.text = constant.PORTION_TEXT
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = constant.FONT_NAME
        fill_format = SolidFill()
        fill_format.color = constant.COLOR
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.create_subshape_portion(constant.FILE_NAME, slide_index, shape_path, shape_index,
                                                               paragraph_index, dto, None, constant.PASSWORD,
                                                               constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_update_portion(self):
        dto = Portion()
        dto.text = constant.PORTION_TEXT
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = constant.FONT_NAME
        fill_format = SolidFill()
        fill_format.color = constant.COLOR
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        portion_index = 1
        response = BaseTest.slides_api.update_portion(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                      portion_index, dto, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_update_sub_shape_portion(self):
        dto = Portion()
        dto.text = constant.PORTION_TEXT
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = constant.FONT_NAME
        fill_format = SolidFill()
        fill_format.color = constant.COLOR
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        portion_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.update_subshape_portion(constant.FILE_NAME, slide_index, shape_path, shape_index,
                                                               paragraph_index, portion_index, dto, constant.PASSWORD,
                                                               constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_delete_portions(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        response = BaseTest.slides_api.delete_portions(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                       None, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(0, len(response.items))

    def test_delete_portions_indexes(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        response = BaseTest.slides_api.delete_portions(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                       [1], constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(response.items))

    def test_delete_sub_shape_portions(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.delete_subshape_portions(constant.FILE_NAME, slide_index, shape_path,
                                                                 shape_index, paragraph_index, None, constant.PASSWORD,
                                                                 constant.FOLDER_NAME)
        self.assertEqual(0, len(response.items))

    def test_delete_sub_shape_portions_indexes(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.delete_subshape_portions(constant.FILE_NAME, slide_index, shape_path, shape_index,
                                                       paragraph_index, [1], constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(response.items))

    def test_delete_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        portion_index = 1
        response = BaseTest.slides_api.delete_portion(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                      portion_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(response.items))

    def test_delete_sub_shape_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        portion_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.delete_subshape_portion(constant.FILE_NAME, slide_index, shape_path, shape_index,
                                                               paragraph_index, portion_index, constant.PASSWORD,
                                                               constant.FOLDER_NAME)
        self.assertEqual(1, len(response.items))

    def get_get_portion_rect(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        portion_index = 1
        response = BaseTest.slides_api.ge_portion_rectangle(constant.FILE_NAME, slide_index, shape_index,
                                                            paragraph_index, portion_index, constant.PASSWORD,
                                                            constant.FOLDER_NAME)
        self.assertIsNotNone(response)
        self.assertGreater(response.x, 0)
        self.assertGreater(response.y, 0)
        self.assertGreater(response.width, 0)
        self.assertGreater(response.height, 0)

    def test_get_portion_effective(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 2
        paragraph_index = 1
        portion_index = 1
        response = BaseTest.slides_api.get_portion_effective(constant.FILE_NAME, slide_index, shape_index, paragraph_index,
                                                   portion_index, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(18, response.font_height)

    def test_get_sub_shape_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        portion_index = 1
        shape_path = "3/shapes"
        response = BaseTest.slides_api.get_subshape_portion_effective(constant.FILE_NAME, slide_index, shape_path,
                                                                      shape_index, paragraph_index, portion_index,
                                                                      constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(18, response.font_height)