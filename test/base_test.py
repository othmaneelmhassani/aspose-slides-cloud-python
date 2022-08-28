# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

from __future__ import absolute_import

import json
import os
import unittest
import asposeslidescloud
from asposeslidescloud import models
from asposeslidescloud.api_client import ApiClient
from asposeslidescloud.apis.slides_api import SlidesApi
from asposeslidescloud.configuration import Configuration
from asposeslidescloud.rest import ApiException

class BaseTest(unittest.TestCase):

    __test__ = False
    
    is_initialized = False
    configuration = None
    slides_api = None
    expected_test_data_version = '1'
    
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)

        self.test_data_path = "TestData"
        self.folder_name = "TempSlidesSDK"
        self.changed_file_name = "changedtest.pptx"
        self.file_name = "test.pptx"
        self.file_password = "password"

        if not BaseTest.slides_api:
            with open('testConfig.json') as f:
                config = json.loads(f.read())
            BaseTest.configuration = Configuration()
            BaseTest.configuration.app_sid = config['ClientId']
            BaseTest.configuration.app_key = config['ClientSecret']
            BaseTest.configuration.base_url = config['BaseUrl']
            BaseTest.configuration.auth_base_url = config['BaseUrl']
            if 'AuthBaseUrl' in config:
                BaseTest.configuration.auth_base_url = config['AuthBaseUrl']
            BaseTest.configuration.debug = config['Debug']

            with open('testRules.json') as f:
                BaseTest.test_rules = json.loads(f.read())

            BaseTest.slides_api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def initialize(self, function_name, invalid_parameter_name, invalid_parameter_value):
        if not BaseTest.is_initialized:
            version = ''
            try:
                version_path = BaseTest.slides_api.download_file("TempTests/version.txt")
                with open(version_path) as version_file:
                    version = version_file.read()
            except ApiException:
                pass #just try to reupload the files if smth went wrong
            if version != BaseTest.expected_test_data_version:
                for file_name in os.listdir('TestData'):
                    with open(os.path.join('TestData', file_name), 'rb') as f:
                        file = f.read()
                    BaseTest.slides_api.upload_file(file, "TempTests/" + file_name)
                BaseTest.slides_api.upload_file(BaseTest.expected_test_data_version, "TempTests/version.txt")
            BaseTest.is_initialized = True
        files = dict()
        for rule in self.get_rules(BaseTest.test_rules['Files'], function_name, invalid_parameter_name):
            actual_name = self.untemplatize(rule['File'], invalid_parameter_value)
            path = "TempSlidesSDK"
            if 'Folder' in rule:
                path = self.untemplatize(rule['Folder'], invalid_parameter_value)
            path = path + "/" + actual_name
            files[path] = rule
            rule['ActualName'] = actual_name
        for path, rule in files.items():
            if rule['Action'] == 'Put':
                BaseTest.slides_api.copy_file("TempTests/" + rule['ActualName'], path)
            elif rule['Action'] == 'Delete':
                BaseTest.slides_api.delete_file(path)

    def get_test_value(self, function_name, field_name, field_type):
        if field_type == 'Stream' or field_type == 'file':
            bin_file_name = self.file_name
            if function_name == 'import_from_pdf':
                bin_file_name = 'test.pdf'
            elif field_name == 'image':
                if function_name == 'import_shapes_from_svg':
                    bin_file_name = 'shapes.svg'
                else:
                    bin_file_name = 'watermark.png'
            with open(self.test_data_path + "/" + bin_file_name, "rb") as bf:
                return bf.read()
        if field_type == 'dict' and field_name == 'files':
            files = {}
            with open("TestData/test.pptx", 'rb') as f:
                files["file1"] = ("test.pptx", f.read())
            with open("TestData/test-unprotected.pptx", 'rb') as f:
                files["file2"] = ("test-unprotected.pptx", f.read())
            return files
        value = "test" + field_name
        for rule in self.get_rules(BaseTest.test_rules['Values'], function_name, field_name):
            if 'Value' in rule:
                rule_value = rule['Value']
                if 'Type' in rule:
                    rule_class = getattr(models, rule['Type'])
                    field_class = getattr(models, field_type)
                    if rule_class and field_class and issubclass(rule_class, field_class):
                        api_client = ApiClient(Configuration())
                        value = api_client.deserialize_model(rule_value, rule['Type'])
                else:
                    value = rule_value
        return value

    def get_invalid_test_value(self, function_name, field_name, field_value, field_type):
        if field_type == 'Stream' or field_type == 'file':
            return None
        invalid_value = None
        for rule in self.get_rules(BaseTest.test_rules['Values'], function_name, field_name):
            if 'InvalidValue' in rule:
                invalid_value = rule['InvalidValue']
        return self.untemplatize(invalid_value, field_value)

    def assert_exception(self, ex, function_name, field_name, field_value):
        code = 0
        message = "Unexpeceted message"
        for rule in self.get_rules(BaseTest.test_rules['Results'], function_name, field_name):
            if 'Code' in rule:
                code = rule['Code']
            if 'Message' in rule:
                message = rule['Message']
        self.assertEqual(code, ex.status)
        exbody = ex.body
        if not isinstance(exbody, str):
            exbody = ex.body.decode("utf-8")
        self.assertTrue(self.untemplatize(message, field_value) in exbody)

    def assert_value_error(self, ex, function_name, field_name, field_value):
        code = 0
        message = "Unexpeceted message"
        for rule in self.get_rules(BaseTest.test_rules['Results'], function_name, field_name):
            if 'Code' in rule:
                code = rule['Code']
            if 'Message' in rule:
                message = rule['Message']
        self.assertEqual(code, 400)
        self.assertTrue(self.untemplatize(message, field_value) in str(ex))

    def assert_no_exception(self, function_name, field_name):
        failed = True
        for rule in self.get_rules(BaseTest.test_rules['OKToNotFail'], function_name, field_name):
            failed = False
        if failed:
            self.fail("Must have failed")
    
    def get_rules(self, rules, function_name, field_name):
        filtered_rules = []
        for rule in rules:
            if self.applies(rule, function_name, field_name):
                filtered_rules.append(rule)
        return filtered_rules

    def applies(self, rule, function_name, field_name):
        return (not ('Method' in rule) \
                or (function_name != None and rule['Method'].lower() == function_name.replace('_', '').lower())) \
            and (not ('Invalid' in rule) or ((field_name != None) == rule['Invalid'])) \
            and (not ('Parameter' in rule) or (field_name != None and rule['Parameter'].lower() == field_name.replace('_', '').lower())) \
            and (not ('Language' in rule) or rule['Language'].lower() == "python")

    def untemplatize(self, template, value):
        if template == None and value != None and isinstance(value, str):
            return value
        if template != None and isinstance(template, str):
            if value == None:
                return template.replace("%v", "")
            elif not isinstance(value, str):
                return template.replace("%v", str(value))
            else:
                return template.replace("%v", value)
        return template