# Generated by Django 4.1.7 on 2023-02-24 12:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677244136),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a8b0e5ff-9318-4749-b458-4102bdd65372'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
