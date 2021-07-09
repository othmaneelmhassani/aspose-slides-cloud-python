from slides_configuration import *

response = slides_api.delete_notes_slide("test.pptx", 1)
print(response)