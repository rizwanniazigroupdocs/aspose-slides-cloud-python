from slides_configuration import *

request=GetLayoutSlideRequest("test.pptx", slide_index=1)
response = layout_api.get_layout_slide(request)

print(response)