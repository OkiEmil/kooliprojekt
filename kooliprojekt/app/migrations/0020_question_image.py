# Generated by Django 4.2.1 on 2023-05-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_question_correct_max_question_correct_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
