
from __future__ import absolute_import

import os

from asposeslidescloud import ProtectionProperties, SlideProperties, DocumentProperty, DocumentProperties, \
    ViewProperties, CommonSlideViewProperties
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestProperties(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_property_builtin(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        property_name = "Author"
        updated_property_value = "New Value"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.get_document_property(file_name, property_name, password, folder_name)
        self.assertEqual(property_name, result.name)
        self.assertTrue(result.built_in)
        property = DocumentProperty()
        property.value = updated_property_value
        result = BaseTest.slides_api.set_document_property(file_name, property_name, property, password, folder_name)
        self.assertEqual(property_name, result.name)
        self.assertEqual(updated_property_value, result.value)
        self.assertTrue(result.built_in)
        BaseTest.slides_api.delete_document_property(file_name, property_name, password, folder_name)
        result = BaseTest.slides_api.get_document_property(file_name, property_name, password, folder_name)
        # built-in property is not actually deleted
        self.assertEqual(property_name, result.name)
        self.assertNotEqual(updated_property_value, result.value)
        self.assertTrue(result.built_in)

    def test_property_custom(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        property_name = "CustomProperty2"
        updated_property_value = "New Value"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        property = DocumentProperty()
        property.value = updated_property_value
        result = BaseTest.slides_api.set_document_property(file_name, property_name, property, password, folder_name)
        self.assertEqual(property_name, result.name)
        self.assertEqual(updated_property_value, result.value)
        self.assertFalse(result.built_in)
        BaseTest.slides_api.delete_document_property(file_name, property_name, password, folder_name)
        try:
            BaseTest.slides_api.get_document_property(file_name, property_name, password, folder_name)
            self.fail("The property must have been deleted")
        except ApiException as ex:
            self.assertEqual(404, ex.status)

    def test_property_bulk_update(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        property_name = "Author"
        custom_property_name = "CustomProperty2"
        updated_property_value = "New Value"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.get_document_properties(file_name, password, folder_name)
        count = len(result.list)
        property1 = DocumentProperty()
        property1.name = property_name
        property1.value = updated_property_value
        property2 = DocumentProperty()
        property2.name = custom_property_name
        property2.value = updated_property_value
        properties = DocumentProperties()
        properties.list = [property1, property2]
        result = BaseTest.slides_api.set_document_properties(file_name, properties, password, folder_name)
        self.assertEqual(count + 1, len(result.list))
        result = BaseTest.slides_api.delete_document_properties(file_name, password, folder_name)
        self.assertEqual(count - 1, len(result.list))

    def test_property_slide_properties(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        get_result = BaseTest.slides_api.get_slide_properties(file_name, password, folder_name)
        dto = SlideProperties()
        dto.first_slide_number = get_result.first_slide_number + 2
        put_result = BaseTest.slides_api.set_slide_properties(file_name, dto, password, folder_name)
        self.assertEqual(get_result.orientation, put_result.orientation)
        self.assertNotEqual(get_result.first_slide_number, put_result.first_slide_number)

    def test_property_slide_size_preset(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = SlideProperties()
        dto.size_type = 'B4IsoPaper'
        result = BaseTest.slides_api.set_slide_properties(file_name, dto, password, folder_name)
        self.assertEqual('B4IsoPaper', result.size_type)
        self.assertEqual(852, result.width)
        self.assertEqual(639, result.height)

    def test_property_slide_size_custom(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        width = 800
        height = 500
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        dto = SlideProperties()
        dto.width = width
        dto.height = height
        result = BaseTest.slides_api.set_slide_properties(file_name, dto, password, folder_name)
        self.assertEqual('Custom', result.size_type)
        self.assertEqual(width, result.width)
        self.assertEqual(height, result.height)

    def test_property_protection(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        get_result = BaseTest.slides_api.get_protection_properties(file_name, password, folder_name)
        dto = ProtectionProperties()
        dto.read_only_recommended = not get_result.read_only_recommended
        put_result = BaseTest.slides_api.set_protection(file_name, dto, password, folder_name)
        self.assertEqual(get_result.encrypt_document_properties, put_result.encrypt_document_properties)
        self.assertNotEqual(get_result.read_only_recommended, put_result.read_only_recommended)

    def test_property_protection_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_protection(file_name, password, folder_name)
        self.assertFalse(result.is_encrypted)
        self.assertFalse(result.read_only_recommended)
        self.assertFalse(result.read_password)

    def test_property_protection_online(self):
        dto = ProtectionProperties()
        dto.read_password = "newPassword"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.set_protection_online(source, dto, "password")
        self.assertTrue(os.path.getsize(result) > 0)

    def test_property_protection_unprotect_online(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.delete_protection_online(source, "password")
        self.assertNotEqual(len(source), os.path.getsize(result))

    def test_get_view_properties(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        response = BaseTest.slides_api.get_view_properties(constant.FILE_NAME, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual("True", response.show_comments)

    def test_set_view_properties(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        dto = ViewProperties()
        dto.show_comments = "False"
        dto.slide_view_properties = CommonSlideViewProperties()
        dto.slide_view_properties.scale = 50
        response = BaseTest.slides_api.set_view_properties(constant.FILE_NAME, dto, constant.PASSWORD,
                                                           constant.FOLDER_NAME)
        self.assertEqual("False", response.show_comments)
        self.assertEqual(50, response.slide_view_properties.scale)

    def test_protection_check(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        protection_properties = BaseTest.slides_api.get_protection_properties(file_name, None, folder_name)
        self.assertEqual(True, protection_properties.is_encrypted)
        self.assertEqual(None, protection_properties.read_password)

        protection_properties = BaseTest.slides_api.get_protection_properties(file_name, password, folder_name)
        self.assertEqual(True, protection_properties.is_encrypted)
        self.assertNotEqual(None, protection_properties.read_password)
