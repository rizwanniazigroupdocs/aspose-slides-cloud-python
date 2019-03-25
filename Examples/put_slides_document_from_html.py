from slides_configuration import *


request= PutSlidesDocumentFromHtmlRequest("test.pptx", "test.html")
response = slides_api.put_slides_document_from_html(request)


print(response)