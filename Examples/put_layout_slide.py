from slides_configuration import *

dto={"MasterSlide": { "Uri": { "Href": "masterSlides/2" } }}



request=PutLayoutSlideRequest("test.pptx", slide_index=1, slide_dto=dto)

response = layout_api.put_layout_slide(request)
print(response)