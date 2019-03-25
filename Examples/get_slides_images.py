from slides_configuration import *

request=GetSlidesImagesRequest("test.pptx")
response = images_api.get_slides_images(request)
print(response)