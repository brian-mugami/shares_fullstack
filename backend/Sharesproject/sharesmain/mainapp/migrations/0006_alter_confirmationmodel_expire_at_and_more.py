# Generated by Django 4.1.7 on 2023-02-23 19:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677183958),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ddc5c0f6-6594-4972-9cf0-7ea921c8c71c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
