from slides_configuration import *

request=GetSlidesPlaceholdersRequest("placeholders.pptx", slide_index=1,password="password")
response =placeholder_api.get_slides_placeholders(request)
print(response)