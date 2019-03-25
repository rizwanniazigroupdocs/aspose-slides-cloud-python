from slides_configuration import *


request=PostCopyLayoutSlideFromSourcePresentationRequest("test.pptx", "test.pptx", clone_from_position=1)
response = layout_api.post_copy_layout_slide_from_source_presentation(request)
print(response)