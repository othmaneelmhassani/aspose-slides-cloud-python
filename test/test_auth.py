from __future__ import absolute_import

from asposeslidescloud import Configuration
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest
import asposeslidescloud

class TestAuth(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_good_auth(self):
        config = Configuration()
        config.app_sid = self.configuration.app_sid
        config.app_key = self.configuration.app_key
        config.base_url = self.configuration.base_url
        config.auth_base_url = self.configuration.auth_base_url
        config.debug = self.configuration.debug
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()

    def test_bad_auth(self):
        config = Configuration()
        config.app_sid = "invalid"
        config.app_key = self.configuration.app_key
        config.base_url = self.configuration.base_url
        config.auth_base_url = self.configuration.auth_base_url
        config.debug = self.configuration.debug
        try:
            api = asposeslidescloud.apis.slides_api.SlidesApi(config)
            api.get_api_info()
            self.fail("Must have failed")
        except ApiException as ex:
            self.assertEqual(401, ex.status)

    def test_good_token(self):
        config = Configuration()
        config.app_sid = self.configuration.app_sid
        config.app_key = self.configuration.app_key
        config.base_url = self.configuration.base_url
        config.auth_base_url = self.configuration.auth_base_url
        config.debug = self.configuration.debug
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()
        config.app_sid = "invalid"
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()

    def test_bad_token(self):
        config = Configuration()
        config.app_sid = self.configuration.app_sid
        config.app_key = self.configuration.app_key
        config.base_url = self.configuration.base_url
        config.auth_base_url = self.configuration.auth_base_url
        config.debug = self.configuration.debug
        config.access_token = "invalid"
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()