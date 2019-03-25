from slides_configuration import *

prop={ "Name": "auhor", "Value": "mateen" }
request=PutSlidesSetDocumentPropertyRequest("test.pptx", property_name="author", _property=prop)

response = properties_api.put_slides_set_document_property(request)
print(response)