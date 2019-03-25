from slides_configuration import *

request=PostSlidesDocumentRequest("test.pptx", "Hello World", "")
response = slides_api.get_slides_document_with_format(request)

print (response)