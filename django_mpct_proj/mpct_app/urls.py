from django.urls import path 
from . import views 

app_name = 'mpct_app'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('material_list', views.MaterialListView.as_view(), name='material_list_view'),
    path('material_create', views.MaterialCreateView.as_view(), name='material_create_view'),
    path('material_type_create', views.MaterialTypeCreateView.as_view(), name='material_type_create_view'),
    path('Institution_create', views.InstitutionCreateView.as_view(), name='institution_create_view'),
    path('Specifications_create', views.SpecificationsCreateView.as_view(), name='specifications_create_view'),
]


