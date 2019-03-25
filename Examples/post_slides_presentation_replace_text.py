from slides_configuration import *

request=PostSlidesPresentationReplaceTextRequest("test.pptx", old_value="hello", new_value="world", ignore_case="true")
response = text_api.post_slides_presentation_replace_text(request)
print(response)