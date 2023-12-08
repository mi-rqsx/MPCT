from django.shortcuts import render
from django.views.generic import  ListView, CreateView, DetailView
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



class MaterialDetailView(DetailView):
    # returns only one instance (material) from Material model
    model = Material


def MaterialDetailViewFunc(request, pk):
    model_instance = Material.objects.get(pk=pk)

    # returns a tuple of all fields as objects like (<django.db.models.fields.BigAutoField: id>, ...)
    all_fields_tuple = Material._meta.get_fields()

    # converts each field object into a string and then appends each string to a list by using a list comprehension
    field_value_list = [str(each_field) for each_field in all_fields_tuple]

    # field_value_dict_all = { item.split('.')[-1] : str(getattr(model_instance, item.split('.')[-1])) for item in field_value_list if str(getattr(model_instance, item.split('.')[-1])) != 'None'}

    field_value_dict_gen = {}
    field_value_dict_chem = {}
    field_value_dict_mech = {}

    for item in field_value_list:
        my_key = item.split('.')[-1]
        my_value = str(getattr(model_instance, my_key))
        if my_value != 'None':
            if 'chem_' in my_key:
                field_value_dict_chem[my_key] = my_value
            elif 'mech_' in my_key:
                field_value_dict_mech[my_key] = my_value
            else:
                field_value_dict_gen[my_key] = my_value

    data = {
        'model_instance': model_instance,
        'all_fields_tuple': all_fields_tuple,
        'field_value_list': field_value_list,
        'field_value_dict_gen': field_value_dict_gen,
        'field_value_dict_chem': field_value_dict_chem,
        'field_value_dict_mech': field_value_dict_mech,
    }

    return render(request, 'mpct_app/material_detail_func.html', context=data)