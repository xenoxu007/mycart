# Generated by Django 4.0.4 on 2022-04-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=30)),
                ('lname', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=300)),
                ('password', models.IntegerField(default='123')),
                ('Address1', models.CharField(default='', max_length=300)),
                ('Address2', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=400)),
                ('pinc', models.IntegerField(default='')),
                ('query', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='none', max_length=30)),
                ('desc', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default='')),
                ('sub', models.CharField(default='', max_length=30)),
                ('pub_date', models.DateField(default='0000-00-00')),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
