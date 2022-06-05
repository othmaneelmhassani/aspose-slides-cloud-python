from __future__ import absolute_import

from asposeslidescloud import ExportFormat, Pipeline, Save, OutputFile, Input, RequestInputFile
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestPipeline(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_pipeline(self):
        file1 = RequestInputFile()
        file1.type = "Request"
        file1.index = 0

        file2 = RequestInputFile()
        file2.type = "Request"
        file2.index = 1

        input = Input()
        input.templateData = file1
        input.template = file2

        output = OutputFile("Response")
        output.type = "Response"

        task = Save()
        task.format = ExportFormat.PPTX
        task.output = output
        task.type = "Save"

        pipeline = Pipeline()
        pipeline.input = input
        pipeline.tasks = [task]

        files = {}
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/TemplatingCVDataWithBase64.xml", 'rb') as f:
            files["file1"] = ("TemplatingCVDataWithBase64.xml", f.read())

        with open(constant.LOCAL_TEST_DATA_FOLDER + "/TemplateCV.pptx", 'rb') as f:
            files["file2"] = ("TemplateCV.pptx", f.read())

        result = self.api.pipeline(pipeline, files)
        self.assertTrue(isinstance(result, str))
        self.assertTrue(len(result) > 0)