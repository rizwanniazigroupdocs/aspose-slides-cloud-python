from slides_configuration import *

request= PostSlidesSplitRequest("test.pptx",  "PNG",  "1", "2")
response = slides_api.post_slides_split(request)
print(response)