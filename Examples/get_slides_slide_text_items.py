from slides_configuration import *


request=GetSlidesSlideTextItemsRequest("test.pptx", slide_index=1)
response = text_api.get_slides_slide_text_items(request)
print(response)