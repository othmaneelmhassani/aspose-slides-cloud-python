from slides_configuration import *

prop = { "Name": "auhor", "Value": "mateen" }
response = slides_api.set_document_property("test.pptx", "author", prop)
print(response)