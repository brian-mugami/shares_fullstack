# Generated by Django 4.1.7 on 2023-02-23 19:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677184509),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('996d940e-7700-428e-8b5a-fac9e2a99930'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
