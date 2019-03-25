from slides_configuration import *


request=DeleteSlidesDocumentPropertyRequest("test.pptx", property_name="author")
response = properties_api.delete_slides_document_property(request)
print(response)