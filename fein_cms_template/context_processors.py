from django.contrib.sites.models import Site


def site(request):
    return {'SITE': Site.objects.get_current()}
