from slides_configuration import *

request=GetSlidesPlaceholderRequest("placeholders.pptx", slide_index=1, placeholder_index=1,password="password")
response = placeholder_api.get_slides_placeholder(request)
print(response)