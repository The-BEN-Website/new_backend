from django.urls import path
from .views import Postlistview, PostDetailview, PostCreateview, PostManageView

app_name = 'core_api'

urlpatterns = [
    path('<int:pk>', PostDetailview.as_view(), name='detail'),
    path('<int:pk>/manage', PostManageView.as_view(), name='manage'),
    path('', Postlistview.as_view(), name='list'),
    path('create', PostCreateview.as_view(), name='create'),
]
