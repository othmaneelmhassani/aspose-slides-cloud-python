from slides_configuration import *

response = slides_api.download_image("test.pptx", 1, "PNG")
print("The image was saved to " + response)
