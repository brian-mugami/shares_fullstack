# Generated by Django 4.1.7 on 2023-02-25 16:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677347532),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a7ac57ac-e661-4a4d-ac65-041404ce7d1a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
