from django.urls import path 
from . import views 

app_name = 'mpct_app'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    
    path('material_list', views.MaterialListView.as_view(), name='material_list_view'),
    path('material_detail_func/<int:pk>', views.material_detail_view, name='material_detail_func'),

    path('certificate_list', views.CertificateListView.as_view(), name='certificate_list_view'),
    path('certificate_detail/<str:pk>', views.certificate_detail_view, name='certificate_detail_view'),

    path('register_material', views.register_material, name='register_material'),
    path('material_type_create', views.MaterialTypeCreateView.as_view(), name='material_type_create_view'),
    path('specification_create', views.SpecificationCreateView.as_view(), name='specification_create_view'),

    path('check_certificate/<str:grade>/<int:pk>', views.check_certificate_view, name='check_certificate'),
    path('search_heat_number', views.search_heat_number, name='search_heat_number'),
]



"""
urlpatterns = [
    path('material/', material_view, name='material_view'),
    path('ajax/load-materials/', load_materials, name='ajax_load_materials'),
]
"""


