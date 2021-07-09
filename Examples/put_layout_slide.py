from slides_configuration import *

dto={"MasterSlide": { "Uri": { "Href": "masterSlides/2" } }}
response = slides_api.update_layout_slide("test.pptx", 1, dto)
print(response)