from slides_configuration import *

response = slides_api.get_layout_slide("test.pptx", 1)

print(response)