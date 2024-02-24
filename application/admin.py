from django.contrib import admin
from .models import Usuario, Publicacion, Comentario, Conversacion

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'nombre',
        'apellidos',
        'correo',
    )
    list_display_links = ('usuario',)
    search_fields = ('usuario', 'nombre',)
    sortable_by = ('id',)


class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha',
        'descripcion',
        'id_usuario',
        'tipo',
    )
    list_display_links = ('fecha',)
    search_fields = ('descripcion',)
    list_filter = ('tipo',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha',
        'contenido',
        'id_publicacion',
        'id_usuario_comentario',
    )
    list_display_links = ('fecha',)
    search_fields = ('contenido',)

class ConversacionAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'contenido',
        'estatus',
        'id_usuario_orig',
        'id_usuario_dest',
    )
    list_display_links = ('fecha',)
    search_fields = ('contenido',)
    list_filter = ('estatus',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Conversacion, ConversacionAdmin)

