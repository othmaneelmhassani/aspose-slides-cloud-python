from slides_configuration import *

response = slides_api.get_master_slide("test.pptx", 1)
print(response)
