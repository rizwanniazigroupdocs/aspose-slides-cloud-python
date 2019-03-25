import asposeslidescloud
from asposeslidescloud.rest import ApiException
from asposeslidescloud.models.requests import GetSlidesDocumentRequest
from slides_configuration import *

slides_request=GetSlidesDocumentRequest("test.pptx")
response =slides_api.get_slides_document(slides_request)

print(response)