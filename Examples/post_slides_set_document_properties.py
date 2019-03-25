from slides_configuration import *

request=PostSlidesSetDocumentPropertiesRequest("test.pptx")

response = properties_api.post_slides_set_document_properties(request)
print(response)