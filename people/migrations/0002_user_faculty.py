# Generated by Django 4.0.4 on 2022-05-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.CharField(choices=[('MB', 'Mechanical Engineering'), ('VST', 'Process and Systems Engineering'), ('EIT', 'Electrical Engineering and Information Technology'), ('IN', 'Computer Science'), ('MA', 'Mathematics'), ('NW', 'Natural Sciences'), ('ME', 'Medicine'), ('HW', 'Humanities, Social Sciences and Education'), ('WW', 'Economics and Management')], max_length=3, null=True, verbose_name='Faculty'),
        ),
    ]
