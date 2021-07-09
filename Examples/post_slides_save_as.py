from slides_configuration import *

response =slides_api.download_presentation("test.pptx", "pdf")
print("The presentation was saved to " + response)
