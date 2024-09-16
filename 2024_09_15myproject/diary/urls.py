from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name= "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("pages/", views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    path("page/<uuid:id>/update/", views.page_updete, name="page_update"),
    path("page/<uuid:id>/delete/", views.page_delete, name="page_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)