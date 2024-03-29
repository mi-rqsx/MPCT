# Generated by Django 5.0 on 2024-02-08 10:49

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chem_c_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Carbon, max')),
                ('chem_c_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Carbon, min')),
                ('chem_mn_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Manganese, max')),
                ('chem_mn_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Manganese, min')),
                ('chem_si_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Silicon, max')),
                ('chem_si_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Silicon, min')),
                ('chem_p_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Phosphorus, max')),
                ('chem_p_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Phosphorus, min')),
                ('chem_s_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sulfur max')),
                ('chem_s_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sulfur min')),
                ('chem_ni_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nickel, max')),
                ('chem_ni_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nickel, min')),
                ('chem_cr_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Chromium, max')),
                ('chem_cr_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Chromium, min')),
                ('chem_cu_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Copper, max')),
                ('chem_cu_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Copper, min')),
                ('chem_al_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Aluminum, max')),
                ('chem_al_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Aluminum, min')),
                ('chem_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Vanadium, max')),
                ('chem_v_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Vanadium, min')),
                ('chem_nb_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Niobium, max')),
                ('chem_nb_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Niobium, min')),
                ('chem_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Molybdenum, max')),
                ('chem_mo_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Molybdenum, min')),
                ('chem_ti_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Titanium, max')),
                ('chem_ti_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Titanium, min')),
                ('chem_b_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Boron, max')),
                ('chem_b_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Boron, min')),
                ('chem_n_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nitrogen, max')),
                ('chem_n_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nitrogen, min')),
                ('chem_ca_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Calcium, max')),
                ('chem_ca_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Calcium, min')),
                ('chem_co_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cobalt, max')),
                ('chem_co_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cobalt, min')),
                ('chem_fe_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Iron, max')),
                ('chem_fe_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Iron, min')),
                ('chem_w_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tungsten, max')),
                ('chem_w_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tungsten, min')),
                ('chem_summ_nb_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb + V')),
                ('chem_summ_nb_ti_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb+Ti+V')),
                ('chem_summ_cr_cu_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Cu+Mo')),
                ('chem_summ_ni_cr_mo_cu_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ni+Cr+Mo+Cu')),
                ('chem_summ_cr_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Mo')),
                ('chem_c_equivalent', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='C Equivalent , max')),
                ('mech_tensile_strength_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='TS, max')),
                ('mech_tensile_strength_min', models.PositiveIntegerField(blank=True, null=True, verbose_name='TS, min')),
                ('mech_yield_strength_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='YS, max')),
                ('mech_yield_strength_min', models.PositiveIntegerField(blank=True, null=True, verbose_name='YS, min')),
                ('mech_strength_units', models.CharField(blank=True, choices=[('MPa', 'Megapascal'), ('PSI', 'Pounds per square inch'), ('KSI', 'Kilopounds per square inch')], default='MPa', max_length=20, null=True)),
                ('mech_hardness_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='Hardness, max')),
                ('mech_hardness_units', models.CharField(blank=True, choices=[('HB', 'Brinell'), ('HV', 'Vickers'), ('HRC', 'Rockwell C'), ('HRB', 'Rockwell B'), ('HRA', 'Rockwell A')], default='HB', max_length=20, null=True)),
                ('mech_toughness_single', models.PositiveIntegerField(blank=True, null=True, verbose_name='Impact Test, Minimum')),
                ('mech_toughness_mean', models.PositiveIntegerField(blank=True, null=True, verbose_name='Impact Test, Average')),
                ('mech_toughness_units', models.CharField(blank=True, choices=[('J', 'Joule')], default='J', max_length=20, null=True)),
                ('mech_toughness_size', models.CharField(blank=True, choices=[('10x10', '10x10'), ('7.5x10', '7.5x10'), ('5x10', '5x10'), ('2.5x10', '2.5x10')], default='10x10', max_length=20, null=True)),
                ('supp_nace', models.BooleanField(default=True, verbose_name='NACE MR0175')),
                ('supp_wst2004', models.BooleanField(default=True, verbose_name='W-ST-2004, TCO')),
                ('supp_lst2009', models.BooleanField(default=False, verbose_name='L-ST-2009, TCO')),
                ('supp_hic', models.BooleanField(default=False, verbose_name='HIC test')),
                ('supp_dwtt', models.BooleanField(default=False, verbose_name='Drop Weight  Tear Test')),
                ('supp_fpbt', models.BooleanField(default=False, verbose_name='Four Point Bend test')),
                ('supp_ssc', models.BooleanField(default=False, verbose_name='Sulfide Stress Corrosion test')),
                ('gen_grade', models.CharField(max_length=100, verbose_name='Grade')),
            ],
            options={
                'verbose_name': 'Material',
                'db_table': 'Material',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Type Material',
                'db_table': 'Type Material',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Specification',
                'db_table': 'Specification',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('chem_c_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Carbon, max')),
                ('chem_c_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Carbon, min')),
                ('chem_mn_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Manganese, max')),
                ('chem_mn_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Manganese, min')),
                ('chem_si_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Silicon, max')),
                ('chem_si_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Silicon, min')),
                ('chem_p_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Phosphorus, max')),
                ('chem_p_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Phosphorus, min')),
                ('chem_s_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sulfur max')),
                ('chem_s_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sulfur min')),
                ('chem_ni_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nickel, max')),
                ('chem_ni_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nickel, min')),
                ('chem_cr_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Chromium, max')),
                ('chem_cr_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Chromium, min')),
                ('chem_cu_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Copper, max')),
                ('chem_cu_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Copper, min')),
                ('chem_al_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Aluminum, max')),
                ('chem_al_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Aluminum, min')),
                ('chem_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Vanadium, max')),
                ('chem_v_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Vanadium, min')),
                ('chem_nb_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Niobium, max')),
                ('chem_nb_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Niobium, min')),
                ('chem_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Molybdenum, max')),
                ('chem_mo_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Molybdenum, min')),
                ('chem_ti_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Titanium, max')),
                ('chem_ti_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Titanium, min')),
                ('chem_b_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Boron, max')),
                ('chem_b_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Boron, min')),
                ('chem_n_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nitrogen, max')),
                ('chem_n_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nitrogen, min')),
                ('chem_ca_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Calcium, max')),
                ('chem_ca_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Calcium, min')),
                ('chem_co_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cobalt, max')),
                ('chem_co_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cobalt, min')),
                ('chem_fe_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Iron, max')),
                ('chem_fe_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Iron, min')),
                ('chem_w_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tungsten, max')),
                ('chem_w_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tungsten, min')),
                ('chem_summ_nb_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb + V')),
                ('chem_summ_nb_ti_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Nb+Ti+V')),
                ('chem_summ_cr_cu_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Cu+Mo')),
                ('chem_summ_ni_cr_mo_cu_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ni+Cr+Mo+Cu')),
                ('chem_summ_cr_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cr+Mo')),
                ('chem_c_equivalent', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='C Equivalent , max')),
                ('mech_tensile_strength_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='TS, max')),
                ('mech_tensile_strength_min', models.PositiveIntegerField(blank=True, null=True, verbose_name='TS, min')),
                ('mech_yield_strength_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='YS, max')),
                ('mech_yield_strength_min', models.PositiveIntegerField(blank=True, null=True, verbose_name='YS, min')),
                ('mech_strength_units', models.CharField(blank=True, choices=[('MPa', 'Megapascal'), ('PSI', 'Pounds per square inch'), ('KSI', 'Kilopounds per square inch')], default='MPa', max_length=20, null=True)),
                ('mech_hardness_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='Hardness, max')),
                ('mech_hardness_units', models.CharField(blank=True, choices=[('HB', 'Brinell'), ('HV', 'Vickers'), ('HRC', 'Rockwell C'), ('HRB', 'Rockwell B'), ('HRA', 'Rockwell A')], default='HB', max_length=20, null=True)),
                ('mech_toughness_single', models.PositiveIntegerField(blank=True, null=True, verbose_name='Impact Test, Minimum')),
                ('mech_toughness_mean', models.PositiveIntegerField(blank=True, null=True, verbose_name='Impact Test, Average')),
                ('mech_toughness_units', models.CharField(blank=True, choices=[('J', 'Joule')], default='J', max_length=20, null=True)),
                ('mech_toughness_size', models.CharField(blank=True, choices=[('10x10', '10x10'), ('7.5x10', '7.5x10'), ('5x10', '5x10'), ('2.5x10', '2.5x10')], default='10x10', max_length=20, null=True)),
                ('supp_nace', models.BooleanField(default=True, verbose_name='NACE MR0175')),
                ('supp_wst2004', models.BooleanField(default=True, verbose_name='W-ST-2004, TCO')),
                ('supp_lst2009', models.BooleanField(default=False, verbose_name='L-ST-2009, TCO')),
                ('supp_hic', models.BooleanField(default=False, verbose_name='HIC test')),
                ('supp_dwtt', models.BooleanField(default=False, verbose_name='Drop Weight  Tear Test')),
                ('supp_fpbt', models.BooleanField(default=False, verbose_name='Four Point Bend test')),
                ('supp_ssc', models.BooleanField(default=False, verbose_name='Sulfide Stress Corrosion test')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=200, null=True)),
                ('po', models.CharField(max_length=100)),
                ('heat_number', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('acceptance_status', models.BooleanField()),
                ('comment', models.TextField(blank=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mpct_app.material')),
            ],
            options={
                'verbose_name': 'Certificate',
                'db_table': 'Certificate',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='material',
            name='gen_material_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mpct_app.materialtype', verbose_name='Type of material'),
        ),
        migrations.AddField(
            model_name='material',
            name='gen_specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mpct_app.specification', verbose_name='Specification'),
        ),
    ]
