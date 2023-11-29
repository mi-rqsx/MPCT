from django.db import models

# it is not a model, it's a base template to be inherited by other models (Meta abstract = True)
class BaseChemistry(models.Model):
    chem_c_max = models.DecimalField(verbose_name='Carbon, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_c_min = models.DecimalField(verbose_name='Carbon, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_mn_max = models.DecimalField(verbose_name='Manganese, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_mn_min = models.DecimalField(verbose_name='Manganese, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_si_max = models.DecimalField(verbose_name='Silicon, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_si_min = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)

    chem_p_max = models.DecimalField(verbose_name='Phosphorus, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_p_min = models.DecimalField(verbose_name='Phosphorus, min', max_digits=6, decimal_places=4, null=True)

    chem_s_max = models.DecimalField(verbose_name='Sulfur max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_s_min = models.DecimalField(verbose_name='Sulfur min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_ni_max = models.DecimalField(verbose_name='Nickel, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_ni_min = models.DecimalField(verbose_name='Nickel, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_cr_max = models.DecimalField(verbose_name='Chromium, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_cr_min = models.DecimalField(verbose_name='Chromium, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_cu_max = models.DecimalField(verbose_name='Copper, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_cu_min = models.DecimalField(verbose_name='Copper, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_al_max = models.DecimalField(verbose_name='Aluminum, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_al_min = models.DecimalField(verbose_name='Aluminum, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_v_max = models.DecimalField(verbose_name='Vanadium, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_v_min = models.DecimalField(verbose_name='Vanadium, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_nb_max = models.DecimalField(verbose_name='Niobium, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_nb_min = models.DecimalField(verbose_name='Niobium, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_mo_max = models.DecimalField(verbose_name='Molybdenum, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_mo_min = models.DecimalField(verbose_name='Molybdenum, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_ti_max = models.DecimalField(verbose_name='Titanium, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_ti_min = models.DecimalField(verbose_name='Titanium, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_b_max = models.DecimalField(verbose_name='Boron, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_b_min = models.DecimalField(verbose_name='Boron, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_n_max = models.DecimalField(verbose_name='Nitrogen, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_n_min = models.DecimalField(verbose_name='Nitrogen, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_ca_max = models.DecimalField(verbose_name='Calcium, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_ca_min = models.DecimalField(verbose_name='Calcium, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_co_max = models.DecimalField(verbose_name='Cobalt, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_co_min = models.DecimalField(verbose_name='Cobalt, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_fe_max = models.DecimalField(verbose_name='Iron, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_fe_min = models.DecimalField(verbose_name='Iron, min', max_digits=6, decimal_places=4, null=True, blank=True)

    chem_w_max = models.DecimalField(verbose_name='Tungsten, max', max_digits=6, decimal_places=4, null=True, blank=True)
    chem_w_min = models.DecimalField(verbose_name='Tungsten, min', max_digits=6, decimal_places=4, null=True, blank=True)

    class Meta:
        abstract = True


# base template
class BaseMechanical(models.Model):

    STRESS_UNITS = (
        ('MPa', 'Megapascal'),
        ('PSI', 'Pounds per square inch'),
        ('KSI', 'Kilopounds per square inch'), # I don't why, but it turned out to be important to put a come at the end of the last tuple
    )

    HARDNESS_UNITS = (
        ('HB', 'Brinell'),
        ('HV', 'Vickers'), # needs to be specified HV5, HV10, HV30 ...
        ('HRC', 'Rockwell C'),
        ('HRB', 'Rockwell B'),
        ('HRA', 'Rockwell A'),
    )

    TOUGHNESS_UNITS = (
        ('J', 'Joule'), # more units to be added
        )
    
    TOUGHNESS_SIZES = (
        ('10x10', '10x10'),
        ('7.5x10', '7.5x10'), # check in ASTM 370
        ('5x10', '5x10'),
        ('2.5x10', '2.5x10'),
        )

    mech_tensile_strength_max = models.IntegerField(verbose_name='TS, max')
    mech_tensile_strength_min = models.IntegerField(verbose_name='TS, min')
    mech_yield_strength_max = models.IntegerField(verbose_name='YS, max')
    mech_yield_strength_min = models.IntegerField(verbose_name='YS, min')
    mech_strength_units = models.CharField(max_length=20, choices=STRESS_UNITS, default='MPa')

    mech_hardness_max = models.IntegerField(verbose_name='Hardness, max', null=True, blank=True)
    mech_hardness_units = models.CharField(max_length=20, choices=HARDNESS_UNITS, default='HB', null=True, blank=True)

    mech_toughness_min = models.IntegerField(verbose_name='Minimum', null=True, blank=True)
    mech_toughness_mean = models.IntegerField(verbose_name='Average', null=True, blank=True)
    mech_toughness_units = models.CharField(max_length=20, choices=TOUGHNESS_UNITS, default='J', null=True, blank=True)
    mech_toughness_size = models.CharField(max_length=20, choices=TOUGHNESS_SIZES, default='10x10', null=True, blank=True)

    class Meta:
        abstract = True

#-----------------------------------------------------------------

class Institution(models.Model):
    name = models.CharField(max_length=200) # ASTM, ASME, GOST, BS EN etc...

    def __str__(self):
        return f"{self.name}"


class Specifications(models.Model):
    institution = models.ForeignKey('Institution', on_delete=models.RESTRICT) 
    id_number = models.CharField(max_length=100)
    title = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.institution} {self.id_number}"


class MaterialType(models.Model):
    name = models.CharField(max_length=100) # Plate, pipe, Fitting...

    def __str__(self):
        return f"{self.name}"

class Material(BaseChemistry, BaseMechanical):
    material_type = models.ForeignKey('MaterialType', on_delete=models.RESTRICT) 
    specification = models.ForeignKey('Specifications',on_delete=models.RESTRICT) # e.g., ASTM A516
    grade = models.CharField(max_length=100)
    category = models.CharField(verbose_name='Class or Category', max_length=100, null=True, blank=True)

    class Meta:
        abstract = False

    def __str__(self) :
        return f"{self.material.specification.institution}-{self.material.specification.id_number} {self.material.grade} {self.material.category}"

   
