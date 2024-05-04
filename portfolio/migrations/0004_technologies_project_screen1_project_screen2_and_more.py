# Generated by Django 5.0.4 on 2024-05-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_descriptionen_project_descriptionsp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='portfolio/images/icons')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='screen1',
            field=models.ImageField(default=None, upload_to='portfolio/images/screens'),
        ),
        migrations.AddField(
            model_name='project',
            name='screen2',
            field=models.ImageField(default=None, upload_to='portfolio/images/screens'),
        ),
        migrations.AddField(
            model_name='project',
            name='screen3',
            field=models.ImageField(default=None, upload_to='portfolio/images/screens'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default=None, upload_to='portfolio/images/covers'),
        ),
    ]