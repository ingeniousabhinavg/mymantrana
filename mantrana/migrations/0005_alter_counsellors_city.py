# Generated by Django 4.1 on 2022-09-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantrana', '0004_counsellors_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellors',
            name='city',
            field=models.CharField(choices=[('Chandigarh', 'Chandigarh'), ('Sangur', 'Sangur'), ('Amritsar', 'Amritsar'), ('Ludhiana', 'Ludhiana'), ('Moga', 'Moga'), ('Sunam', 'Sunam'), ('other', 'other')], default='Select City', max_length=100),
        ),
    ]
