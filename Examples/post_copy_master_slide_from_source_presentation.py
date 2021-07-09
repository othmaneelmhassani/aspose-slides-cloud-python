from slides_configuration import *

response = slides_api.copy_master_slide("test.pptx", "test.pptx", 1)
print(response)