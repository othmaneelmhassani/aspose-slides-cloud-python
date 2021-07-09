from slides_configuration import *

response = slides_api.get_presentation_text_items("test.pptx")

if response and response.items:
    for item in response.items:
        print("Text item: " + item.text)
        print("Shape uri: " + item.uri.href)
        print()
