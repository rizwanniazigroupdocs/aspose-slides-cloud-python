from slides_configuration import *

request=GetSlidesDocumentWithFormatRequest("test.pptx", "JPEG")
response = slides_api.get_slides_document_with_format(request)

print (response)