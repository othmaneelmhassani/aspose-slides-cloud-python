from slides_configuration import *

response = slides_api.get_placeholders("placeholders.pptx", 1, password="password")
print(response)