from slides_configuration import *


request=GetSlidesDocumentPropertyRequest("test.pptx", property_name="author")

response =properties_api.get_slides_document_property(request)
print(response)