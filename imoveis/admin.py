from django.contrib import admin
from .models import Imovel, Tipo


# Register your models here.
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('lote', 'endereco', 'situacao', 'tipo','ativo')
    list_filter = ('lote', 'situacao')
    search_fields = ('lote', 'situacao')
    list_editable = ('endereco','ativo')


admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Tipo)
