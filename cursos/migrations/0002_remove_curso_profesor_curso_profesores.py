# Generated by Django 4.2.7 on 2023-12-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='profesor',
        ),
        migrations.AddField(
            model_name='curso',
            name='profesores',
            field=models.ManyToManyField(related_name='cursos', to='cursos.profesor'),
        ),
    ]
