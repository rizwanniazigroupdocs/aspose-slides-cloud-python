from slides_configuration import *


request=GetMasterSlideRequest("test.pptx", slide_index=1)
response = master_api.get_master_slide(request)
print(response)
