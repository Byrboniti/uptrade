from django.urls import re_path
from some_app.views import IndexView
# from menus.views import menu_item

app_name = 'some_app'

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
