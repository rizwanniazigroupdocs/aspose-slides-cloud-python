from slides_configuration import *


request=DeleteSlidesDocumentPropertiesRequest("test.pptx")
response = properties_api.delete_slides_document_properties(request)
print(response)