# Generated by Django 2.1.2 on 2018-11-11 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perritos', '0003_auto_20181024_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('comuna', models.CharField(blank=True, max_length=100)),
                ('foto_perfil', models.ImageField(blank=True, upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='nuevo',
            name='rut_dueno',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nuevo',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]