from slides_configuration import *

response = slides_api.get_layout_slides("test.pptx")
print(response)