# Generated by Django 3.0a1 on 2022-08-08 10:18

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200, verbose_name='car_title')),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('NI', 'Niger'), ('BO', 'Borno '), ('TA', 'Taraba'), ('KD', 'Kaduna'), ('BA', 'Bauchi'), ('YO', 'Yobe'), ('ZA', 'Zamfara'), ('AD', 'Adamawa'), ('KW', 'Kwara'), ('KE', 'Kebbi'), ('BE', 'Benue'), ('PL', 'Plateau'), ('KO', 'Kogi'), ('OY', 'Oyo'), ('NA', 'Nasarawa'), ('SO', 'Sokoto'), ('KT', 'Katsina'), ('JI', 'Jigawa'), ('CR', 'Cross River'), ('KN', 'Kano'), ('GO', 'Gombe'), ('ED', 'Edo'), ('DE', 'Delta'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('RI', 'Rivers'), ('BY', 'Bayelsa'), ('OS', 'Osun'), ('FC', 'Fct'), ('EN', 'Enugun'), ('AK', 'Akwa Ibom'), ('EK', 'Ekit'), ('AB', 'Abia'), ('EB', 'Ebonyi'), ('IM', 'Imo'), ('AN', 'Anambra'), ('LA', 'Lagos')], max_length=10)),
                ('color', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='Year')),
                ('condition', models.CharField(max_length=200)),
                ('rent_price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('car_photo', models.ImageField(upload_to='cars_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])])),
                ('car_photo_1', models.ImageField(blank=True, upload_to='cars_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])])),
                ('car_photo_2', models.ImageField(blank=True, upload_to='cars_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])])),
                ('car_photo_3', models.ImageField(blank=True, upload_to='cars_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])])),
                ('car_photo_4', models.ImageField(blank=True, upload_to='cars_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])])),
                ('features', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=195)),
                ('body_style', models.CharField(max_length=200)),
                ('miles', models.PositiveIntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10)),
                ('passengers', models.PositiveIntegerField()),
                ('milage', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('is_latest', models.BooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('brand_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.Brand')),
            ],
        ),
    ]
