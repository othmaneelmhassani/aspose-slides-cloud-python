from slides_configuration import *

response = slides_api.copy_layout_slide("test.pptx", "test.pptx", 1)
print(response)