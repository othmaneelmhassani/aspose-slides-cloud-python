from slides_configuration import *

response = slides_api.download_notes_slide("test.pptx", 1, "PNG")
print("The notes slide was saved to " + response)