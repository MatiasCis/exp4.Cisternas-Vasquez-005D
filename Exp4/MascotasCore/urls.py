from django.urls import URLPattern, path
from django.conf.urls.static import static
from django.conf import settings
from .views import index, somos, galeria, FormReg, FormCont, Api, MostrarProducto, formProducto, form_mod_producto, form_del_producto
from .views import MostrarCliente ,formCliente,form_mod_cliente,form_del_cliente
urlpatterns = [
    path('', index, name="index"),
    path('somos/', somos, name="somos"),
    path('galeria/', galeria, name="galeria"),
    path('FormReg/', FormReg, name="FormReg"),
    path('FormCont/', FormCont, name="FormCont"),
    path('Api/', Api, name="Api"),
    path('MostrarProducto/', MostrarProducto, name="MostrarProducto"),
    path('formProducto/', formProducto, name="formProducto"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),

    path('MostrarCliente/', MostrarCliente, name="MostrarCliente"),
    path('formCliente/', formCliente, name="formCliente"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),

    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 