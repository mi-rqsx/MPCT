import uuid
from django.db import models
from django.core.validators import MinValueValidator


# it is not a model, it's a base template to be inherited by other models (Meta abstract = True)
class BaseChemistry(models.Model):
    chem_c_max = models.DecimalField(verbose_name='Carbon, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_c_min = models.DecimalField(verbose_name='Carbon, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_mn_max = models.DecimalField(verbose_name='Manganese, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_mn_min = models.DecimalField(verbose_name='Manganese, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_si_max = models.DecimalField(verbose_name='Silicon, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_si_min = models.DecimalField(verbose_name='Silicon, min',max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_p_max = models.DecimalField(verbose_name='Phosphorus, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_p_min = models.DecimalField(verbose_name='Phosphorus, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_s_max = models.DecimalField(verbose_name='Sulfur max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_s_min = models.DecimalField(verbose_name='Sulfur min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_ni_max = models.DecimalField(verbose_name='Nickel, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_ni_min = models.DecimalField(verbose_name='Nickel, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_cr_max = models.DecimalField(verbose_name='Chromium, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_cr_min = models.DecimalField(verbose_name='Chromium, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_cu_max = models.DecimalField(verbose_name='Copper, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_cu_min = models.DecimalField(verbose_name='Copper, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_al_max = models.DecimalField(verbose_name='Aluminum, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_al_min = models.DecimalField(verbose_name='Aluminum, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_v_max = models.DecimalField(verbose_name='Vanadium, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_v_min = models.DecimalField(verbose_name='Vanadium, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_nb_max = models.DecimalField(verbose_name='Niobium, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_nb_min = models.DecimalField(verbose_name='Niobium, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_mo_max = models.DecimalField(verbose_name='Molybdenum, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_mo_min = models.DecimalField(verbose_name='Molybdenum, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_ti_max = models.DecimalField(verbose_name='Titanium, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_ti_min = models.DecimalField(verbose_name='Titanium, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_b_max = models.DecimalField(verbose_name='Boron, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_b_min = models.DecimalField(verbose_name='Boron, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_n_max = models.DecimalField(verbose_name='Nitrogen, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_n_min = models.DecimalField(verbose_name='Nitrogen, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_ca_max = models.DecimalField(verbose_name='Calcium, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_ca_min = models.DecimalField(verbose_name='Calcium, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_co_max = models.DecimalField(verbose_name='Cobalt, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_co_min = models.DecimalField(verbose_name='Cobalt, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_fe_max = models.DecimalField(verbose_name='Iron, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_fe_min = models.DecimalField(verbose_name='Iron, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_w_max = models.DecimalField(verbose_name='Tungsten, max', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_w_min = models.DecimalField(verbose_name='Tungsten, min', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_summ_nb_v_max = models.DecimalField(verbose_name='Nb + V', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_summ_nb_ti_v_max = models.DecimalField(verbose_name='Nb+Ti+V', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_summ_cr_cu_mo_max = models.DecimalField(verbose_name='Cr+Cu+Mo', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_summ_ni_cr_mo_cu_max = models.DecimalField(verbose_name='Ni+Cr+Mo+Cu', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])
    chem_summ_cr_mo_max = models.DecimalField(verbose_name='Cr+Mo', max_digits=6, decimal_places=4, null=True, blank=True, validators=[MinValueValidator(0)])

    chem_c_equivalent  = models.DecimalField(verbose_name='C Equivalent , max', max_digits=6, decimal_places=4, null=True, blank=True)

    class Meta:
        abstract = True


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

    mech_tensile_strength_max = models.PositiveIntegerField(verbose_name='TS, max', null=True, blank=True)
    mech_tensile_strength_min = models.PositiveIntegerField(verbose_name='TS, min', null=True, blank=True)
    mech_yield_strength_max = models.PositiveIntegerField(verbose_name='YS, max', null=True, blank=True)
    mech_yield_strength_min = models.PositiveIntegerField(verbose_name='YS, min', null=True, blank=True)
    mech_strength_units = models.CharField(max_length=20, choices=STRESS_UNITS, default='MPa', null=True, blank=True)

    mech_hardness_max = models.PositiveIntegerField(verbose_name='Hardness, max', null=True, blank=True)
    mech_hardness_units = models.CharField(max_length=20, choices=HARDNESS_UNITS, default='HB', null=True, blank=True)

    mech_toughness_single = models.PositiveIntegerField(verbose_name='Impact Test, Minimum', null=True, blank=True)
    mech_toughness_mean = models.PositiveIntegerField(verbose_name='Impact Test, Average', null=True, blank=True)
    mech_toughness_units = models.CharField(max_length=20, choices=TOUGHNESS_UNITS, default='J', null=True, blank=True)
    mech_toughness_size = models.CharField(max_length=20, choices=TOUGHNESS_SIZES, default='10x10', null=True, blank=True)

    class Meta:
        abstract = True


class BaseSupplementary(models.Model):
    supp_nace = models.BooleanField(verbose_name='NACE MR0175', default=True)
    supp_wst2004 = models.BooleanField(verbose_name='W-ST-2004, TCO', default=True)
    supp_lst2009 = models.BooleanField(verbose_name='L-ST-2009, TCO', default=False)
    supp_hic = models.BooleanField(verbose_name='HIC test', default=False) # 
    supp_dwtt = models.BooleanField(verbose_name='Drop Weight  Tear Test', default=False) # add spec
    supp_fpbt =  models.BooleanField(verbose_name='Four Point Bend test', default=False) # add ASTM spec
    supp_ssc =  models.BooleanField(verbose_name='Sulfide Stress Corrosion test', default=False) # add ASTM spec
    # supp_mech_toughness_single = models.PositiveIntegerField(verbose_name='Supplementary Impact Test, Min.', null=True, blank=True)
    # supp_mech_toughness_mean = models.PositiveIntegerField(verbose_name='Supplementary Impact Test, Aver.', null=True, blank=True)

    class Meta:
        abstract = True

#-----------------------------------------------------------------

class Specification(models.Model):
    name = models.CharField(max_length=200) # ASTM A516, ASME SA-516, GOST 1050, BS EN etc...
    title = models.CharField(max_length=300)

    class Meta:
        db_table = 'Specification'
        verbose_name = 'Specification'

    def __str__(self):
        return f"{self.name}"


class MaterialType(models.Model):
    name = models.CharField(max_length=100) # Plate, pipe, Fitting...

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = False
        db_table = 'Type Material'
        verbose_name = 'Type Material'

class Material(BaseChemistry, BaseMechanical, BaseSupplementary):
    gen_specification = models.ForeignKey(to=Specification, verbose_name='Specification', on_delete=models.RESTRICT) # e.g., ASTM A516
    gen_grade = models.CharField(verbose_name='Grade', max_length=100)
    gen_material_type = models.ForeignKey(to=MaterialType, verbose_name='Type of material', on_delete=models.RESTRICT)

    class Meta:
        abstract = False
        db_table = 'Material'
        verbose_name = 'Material'

    def __str__(self):
        return f"{self.gen_specification} Gr. {self.gen_grade}"


class Certificate(BaseChemistry, BaseMechanical, BaseSupplementary):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=200, null=True) # needs to be changed to MS account data when deployed in Azure
    po = models.CharField(max_length=100) # you need to create a logic that provides option for user to leave this field empty. However, NULL=False.
    heat_number = models.CharField(max_length=100) # unique=True
    manufacturer = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True) # sets the field to now when the object is saved, auto_now_add=True: sets the field to now when the object is created.
    material = models.ForeignKey('Material', on_delete=models.RESTRICT) # probably, it's worth to change "on_delete" to something that allows to save old data, and NULL new data
    acceptance_status = models.BooleanField()
    comment = models.TextField(blank=True)

    def __str__(self) :
        return f"{self.heat_number}, {self.material}"

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Certificate._meta.fields]

    class Meta:
        abstract = False
        db_table = 'Certificate'
        verbose_name = 'Certificate'
