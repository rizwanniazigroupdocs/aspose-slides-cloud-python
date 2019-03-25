from slides_configuration import *


request=GetMasterSlidesListRequest("test.pptx")
response =master_api.get_master_slides_list(request)
print(response)