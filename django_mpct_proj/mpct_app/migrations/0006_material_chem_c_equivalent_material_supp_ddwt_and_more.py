# Generated by Django 4.2.7 on 2023-12-08 16:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mpct_app', '0005_alter_material_chem_al_max_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='chem_c_equivalent',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='C Equivalent , max'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_ddwt',
            field=models.BinaryField(blank=True, null=True, verbose_name='Drop-Down Tear Test'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_fpbt',
            field=models.BinaryField(blank=True, null=True, verbose_name='Four Point Bend test'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_hic',
            field=models.BinaryField(blank=True, null=True, verbose_name='Supplementary HIC test'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_mech_toughness_mean',
            field=models.IntegerField(blank=True, null=True, verbose_name='Supplementary Impact Test, Aver.'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_mech_toughness_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Supplementary Impact Test, Min.'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_nace',
            field=models.BinaryField(blank=True, null=True, verbose_name='NACE'),
        ),
        migrations.AddField(
            model_name='material',
            name='supp_scct',
            field=models.BinaryField(blank=True, null=True, verbose_name='Stress Corrosion Cracking test'),
        ),
        migrations.AlterField(
            model_name='material',
            name='mech_toughness_mean',
            field=models.IntegerField(blank=True, null=True, verbose_name='Impact Test, Average'),
        ),
        migrations.AlterField(
            model_name='material',
            name='mech_toughness_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Impact Test, Minimum'),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('chem_c_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Carbon, max')),
                ('chem_c_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Carbon, min')),
                ('chem_mn_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Manganese, max')),
                ('chem_mn_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Manganese, min')),
                ('chem_si_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Silicon, max')),
                ('chem_si_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('chem_p_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Phosphorus, max')),
                ('chem_p_min', models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Phosphorus, min')),
                ('chem_s_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Sulfur max')),
                ('chem_s_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Sulfur min')),
                ('chem_ni_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Nickel, max')),
                ('chem_ni_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Nickel, min')),
                ('chem_cr_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Chromium, max')),
                ('chem_cr_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Chromium, min')),
                ('chem_cu_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Copper, max')),
                ('chem_cu_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Copper, min')),
                ('chem_al_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Aluminum, max')),
                ('chem_al_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Aluminum, min')),
                ('chem_v_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Vanadium, max')),
                ('chem_v_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Vanadium, min')),
                ('chem_nb_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Niobium, max')),
                ('chem_nb_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Niobium, min')),
                ('chem_mo_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Molybdenum, max')),
                ('chem_mo_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Molybdenum, min')),
                ('chem_ti_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Titanium, max')),
                ('chem_ti_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Titanium, min')),
                ('chem_b_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Boron, max')),
                ('chem_b_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Boron, min')),
                ('chem_n_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Nitrogen, max')),
                ('chem_n_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Nitrogen, min')),
                ('chem_ca_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Calcium, max')),
                ('chem_ca_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Calcium, min')),
                ('chem_co_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Cobalt, max')),
                ('chem_co_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Cobalt, min')),
                ('chem_fe_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Iron, max')),
                ('chem_fe_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Iron, min')),
                ('chem_w_max', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Tungsten, max')),
                ('chem_w_min', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Tungsten, min')),
                ('chem_c_equivalent', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='C Equivalent , max')),
                ('mech_tensile_strength_max', models.IntegerField(verbose_name='TS, max')),
                ('mech_tensile_strength_min', models.IntegerField(verbose_name='TS, min')),
                ('mech_yield_strength_max', models.IntegerField(verbose_name='YS, max')),
                ('mech_yield_strength_min', models.IntegerField(verbose_name='YS, min')),
                ('mech_strength_units', models.CharField(choices=[('MPa', 'Megapascal'), ('PSI', 'Pounds per square inch'), ('KSI', 'Kilopounds per square inch')], default='MPa', max_length=20)),
                ('mech_hardness_max', models.IntegerField(blank=True, null=True, verbose_name='Hardness, max')),
                ('mech_hardness_units', models.CharField(blank=True, choices=[('HB', 'Brinell'), ('HV', 'Vickers'), ('HRC', 'Rockwell C'), ('HRB', 'Rockwell B'), ('HRA', 'Rockwell A')], default='HB', max_length=20, null=True)),
                ('mech_toughness_min', models.IntegerField(blank=True, null=True, verbose_name='Impact Test, Minimum')),
                ('mech_toughness_mean', models.IntegerField(blank=True, null=True, verbose_name='Impact Test, Average')),
                ('mech_toughness_units', models.CharField(blank=True, choices=[('J', 'Joule')], default='J', max_length=20, null=True)),
                ('mech_toughness_size', models.CharField(blank=True, choices=[('10x10', '10x10'), ('7.5x10', '7.5x10'), ('5x10', '5x10'), ('2.5x10', '2.5x10')], default='10x10', max_length=20, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('po', models.CharField(max_length=100)),
                ('heat_number', models.CharField(max_length=100, unique=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mpct_app.material')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
