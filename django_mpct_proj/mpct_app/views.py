from django import forms
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Material, MaterialType, Specification, Certificate
from .forms import SelectSpecificationForm, CheckCertificate, SerchHeatForm, RegisterMaterialForm


def home_view(request):
    materials = Material.objects.all()
    form = SelectSpecificationForm()
    search_heat_form = SerchHeatForm() # move it the base template

    # you need to make detailed form with select ond option things making dropdown list
    if request.method == "POST":
        form = SelectSpecificationForm(request.POST) # get data from the form
        
        if form.is_valid():
            value = form.cleaned_data["gen_specification"]
            print(value)
            materials = Material.objects.filter(gen_specification=value).all()  # show filtered materilas based selected spec

    context = {
        'form': form,
        'search_heat_form': search_heat_form,
        'materials': materials,
    }

    return render(request, "mpct_app/home.html", context=context)


def search_heat_number(request):
    search_heat_form = SerchHeatForm(request.GET)
    if search_heat_form.is_valid():
        input_heat_num = search_heat_form.cleaned_data['s_heat_number']
        certs = Certificate.objects.filter(heat_number__icontains=input_heat_num)
        certs_list = list(certs.values())  # Convert QuerySet to list of dicts
        print(certs)
        return JsonResponse(certs_list, safe=False)
    return JsonResponse({'error':'Not able to validate form'})


def check_certificate_view(request, pk, grade=False):
    material = Material.objects.get(pk=pk)

    # I need this dict to be able to filter the form where all inherited fields the
    # same names of which in the material instance have values of None
    material_dict = model_to_dict(material)
    # print(material_dict)

    # this form is filtered on HTML side to show only origin Certificate attributes (not inherited)
    # form = CheckCertificate()

    if request.method == 'POST':
        form = CheckCertificate(request.POST)
        if form.is_valid():

            # here, I will put a logic to compare cert values with the material specification
            # as for now, I just save the cert results without checking them. 
            # BUT this logic better to provide on a client side (JavaScript). 
            # because, based on this logic, the only acceptance_status filed should be changed without 
            # reloading of page (ibn order not to lose inputs)
            print(f'\n\n\n {form.cleaned_data} \n\n\n ')
            form.save()
    else:
        form = CheckCertificate(initial={'material': f'{material.specification} {material.grade}'}) # material field is disabled in forms.py

    context = {
            "form": form,
            "material_dict": material_dict,
        }

    return render(request, "mpct_app/check_certificate.html", context=context)


# List of registered materials
class MaterialListView(ListView):
    # this view class will look through html files (templates) to find the pattern name model_list.html (material_list.html)
    model = Material
    # queryset = Material.objects.order_by('Specification') # you can use queryset
    context_object_name = "material_list"


class CertificateListView(ListView):
    # this view class will look through html files (templates) to find the pattern name model_list.html (material_list.html)
    model = Certificate
    # queryset = Material.objects.order_by('Specification') # you can use queryset
    context_object_name = "certificate_list"


def certificate_detail_view(request, pk):
    model_instance = Certificate.objects.get(pk=pk)

    # make separate dict objects for mech, chem and general parameters as you did for material detail
    data = {
        'model_instance_dict': model_to_dict(model_instance),
        'model_instance': model_instance,
    }

    return render(request, "mpct_app/certificate_detail.html", context=data)


# Page for registration of new material types (pipe, fitting...)
class MaterialTypeCreateView(CreateView):
    model = MaterialType
    fields = "__all__"
    success_url = reverse_lazy("mpct_app:home_view")


class SpecificationCreateView(CreateView):
    model = Specification
    fields = "__all__"
    success_url = reverse_lazy("mpct_app:home_view")

# Page for registration of new material and its requirements
class MaterialCreateView(CreateView):
    model = Material
    fields = "__all__"
    # it will automaticaly save the data like .save()
    success_url = reverse_lazy(
        "mpct_app:material_list_view"
    )  # I think, that default redirection is DetailView, But I want to redirect the user to the list of materials


def register_material(request):
    form = RegisterMaterialForm()

    if request.method == 'POST':
        form = RegisterMaterialForm(request.POST)
        if form.is_valid(): # if fields are filled out correctly.
            form.save()
            print(form.cleaned_data)
            return render(request, "mpct_app/home.html")


    context = {
        'form': form,
    }



    # just to c heck
    # methods = [method for method in dir(form) if callable(getattr(form, method))]
    # print(methods)

    # for field in form:
    #      if "chem_" in field.name:              
    #           print(field.label_tag)
    #           print(field)

    return render(request, "mpct_app/register_material.html", context=context)
    # in HTML: {% for key, value in  field_value_dict_gen.items %}



def material_detail_view(request, pk):
    model_instance = Material.objects.get(pk=pk)

    # returns a tuple of all fields as objects like (<django.db.models.fields.BigAutoField: id>, ...)
    all_fields_tuple = Material._meta.get_fields()

    # converts each field object into a string and then appends each string to a list by using a list comprehension
    field_value_list = [str(each_field) for each_field in all_fields_tuple]
    
    field_value_dict_gen = {}
    field_value_dict_chem = {}
    field_value_dict_mech = {}
    field_value_dict_supp = {}

    for item in field_value_list:
        try:
            my_key = item.split(".")[-1]
            # print(f"my_key:\n{my_key}\n\n-----------")
            my_value = str(getattr(model_instance, my_key))
            # print(f"my_value:\n{my_value}\n\n-----------")
            if my_value != "None":
                if "chem_" in my_key:
                    field_value_dict_chem[my_key] = my_value
                elif "mech_" in my_key:
                    field_value_dict_mech[my_key] = my_value
                elif "supp_" in my_key:
                    field_value_dict_supp[my_key] = my_value
                else:
                    field_value_dict_gen[my_key] = my_value
        except AttributeError as e:
            print(f'\n\n\n Exception: {e} END \n\n\n')


    data = {
        "field_value_dict_gen": field_value_dict_gen,  # I use this dict in html
        "field_value_dict_chem": field_value_dict_chem,
        "field_value_dict_mech": field_value_dict_mech,
        "field_value_dict_supp": field_value_dict_supp,
    }

    return render(
        request, "mpct_app/material_detail_func.html", context=data
    )  # in HTML: {% for key, value in  field_value_dict_gen.items %}






# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
