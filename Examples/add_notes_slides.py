from slides_configuration import *

dto_obj={ "Text": "testNote" }
request=PostAddNotesSlideRequest("test.pptx", slide_index=1, dto=dto_obj)
response = notes_slides.post_add_notes_slide(request)
print(response)