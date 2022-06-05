from __future__ import absolute_import

from zipfile import ZipFile

from asposeslidescloud import PdfExportOptions
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestSplit(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_split_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result1 = BaseTest.slides_api.split(file_name, None, None, None, None, None, None, None, password, folder_name)
        result2 = BaseTest.slides_api.split(file_name, None, None, None, None, 2, 3, None, password, folder_name)
        self.assertEqual(2, len(result2.slides))
        self.assertGreater(len(result1.slides), len(result2.slides))
        url = result1.slides[0].href
        path = url[url.index("/storage/file/") + len("/storage/file/"):]
        self.assertTrue(BaseTest.slides_api.object_exists(path).exists)

    def test_split_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        password = constant.PASSWORD
        result1 = BaseTest.slides_api.split_online(source, 'png', None, None, None, None, password)
        result2 = BaseTest.slides_api.split_online(source, 'png', None, None, 2, 3, password)
        with ZipFile(result1) as zip1:
            with ZipFile(result2) as zip2:
                self.assertEqual(2, len(zip2.namelist()))
                self.assertGreater(len(zip1.namelist()), len(zip2.namelist()))

    def test_split_request_to_storage(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        password = constant.PASSWORD
        result1 = BaseTest.slides_api.split_and_save_online(source, 'png', None, None, None, None, None, password)
        result2 = BaseTest.slides_api.split_and_save_online(source, 'png', None, None, None, 2, 3, password)
        self.assertEqual(2, len(result2.slides))
        self.assertGreater(len(result1.slides), len(result2.slides))
        url = result1.slides[0].href
        path = url[url.index("/storage/file/") + len("/storage/file/"):]
        self.assertTrue(BaseTest.slides_api.object_exists(path).exists)

    def test_split_with_options(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        options = PdfExportOptions()
        options.jpeg_quality = 50
        result = BaseTest.slides_api.split(file_name, options, None, None, None, None, None, None, password, folder_name)
        url = result.slides[0].href
        path = url[url.index("/storage/file/") + len("/storage/file/"):]
        self.assertTrue(BaseTest.slides_api.object_exists(path).exists)