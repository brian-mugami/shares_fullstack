# Generated by Django 4.1.7 on 2023-02-25 20:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0030_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677359573),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('21c37485-a4f5-4621-bb52-6c1423fa5daf'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
