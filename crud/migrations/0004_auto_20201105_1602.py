# Generated by Django 3.1.2 on 2020-11-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20201105_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Perempuan', 'Perempuan'), ('Laki-laki', 'Laki-laki')], max_length=15),
        ),
    ]
