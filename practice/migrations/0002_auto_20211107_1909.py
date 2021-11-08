# Generated by Django 3.2.8 on 2021-11-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarship_name', models.CharField(blank=True, max_length=100)),
                ('scholarship_url', models.CharField(blank=True, max_length=100)),
                ('scholarship_university', models.CharField(blank=True, max_length=100)),
                ('scholarship_deadline', models.CharField(blank=True, max_length=100)),
                ('scholarship_country', models.CharField(blank=True, max_length=100)),
                ('scholarship_Start_date', models.CharField(blank=True, max_length=100)),
                ('scholarship_program', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='firstname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='lastname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
