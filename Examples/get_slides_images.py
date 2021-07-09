from slides_configuration import *

response = slides_api.get_presentation_images("test.pptx")
print(response)