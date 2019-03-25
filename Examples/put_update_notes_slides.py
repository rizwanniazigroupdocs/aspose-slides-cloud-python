from slides_configuration import *


dto_obj={ "Text": "testNote" }
request=PutUpdateNotesSlideRequest("test.pptx", slide_index=1, dto=dto_obj)
response = notes_slides.put_update_notes_slide(request)
print(response)