from __future__ import absolute_import

from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestCreate(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_create_empty(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.delete_file(folder_name + "/" + file_name)
        BaseTest.slides_api.create_presentation(file_name, None, None, None, folder_name)

    def test_create_from_request(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.delete_file(folder_name + "/" + file_name)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + file_name, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.create_presentation(file_name, source, "password", None, folder_name)

    def test_create_from_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        new_file_name = "test2.pptx"
        BaseTest.slides_api.delete_file(folder_name + "/" + new_file_name)
        source_path = folder_name + "/" + file_name
        BaseTest.slides_api.copy_file("TempTests/" + file_name, source_path)
        BaseTest.slides_api.create_presentation_from_source(new_file_name, source_path, "password", None, None, folder_name)

    def test_create_from_template(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        template_file_name = "TemplateCV.pptx"
        BaseTest.slides_api.delete_file(folder_name + "/" + file_name)
        template_path = folder_name + "/" + template_file_name
        BaseTest.slides_api.copy_file("TempTests/" + template_file_name, template_path)
        data = "<staff><person><name>John Doe</name><address><line1>10 Downing Street</line1><line2>London</line2></address><phone>+457 123456</phone><bio>Hi, I'm John and this is my CV</bio><skills><skill><title>C#</title><level>Excellent</level></skill><skill><title>C++</title><level>Good</level></skill><skill><title>Java</title><level>Average</level></skill></skills></person></staff>"
        BaseTest.slides_api.create_presentation_from_template(file_name, template_path, data, None, None, None, None, folder_name)

    def test_create_from_html(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.delete_file(folder_name + "/" + file_name)
        BaseTest.slides_api.import_from_html(file_name, "<html><body>New Content</body></html>", None, folder_name)

    def test_append_from_html(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        slideCount = len(BaseTest.slides_api.get_slides(file_name, password, folder_name).slide_list)
        BaseTest.slides_api.import_from_html(file_name, "<html><body>New Content</body></html>", password, folder_name)
        newSlideCount = len(BaseTest.slides_api.get_slides(file_name, password, folder_name).slide_list)
        self.assertEqual(slideCount + 1, newSlideCount)

    def test_create_from_pdf(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.delete_file(folder_name + "/" + file_name)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test.pdf", 'rb') as f:
            source = f.read()
        BaseTest.slides_api.import_from_pdf(file_name, source, None, folder_name)

    def test_append_from_pdf(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        slideCount = len(BaseTest.slides_api.get_slides(file_name, password, folder_name).slide_list)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test.pdf", 'rb') as f:
            source = f.read()
        BaseTest.slides_api.import_from_pdf(file_name, source, password, folder_name)
        newSlideCount = len(BaseTest.slides_api.get_slides(file_name, password, folder_name).slide_list)
        self.assertEqual(slideCount + 4, newSlideCount)