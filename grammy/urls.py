from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url('^$',views.index,name = 'index_page'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^search/', views.search, name='search'),
    url(r'^comment/(?P<image_id>\d+)', views.one_image, name='comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)