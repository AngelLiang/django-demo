from django_restful_admin import RestFulAdminSite as _RestFulAdminSite

from .router import ReadOnlyRouter


class RestFulAdminSite(_RestFulAdminSite):

    def get_router(self):
        return ReadOnlyRouter()


apiadmin_site = RestFulAdminSite()
