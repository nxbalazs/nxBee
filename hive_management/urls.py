from django.urls import path
from hive_management import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('hive_management', views.hive_management, name='hive_management'),
    path('new_hive', views.new_hive, name='new_hive'),
    path('edit_hive/<int:pk>', views.edit_hive, name='edit_hive'),
    path('hive_detail/<int:pk>', views.hive_detail, name='hive_detail'),
    path('remove_hive/<int:pk>', views.remove_hive, name='remove_hive'),
    path('add_note/<int:pk>', views.add_note, name='add_note'),
    path('add_inspection/<int:pk>', views.add_inspection, name='add_inspection'),
    path('add_treatment/<int:pk>', views.add_treatment, name='add_treatment'),
    path('donate', views.donate, name='donate'),
    path('tutorials', views.tutorials, name='tutorials'),
    path('divide_hives', views.divide_hives, name='divide_hives'),
    path('search', views.search, name='search'),
]