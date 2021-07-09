from slides_configuration import *

response = slides_api.get_placeholder("placeholders.pptx", 1, 1, password = "password")
print(response)