from slides_configuration import *

request=DeleteNotesSlideRequest("test.pptx", slide_index=3)
response = notes_slides.delete_notes_slide(request)
print(response)