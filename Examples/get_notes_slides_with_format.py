from slides_configuration import *


request=GetNotesSlideWithFormatRequest("test.pptx", slide_index=1, format="PNG")
response = notes_slides.get_notes_slide_with_format(request)
print(response)