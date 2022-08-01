from __future__ import absolute_import

from test import constant
from asposeslidescloud import PresentationToMerge, OrderedMergeRequest, PresentationsMergeRequest
from test.base_test import BaseTest
import asposeslidescloud

class TestMerge(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_merge_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        file_name2 = "test-unprotected.pptx"
        file_name_pdf = "test.pdf"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.copy_file("TempTests/" + file_name2, folder_name + "/" + file_name2)
        BaseTest.slides_api.copy_file("TempTests/" + file_name_pdf, folder_name + "/" + file_name_pdf)
        request = PresentationsMergeRequest()
        request.presentation_paths = [ folder_name + "/" + file_name2, folder_name + "/" + file_name_pdf ]
        BaseTest.slides_api.merge(file_name, request, password, folder_name)

    def test_merge_ordered_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        file_name2 = "test-unprotected.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        BaseTest.slides_api.copy_file("TempTests/" + file_name2, folder_name + "/" + file_name2)
        request = OrderedMergeRequest()
        presentation = PresentationToMerge()
        presentation.path = folder_name + "/" + file_name2
        presentation.slides = [ 2, 1 ]
        request.presentations = [ presentation ]
        BaseTest.slides_api.ordered_merge(file_name, request, password, folder_name)

    def test_merge_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        BaseTest.slides_api.merge_online(files)

    def test_merge_and_save_request(self):
        out_path = "TestData/out.pptx"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        BaseTest.slides_api.merge_and_save_online(out_path, files)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_merge_ordered_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source1 = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        request = OrderedMergeRequest()
        presentation1 = PresentationToMerge()
        presentation1.path = "file1"
        presentation1.password = "password"
        presentation2 = PresentationToMerge()
        presentation2.path = "file2"
        presentation2.slides = [ 1, 2 ]
        request.presentations = [ presentation1, presentation2 ]
        BaseTest.slides_api.merge_online(files, request)

    def test_merge_ordered_combined(self):
        folder_name = "TempSlidesSDK"
        file_name2 = "test-unprotected.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name2, folder_name + "/" + file_name2)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        files = [ source ]
        request = OrderedMergeRequest()
        presentation1 = PresentationToMerge()
        presentation1.path = "file1"
        presentation1.password = "password"
        presentation2 = PresentationToMerge()
        presentation2.path = "test-unprotected.pptx"
        presentation2.slides = [ 1, 2 ]
        presentation2.source = 'Storage'
        presentation2.path = folder_name + "/" + file_name2
        request.presentations = [ presentation1, presentation2 ]
        BaseTest.slides_api.merge_online(files, request)

    def test_merge_ordered_url(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" +
                                      constant.FILE_NAME)
        request = OrderedMergeRequest()
        presentation1 = PresentationToMerge()
        presentation1.path = constant.FOLDER_NAME + "/" + constant.FILE_NAME
        presentation1.password = "password"
        presentation1.source = "Storage"
        presentation1.slides = [1, 2]
        presentation2 = PresentationToMerge()
        presentation2.path = "https://drive.google.com/uc?export=download&id=1ycMzd7e--Ro9H8eH2GL5fPP7-2HjX4My"
        presentation2.slides = [1]
        presentation2.source = 'Url'
        request.presentations = [presentation1, presentation2]
        BaseTest.slides_api.merge_online(None, request)
