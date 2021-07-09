from slides_configuration import *

response = slides_api.get_slide_images("test.pptx", 1)
print(response)