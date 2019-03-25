from slides_configuration import *


request=GetSlidesPresentationTextItemsRequest("test.pptx")

response = text_api.get_slides_presentation_text_items(request)
print(response)