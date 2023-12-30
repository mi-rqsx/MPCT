from gc import disable
from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Material, MaterialType, Specification
from .forms import SelectSpecificationForm, CheckCertificate


def home_view(request):
    if request.method == "POST":
        form = SelectSpecificationForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data["specification"]
            print(value)
            materials = Material.objects.filter(
                specification=value
            ).all()  # show filtered materilas based selected spec
    else:
        form = SelectSpecificationForm()
        materials = Material.objects.all()  # show all list of materials

    return render(request, "mpct_app/home.html", {"form": form, "materials": materials})











def check_certificate_view(request, grade, pk):
    material = Material.objects.get(pk=pk)
    material_dict = model_to_dict(material)
    # print(material_dict)

    form = CheckCertificate()
    print(f"   ppppppppp  {form['heat_number'].name}")


    # for f in form:
    #     print(f'f starts: \n\n\n {f} \n\n\n f ends')

    # make a form for a particular instance:
    material_form = CheckCertificate(instance=material)

    
    for field in material_form:
        field_name = field.name
        field_name_list = field_name.split(',')
        if ', max' in field_name:
            material_form[field_name].field.widget.attrs = {'value': field_name_list[0]}

    
    # for key, value in material_dict.items():
    #     if value is None:
    # #         # material_form[key].label = None
    # #         # material_form[key].field.widget_attrs({'type': 'hidden'})
    # #         # material_form[key].field.widget.attrs = {'disabled': 'disabled'}
    # #         # {'type': 'hidden'}
    #         pass



    # for key, value in material_dict.items():
    #     for field in form:
    #         # print(f'  [key]     {form[key].name}')
    #         if key == form[key].name:
    #             if value is not None:
    #                     print('IT WORKED')
    #                     print(form[key].label_tag)
    #                     print(form[key])

    context = {
        'form': form,
        'material_form': material_form,
        'material': material,
        'material_dict': material_dict,
    }

    return render(request, "mpct_app/check_certificate.html", context=context)











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
    success_url = reverse_lazy(
        "mpct_app:material_list_view"
    )  # I think, that default redirection is DetailView, But I want to redirect the user to the list of materials


# Page for registration of new material types (pipe, fitting...)
class MaterialTypeCreateView(CreateView):
    model = MaterialType
    fields = "__all__"
    success_url = reverse_lazy("mpct_app:home_view")


class SpecificationCreateView(CreateView):
    model = Specification
    fields = "__all__"
    success_url = reverse_lazy("mpct_app:home_view")


class MaterialDetailView(DetailView):
    # returns only one instance (material) from Material model
    model = Material


def MaterialDetailViewFunc(request, pk):
    model_instance = Material.objects.get(pk=pk)

    # returns a tuple of all fields as objects like (<django.db.models.fields.BigAutoField: id>, ...)
    all_fields_tuple = Material._meta.get_fields()
    # print(f'all_fields_tuple: \n {all_fields_tuple} \n \n')
    # print(f"all_fields_tuple:\n{all_fields_tuple}\n\n-----------")

    # converts each field object into a string and then appends each string to a list by using a list comprehension
    field_value_list = [str(each_field) for each_field in all_fields_tuple]
    # print(f'field_value_list: \n {field_value_list} \n \n')
    # print(f"field_value_list:\n{field_value_list}\n\n-----------")
    # field_value_dict_all = { item.split('.')[-1] : str(getattr(model_instance, item.split('.')[-1])) for item in field_value_list if str(getattr(model_instance, item.split('.')[-1])) != 'None'}

    field_value_dict_gen = {}
    field_value_dict_chem = {}
    field_value_dict_mech = {}
    field_value_dict_supp = {}

    for item in field_value_list:
        if ">" in item:
            pass
        else:
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

    data = {
        # 'model_instance': model_instance,
        # 'all_fields_tuple': all_fields_tuple,
        # 'field_value_list': field_value_list,
        "field_value_dict_gen": field_value_dict_gen,  # I use this dict in html
        "field_value_dict_chem": field_value_dict_chem,
        "field_value_dict_mech": field_value_dict_mech,
        "field_value_dict_supp": field_value_dict_supp,
    }

    return render(
        request, "mpct_app/material_detail_func.html", context=data
    )  # in HTML: {% for key, value in  field_value_dict_gen.items %}


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
