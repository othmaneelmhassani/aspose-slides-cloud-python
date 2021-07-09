from slides_configuration import *

response = slides_api.replace_presentation_text("test.pptx", old_value="hello", new_value="world", ignore_case="true")
print(response)