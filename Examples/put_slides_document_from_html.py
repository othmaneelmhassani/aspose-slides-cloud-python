from slides_configuration import *

response = slides_api.import_from_html("test.pptx", "test.html")
print(response)