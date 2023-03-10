# Generated by Django 4.1.7 on 2023-03-05 11:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1678020818),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('624ab8fc-62ab-46e4-b289-4128338c3893'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
