# Generated by Django 4.1.7 on 2023-02-24 12:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677245284),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a3bdc267-1735-4f72-b5eb-4e30a197e8f6'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
