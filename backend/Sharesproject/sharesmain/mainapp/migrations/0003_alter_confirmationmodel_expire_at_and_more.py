# Generated by Django 4.1.7 on 2023-02-23 12:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677157926),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('249d2945-06a7-444d-bae2-39e60e25c04c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
