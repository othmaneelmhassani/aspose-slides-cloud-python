from slides_configuration import *

dto_obj = { "Text": "testNote" }
response = slides_api.update_notes_slide("test.pptx", 1, dto_obj)
print(response)