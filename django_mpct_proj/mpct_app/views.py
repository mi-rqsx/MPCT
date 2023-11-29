from django.shortcuts import render
from django.views.generic import  ListView, CreateView
from django.urls import reverse_lazy
from mpct_app.models import Material, MaterialType, Institution, Specifications


# Create your views here.
def home_view(request):
    return render (request, 'mpct_app/home.html')



# List of registered materials
class MaterialListView(ListView):
    # this view class will look through html files (templates) to find the pattern name model_list.html (material_list.html)
    model = Material
    # queryset = Material.objects.order_by('Specification') # you can use queryset
    context_object_name = "material_list"


# Page for registration of new material and its requirements
class MaterialCreateView(CreateView):
    model = Material
    fields = "__all__"
    # it will automaticaly save the data like .save()
    success_url = reverse_lazy('mpct_app:material_list_view') # I think, that default redirection is DetailView, But I want to redirect the user to the list of materials


# Page for registration of new material types (pipe, fitting...)
class MaterialTypeCreateView(CreateView):
    model = MaterialType
    fields = "__all__"
    success_url = reverse_lazy('mpct_app:home_view') 


# Page for registration of new institution
class InstitutionCreateView(CreateView):
    model = Institution
    fields = "__all__"
    success_url = reverse_lazy('mpct_app:home_view') 


class SpecificationsCreateView(CreateView):
    model = Specifications
    fields = "__all__"
    success_url = reverse_lazy('mpct_app:home_view')