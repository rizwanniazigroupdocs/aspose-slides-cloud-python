from slides_configuration import *

request=PostCopyMasterSlideFromSourcePresentationRequest("test.pptx", "test.pptx", clone_from_position=1)
response = master_api.post_copy_master_slide_from_source_presentation(request)

print(response)