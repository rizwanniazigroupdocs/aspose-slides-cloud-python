from slides_configuration import *


request=PutSlidesSlideSizeRequest("test.pptx", width="100", height="100", size_type="OnScreen", scale_type="DoNotScale")
response = slides_api.put_slides_slide_size(request)
print(response)