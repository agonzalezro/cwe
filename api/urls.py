from django.conf.urls import patterns, include, url

from tastypie.api import Api
from api.resources import (CompanyResource,
                           PersonResource,
                           OrganizationResource,
                           PoliticianResource)


api = Api(api_name='v1')
api.register(CompanyResource())
api.register(PersonResource())
api.register(OrganizationResource())
api.register(PoliticianResource())


urlpatterns = patterns('',
    url(r'', include(api.urls)),
)
