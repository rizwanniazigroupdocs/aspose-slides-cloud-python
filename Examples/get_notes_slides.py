from slides_configuration import *

request=GetNotesSlideRequest("test.pptx", slide_index=2)
response = notes_slides.get_notes_slide(request)
print(response)