# Generated by Django 5.0.4 on 2024-05-04 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_project_developer_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='developer',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile'),
        ),
    ]