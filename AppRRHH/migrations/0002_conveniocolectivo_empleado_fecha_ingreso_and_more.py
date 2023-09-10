# Generated by Django 4.2.4 on 2023-09-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRRHH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvenioColectivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_cct', models.CharField(max_length=10)),
                ('nombre_cct', models.CharField(max_length=30)),
                ('categorias_cct', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='actividadPrincipoal',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cuil',
            field=models.IntegerField(),
        ),
    ]
