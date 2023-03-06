# Generated by Django 4.1.7 on 2023-02-25 16:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677347924),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0bfddeb8-5831-46cc-8972-a3b99eb54df3'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
