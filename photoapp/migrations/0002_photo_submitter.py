# Generated by Django 4.2.2 on 2023-06-14 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.contrib.auth.models import User

def get_first_user_id():
    return User.objects.first().id


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='submitter',
            field=models.ForeignKey(default=get_first_user_id, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
