from __future__ import absolute_import

from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestTimeout(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_timeout(self):
        return # unstable test
        self.initialize('post_slide_save_as', None, None)
        config = Configuration()
        config.app_sid = self.configuration.app_sid
        config.app_key = self.configuration.app_key
        config.base_url = self.configuration.base_url
        config.auth_base_url = self.configuration.auth_base_url
        config.debug = self.configuration.debug
        config.timeout = 1
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)  # noqa: E501
        result = api.download_slide("test.pptx", 1, "svg", None, None, None, "password", "TempSlidesSDK")
