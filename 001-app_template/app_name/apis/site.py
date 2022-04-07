from django_restful_admin import RestFulAdminSite as _RestFulAdminSite

from django_restful_admin.router import DefaultRouter


class RestFulAdminSite(_RestFulAdminSite):

    def get_router(self):
        return DefaultRouter()


apiadmin_site = RestFulAdminSite()
