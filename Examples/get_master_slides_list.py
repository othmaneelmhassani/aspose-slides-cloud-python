from slides_configuration import *

response = slides_api.get_master_slides("test.pptx")
print(response)