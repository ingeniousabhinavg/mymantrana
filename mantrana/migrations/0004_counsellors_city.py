# Generated by Django 4.1 on 2022-09-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantrana', '0003_counsellors_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellors',
            name='city',
            field=models.CharField(choices=[('Chandigarh', 'Chandigarh'), ('Sangur', 'Sangur'), ('Amritsar', 'Amritsar'), ('Ludhiana', 'Ludhiana'), ('Moga', 'Moga'), ('Sunam', 'Sunam'), ('other', 'other')], default='City', max_length=100),
        ),
    ]
