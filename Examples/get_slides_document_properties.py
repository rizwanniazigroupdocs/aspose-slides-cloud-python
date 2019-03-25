from slides_configuration import *


request=GetSlidesDocumentPropertiesRequest("test.pptx")
response = properties_api.get_slides_document_properties(request)
print(response)