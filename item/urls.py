from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^query_by_pos/$', views.query_by_pos, name='query_by_pos'),
    url(r'^query_by_name/$', views.query_by_name, name='query_by_name'),
    url(r'^query_by_name/result$', views.query_by_name, name='query_by_name_result'),
    url(r'^detail/(?P<item_id>[0-9]+)$', views.item_detail, name='item_detail'),
    url(r'^detail/(?P<item_id>[0-9]+)/change_status$', views.change_status, name='change_status')
]