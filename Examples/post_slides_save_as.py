from slides_configuration import *


request=PostSlidesSaveAsRequest("test.pptx", "pdf")
response =slides_api.post_slides_save_as(request)
print(response)
