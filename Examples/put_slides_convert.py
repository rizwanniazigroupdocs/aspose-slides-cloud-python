from slides_configuration import *


request=PutSlidesConvertRequest("PDF")

response = slides_api.put_slides_convert(request)
print(response)