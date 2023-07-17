# Generated by Django 2.2.28 on 2023-07-17 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_files_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileupload',
            options={'ordering': ['-created_at'], 'verbose_name': 'File Upload', 'verbose_name_plural': 'Files Uploads'},
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='files_uploaded', to=settings.AUTH_USER_MODEL),
        ),
    ]
