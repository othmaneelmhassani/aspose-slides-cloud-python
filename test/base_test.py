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
import re
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

    def initialize(self, function_name, invalid_parameter_name, invalid_parameter_value, invalid_parameter_type):
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
                    BaseTest.slides_api.upload_file("TempTests/" + file_name, file)
                BaseTest.slides_api.upload_file(BaseTest.expected_test_data_version, "TempTests/version.txt")
            BaseTest.is_initialized = True
        files = dict()
        for rule in self.get_rules(BaseTest.test_rules['Files'], function_name, invalid_parameter_name, invalid_parameter_type):
            actual_name = self.untemplatize(rule['File'], invalid_parameter_name, invalid_parameter_value)
            path = "TempSlidesSDK"
            if 'Folder' in rule:
                path = self.untemplatize(rule['Folder'], invalid_parameter_name, invalid_parameter_value)
            path = path + "/" + actual_name
            files[path] = rule
            rule['ActualName'] = actual_name
        for path, rule in files.items():
            if rule['Action'] == 'Put':
                BaseTest.slides_api.copy_file("TempTests/" + rule['ActualName'], path)
            elif rule['Action'] == 'Delete':
                BaseTest.slides_api.delete_file(path)

    def get_test_value(self, function_name, field_name, field_type):
        value = None
        for rule in self.get_rules(BaseTest.test_rules['Values'], function_name, field_name, field_type):
            if 'Value' in rule:
                value = rule['Value']
        if hasattr(models, field_type):
            class_type = getattr(models, field_type)
            if 'Type' in rule and hasattr(models, rule['Type']):
                class_type = getattr(models, rule['Type'])
            api_client = ApiClient(Configuration())
            return api_client.deserialize_model(value, class_type)
        return self.untemplatize(value, field_name, None)

    def get_invalid_test_value(self, function_name, field_name, field_value, field_type):
        invalid_value = None
        for rule in self.get_rules(BaseTest.test_rules['Values'], function_name, field_name, field_type):
            if 'InvalidValue' in rule:
                invalid_value = rule['InvalidValue']
        return self.untemplatize(invalid_value, field_name, field_value)

    def assert_exception(self, ex, function_name, field_name, field_value, field_type):
        code = 0
        message = "Unexpeceted message"
        for rule in self.get_rules(BaseTest.test_rules['Results'], function_name, field_name, field_type):
            if 'Code' in rule:
                code = rule['Code']
            if 'Message' in rule:
                message = rule['Message']
        self.assertEqual(code, ex.status)
        exbody = ex.body
        if not isinstance(exbody, str):
            exbody = ex.body.decode("utf-8")
        self.assertTrue(self.untemplatize(message, field_name, field_value) in exbody)

    def assert_value_error(self, ex, function_name, field_name, field_value, field_type):
        code = 0
        message = "Unexpeceted message"
        for rule in self.get_rules(BaseTest.test_rules['Results'], function_name, field_name, field_type):
            if 'Code' in rule:
                code = rule['Code']
            if 'Message' in rule:
                message = rule['Message']
        self.assertEqual(code, 400)
        self.assertTrue(self.untemplatize(message, field_name, field_value) in str(ex))

    def assert_no_exception(self, function_name, field_name, field_type):
        failed = True
        for rule in self.get_rules(BaseTest.test_rules['OKToNotFail'], function_name, field_name, field_type):
            failed = False
        if failed:
            self.fail("Must have failed")
    
    def get_rules(self, rules, function_name, field_name, field_type):
        filtered_rules = []
        if function_name:
            function_name = function_name.replace('_', '')
        if field_name:
            field_name = field_name.replace('_', '')
        for rule in rules:
            if self.applies(rule, function_name, field_name, field_type):
                filtered_rules.append(rule)
        return filtered_rules

    def applies(self, rule, function_name, field_name, field_type):
        return self.appliesValue(rule, 'Method', function_name) \
            and (not ('Invalid' in rule) or ((field_name != None) == rule['Invalid'])) \
            and self.appliesValue(rule, 'Parameter', field_name) \
            and self.appliesType(rule, field_type) \
            and (not ('Language' in rule) or rule['Language'].lower() == "python")

    def appliesValue(self, rule, key, value):
        if not (key in rule):
            return True
        rule_value = rule[key]
        if value == None:
            return False
        if rule_value.startswith("/") and rule_value.endswith("/"):
            return re.search(rule_value[1:-1], value, re.IGNORECASE)
        return rule_value.lower() == value.replace('_', '').lower()

    def appliesType(self, rule, field_type):
        if not ('Type' in rule):
            return True
        rule_type = rule['Type']
        if rule_type == 'bool':
            return field_type == 'bool'
        if rule_type == 'number':
            return field_type == 'int'
        if rule_type == 'int':
            return field_type == 'int'
        if rule_type == "int[]":
            return field_type == "list[int]"
        if rule_type == "stream":
            return field_type == "file"
        if rule_type == "stream[]":
            return field_type == "dict"
        if rule_type == "model":
            return hasattr(models, field_type)
        if hasattr(models, rule_type):
            if not hasattr(models, field_type):
                return False
            return issubclass(getattr(models, rule_type), getattr(models, field_type))
        return False

    def untemplatize(self, template, name, value):
        if template == None and value != None and isinstance(value, str):
            return value
        if template == None or not isinstance(template, str):
            return template
        template = self.replace_str(template, "%n", name)
        template = self.replace_str(template, "%v", value)
        if template.startswith('@'):
            template = template[1:]
            if template.startswith('(') and template.endswith(')'):
                files = []
                for file_name in template[1:-1].split(','):
                    with open(self.test_data_path + "/" + file_name, "rb") as bf:
                        files.append(bf.read())
                return files
            with open(self.test_data_path + "/" + template, "rb") as bf:
                return bf.read()
        return template

    def replace_str(self, template, pattern, value):
        if value == None:
            return template.replace(pattern, "")
        if not isinstance(value, str):
            return template.replace(pattern, str(value))
        return template.replace(pattern, value)