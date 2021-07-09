from slides_configuration import *

response = slides_api.get_document_property("test.pptx", "author")
print(response)