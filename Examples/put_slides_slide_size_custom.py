from slides_configuration import *
from asposeslidescloud.models.slide_properties import SlideProperties

slide_properties = SlideProperties()
slide_properties.width = 100
slide_properties.height = 100

response = slides_api.set_slide_properties("test.pptx", slide_properties)
print(response)