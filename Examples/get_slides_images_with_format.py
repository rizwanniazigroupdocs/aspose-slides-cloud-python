from slides_configuration import *


request=GetSlidesImageWithFormatRequest("test.pptx", index=1, format="PNG")

response =images_api.get_slides_image_with_format(request)
print(response)
