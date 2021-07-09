from slides_configuration import *

response = slides_api.get_notes_slide("test.pptx", 2)
print(response)