# Generated by Django 4.1 on 2022-09-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantrana', '0005_alter_counsellors_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]