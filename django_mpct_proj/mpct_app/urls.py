from django.urls import path 
from . import views 

app_name = 'mpct_app'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('material_detail_func/<int:pk>', views.MaterialDetailViewFunc, name='material_detail_func'),
    path('material_list', views.MaterialListView.as_view(), name='material_list_view'),
    path('material_create', views.MaterialCreateView.as_view(), name='material_create_view'),
    path('material_type_create', views.MaterialTypeCreateView.as_view(), name='material_type_create_view'),
    path('specification_create', views.SpecificationCreateView.as_view(), name='specification_create_view'),
    path('material_detail/<int:pk>', views.MaterialDetailView.as_view(), name='material_detail'),
    path('check_certificate/<str:grade>/<int:pk>', views.check_certificate_view, name='check_certificate'),
]



"""
urlpatterns = [
    path('material/', material_view, name='material_view'),
    path('ajax/load-materials/', load_materials, name='ajax_load_materials'),
]
"""


