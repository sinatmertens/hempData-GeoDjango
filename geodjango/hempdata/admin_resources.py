from import_export import resources
from .models import Field

class FieldResource(resources.ModelResource):
    class Meta:
        model = Field
        fields = ('id', 'name', 'location')  # Specify fields to include
        export_order = ('id', 'name', 'location')  # Optional: specify order
