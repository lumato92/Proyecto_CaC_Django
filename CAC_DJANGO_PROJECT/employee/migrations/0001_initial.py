# Generated by Django 3.2.14 on 2022-10-17 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('base_salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('genre', models.CharField(choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], default='FEMENINO', max_length=20)),
                ('id_number', models.IntegerField()),
                ('tax_id_number', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('nationality', models.CharField(default='Argentina', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('start_date', models.DateField()),
                ('salary', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.puesto')),
            ],
        ),
    ]
