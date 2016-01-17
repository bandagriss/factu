from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/$', 'factu.views.hola'),
    url(r'^$', 'factu.views.login'),
    url(r'^auth_view/$', 'factu.views.auth_view'),
    url(r'^home/$', 'factu.views.home'),
    url(r'^logout/$', 'factu.views.cerrar'),
    url(r'^estudiantesIndex/$', 'factu.views.estudiantesIndex'),
    url(r'^agregar/$', 'factu.views.llenaUsuarios'),
    url(r'^estudiantesIndexJson/', 'factu.views.estudiantesIndexJson'),
    url(r'^buscar/estudiante/', 'factu.views.buscarEstudiante'),

    #ACCOUNT
    url(r'^create/$', 'factu.views.crear'),
    url(r'^register_account/$', 'factu.views.register_account'),

]
