from slides_configuration import *


request=GetLayoutSlidesListRequest("test.pptx")
response = layout_api.get_layout_slides_list(request)
print(response)