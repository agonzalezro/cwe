from tastypie.resources import ModelResource
from db.models import Company, Organization, Person, Politician


class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        allowed_methods = ['get']


class OrganizationResource(ModelResource):
    class Meta:
        queryset = Organization.objects.all()
        allowed_methods = ['get']


class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        allowed_methods = ['get']


class PoliticianResource(ModelResource):
    class Meta:
        queryset = Politician.objects.all()
        allowed_methods = ['get']
