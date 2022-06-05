from __future__ import absolute_import

import os

from asposeslidescloud import TextElement, FunctionElement, BlockElement, MathParagraph, Portion, LimitElement, \
    FractionElement
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest
import asposeslidescloud

class TestMath(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_math_get(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        portion = BaseTest.slides_api.get_portion(file_name, 2, 3, 1, 1, "password", folder_name)
        self.assertIsNotNone(portion.math_paragraph)
        self.assertIsNotNone(portion.math_paragraph.math_block_list)
        self.assertEqual(1, len(portion.math_paragraph.math_block_list))
        self.assertIsNotNone(portion.math_paragraph.math_block_list[0].math_element_list)
        self.assertEqual(3, len(portion.math_paragraph.math_block_list[0].math_element_list))
        self.assertTrue(isinstance(portion.math_paragraph.math_block_list[0].math_element_list[2], FractionElement))

    def test_math_get_null(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        portion = BaseTest.slides_api.get_portion(file_name, 2, 1, 1, 1, "password", folder_name)
        self.assertIsNone(portion.math_paragraph)

    def test_math_create(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = Portion()
        math_paragraph = MathParagraph()
        math_block = BlockElement()
        function_element = FunctionElement()
        limit_element = LimitElement()
        text1 = TextElement()
        text1.value = "lim"
        limit_element.base = text1
        text2 = TextElement()
        text2.value = "x->0"
        limit_element.limit = text2
        function_element.name = limit_element
        fraction_element = FractionElement()
        sinus_element = FunctionElement()
        text3 = TextElement()
        text3.value = "sin"
        sinus_element.name = text3
        text4 = TextElement()
        text4.value = "x"
        sinus_element.name = text4
        fraction_element.numerator = sinus_element
        text5 = TextElement()
        text5.value = "x"
        fraction_element.denominator = text5
        function_element.base = fraction_element
        math_block.math_element_list = [ function_element ]
        math_paragraph.math_block_list = [ math_block ]
        dto.math_paragraph = math_paragraph
        portion = BaseTest.slides_api.create_portion(file_name, 1, 1, 1, dto, None, "password", folder_name)
        self.assertIsNotNone(portion.math_paragraph)
        self.assertIsNotNone(portion.math_paragraph.math_block_list)
        self.assertEqual(1, len(portion.math_paragraph.math_block_list))
        self.assertIsNotNone(portion.math_paragraph.math_block_list[0].math_element_list)
        self.assertEqual(1, len(portion.math_paragraph.math_block_list[0].math_element_list))
        self.assertTrue(isinstance(portion.math_paragraph.math_block_list[0].math_element_list[0], FunctionElement))

    def test_math_update(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = Portion()
        math_paragraph = MathParagraph()
        math_block = BlockElement()
        function_element = FunctionElement()
        limit_element = LimitElement()
        text1 = TextElement()
        text1.value = "lim"
        limit_element.base = text1
        text2 = TextElement()
        text2.value = "x->0"
        limit_element.limit = text2
        function_element.name = limit_element
        fraction_element = FractionElement()
        sinus_element = FunctionElement()
        text3 = TextElement()
        text3.value = "sin"
        sinus_element.name = text3
        text4 = TextElement()
        text4.value = "x"
        sinus_element.name = text4
        fraction_element.numerator = sinus_element
        text5 = TextElement()
        text5.value = "x"
        fraction_element.denominator = text5
        function_element.base = fraction_element
        math_block.math_element_list = [ function_element ]
        math_paragraph.math_block_list = [ math_block ]
        dto.math_paragraph = math_paragraph
        portion = BaseTest.slides_api.update_portion(file_name, 2, 3, 1, 1, dto, "password", folder_name)
        self.assertIsNotNone(portion.math_paragraph)
        self.assertIsNotNone(portion.math_paragraph.math_block_list)
        self.assertEqual(1, len(portion.math_paragraph.math_block_list))
        self.assertIsNotNone(portion.math_paragraph.math_block_list[0].math_element_list)
        self.assertEqual(1, len(portion.math_paragraph.math_block_list[0].math_element_list))
        self.assertTrue(isinstance(portion.math_paragraph.math_block_list[0].math_element_list[0], FunctionElement))

    def test_math_download(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        mathMl = BaseTest.slides_api.download_portion_as_math_ml(file_name, 2, 3, 1, 1, "password", folder_name)
        self.assertGreater(os.path.getsize(mathMl), 0)

    def test_math_download_null(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        try:
            BaseTest.slides_api.download_portion_as_math_ml(file_name, 2, 1, 1, 1, "password", folder_name)
            self.fail("Must have failed because conversion to MathML works only for math portions")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_math_save(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        out_path = folder_name + "/mathml.xml"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.save_portion_as_math_ml(file_name, 2, 3, 1, 1, out_path, "password", folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)