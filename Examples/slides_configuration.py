from asposeslidescloud.configuration import Configuration
from asposeslidescloud.apis.slides_api import SlidesApi

configuration = Configuration()
configuration.app_sid = "MyClientId"
configuration.app_key ="MyClientSecret"

slides_api = SlidesApi(configuration) 
