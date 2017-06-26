
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import archive, metal, index,order,detail,delete_item,top,list1,list2, list3, list4, list5, alll, create
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<product_id>\d+)$', detail, name='detail'),	
    url(r'^top/', top, name='top'),
    url(r'^metal/(?P<items_metal_id>\d+)$', metal, name='metal'),
    url(r'^create/', create, name='create'),
    url(r'^alll/', alll, name='alll'),
    url(r"^archive/", archive, name='archive'),
    url(r'^order/', order, name='order'),
    url(r'^list1/', list1, name='list1'),
    url(r'^list2/', list2, name='list2'),
    url(r'^list3/', list3, name='list3'),
    url(r'^list4/', list4, name='list4'),
    url(r'^list5/', list5, name='list5'),
    url(r'^(?P<item_id>\d+)/delete_item', delete_item, name='delete_item'), 
 ]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
