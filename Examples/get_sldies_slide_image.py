from slides_configuration import *


request=GetSlidesSlideImagesRequest("test.pptx", 1)

response = images_api.get_slides_slide_images(request)
print(response)