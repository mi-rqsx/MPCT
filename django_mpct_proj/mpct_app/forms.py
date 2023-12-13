from django import forms
from django.forms import ModelForm
from .models import Certificate, BaseChemistry, BaseMechanical, BaseSupplementary

class CerificateForm(ModelForm):
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        material = self.instance.material  # assuming 'material' is the FK to Material

        # if material.field4 is not None:  # replace 'field4' with your field name
        #     self.fields['field4'] = forms.CharField()  # or whatever type of field it is

        # List of fields from the inherited models
        inherited_fields = ['field4', 'field5', 'field6']  # replace with your field names

        for field in inherited_fields:
            if getattr(material, field) is not None:
                self.fields[field] = forms.CharField()  # or whatever type of field it is 
    """
    
    class Meta:
        model = Certificate
        fields = '__all__' # grabs all fields
        # fields = []


        # labels = {
        #     'material': 'Material',
        # }

        error_messages = {
            'stars': {
                'min_value': 'YO!! Min value is 0.',
                'max_value': 'YO!! Max value is 10.'
            }
        }
