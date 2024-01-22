from django import forms
from .models import Material, Certificate


class SelectSpecificationForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["specification"]


class CheckCertificate(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = "__all__"
        widgets = {
            'id': forms.HiddenInput(),
            'material': forms.TextInput(attrs={'disabled': 'disabled'})
        }

    def __init__(self, *args, **kwargs):
        super(CheckCertificate, self).__init__(*args, **kwargs)
        self.fields['id'].label = ""
        self.fields['chem_c_max'].label = "Carbon, C"
        self.fields['chem_mn_max'].label = "Manganese, Mn"
        self.fields['chem_si_max'].label = "Silicon, Si"
        self.fields['chem_p_max'].label = "Phosphorus, P"
        self.fields['chem_s_max'].label = "Sulfur, S"
        self.fields['chem_ni_max'].label = "Nickel, Ni"
        self.fields['chem_cr_max'].label = "Chromium, Cr"
        self.fields['chem_cu_max'].label = "Copper, Cu"
        self.fields['chem_al_max'].label = "Aluminum, Al"
        self.fields['chem_v_max'].label = "Vanadium, V"
        self.fields['chem_nb_max'].label = "Niobium, Nb"
        self.fields['chem_mo_max'].label = "Molybdenum, Mo"
        self.fields['chem_ti_max'].label = "Titanium, Ti"
        self.fields['chem_b_max'].label = "Boron, B"
        self.fields['chem_n_max'].label = "Nitrogen, N"
        self.fields['chem_ca_max'].label = "Calcium, Ca"
        self.fields['chem_co_max'].label = "Cobalt, Co"
        self.fields['chem_fe_max'].label = "Iron, Fe"
        self.fields['chem_w_max'].label = "Tungsten, W"
        self.fields['chem_c_equivalent'].label = "Carbon Equivalent, CE"

        self.fields['mech_tensile_strength_max'].label = "Tensile Strength"
        self.fields['mech_yield_strength_max'].label = "Yield Strength"
        # self.fields['mech_hardness_max'].label = "Hardness"


        # for field_name in self.fields:
        #     if '_max' in field_name:
        #         field_name_list = field_name.split('_')
        #         field = self.fields[field_name]
        #         field.label = field_name_list[1]

class SerchHeatForm(forms.Form):
    s_heat_number = forms.CharField(label = 'Search for heat number:')
