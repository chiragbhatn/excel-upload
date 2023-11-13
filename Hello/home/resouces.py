from import_export import resources
from .models import Port


class PortResource(resources.ModelResource):
    class Meta:
        model = Port
