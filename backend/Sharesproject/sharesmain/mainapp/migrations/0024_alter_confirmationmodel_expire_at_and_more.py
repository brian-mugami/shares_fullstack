# Generated by Django 4.1.7 on 2023-02-25 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677340510),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d0e4ca43-ad32-4d45-ab7c-c7520d5924c2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]