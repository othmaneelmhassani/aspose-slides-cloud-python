from slides_configuration import *
from asposeslidescloud.models.document_properties import DocumentProperties
from asposeslidescloud.models.document_property import DocumentProperty

property1 = DocumentProperty()
property1.name = "author"
property1.value = "Agatha Christie"

property2 = DocumentProperty()
property2.name = "title"
property2.value = "Murder on the Orient Express"

properties = DocumentProperties()
properties.list = [ property1, property2 ]

response = slides_api.set_document_properties("test.pptx", properties)
print(response)