# Generated by Django 4.1.7 on 2023-03-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0006_rename_choice_id_submission_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
