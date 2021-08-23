# Generated by Django 3.1.2 on 2021-08-22 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20210822_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='person_all',
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='client_allposts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_allposts', to='blog.post'),
        ),
    ]
