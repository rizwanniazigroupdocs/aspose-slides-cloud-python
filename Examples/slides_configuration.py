from asposeslidescloud.configuration import Configuration
from asposeslidescloud.apis.document_api import DocumentApi
from asposeslidescloud.apis.images_api import ImagesApi
from asposeslidescloud.apis.layout_slides_api import LayoutSlidesApi
from asposeslidescloud.apis.master_slides_api import MasterSlidesApi
from asposeslidescloud.apis.merge_document_api import MergeDocumentApi
from asposeslidescloud.apis.notes_slide_api import NotesSlideApi 
from asposeslidescloud.apis.placeholders_api import PlaceholdersApi
from asposeslidescloud.apis.properties_api import PropertiesApi
from asposeslidescloud.apis.text_api import TextApi

from asposeslidescloud.models.requests import *


configuration = Configuration()
configuration.app_sid = "78946fb4-3bd4-4d3e-b309-f9e2ff9ac6f9"
configuration.app_key ="b125f13bf6b76ed81ee990142d841195"
configuration.base_url = "api.aspose.cloud"
configuration.debug ="true"


slides_api = DocumentApi(configuration) 
images_api=ImagesApi(configuration)
layout_api=LayoutSlidesApi(configuration)
master_api=MasterSlidesApi(configuration)
merge_document_api=MergeDocumentApi(configuration)
notes_slides=NotesSlideApi(configuration)
placeholder_api=PlaceholdersApi(configuration)
properties_api=PropertiesApi(configuration)
text_api=TextApi(configuration)