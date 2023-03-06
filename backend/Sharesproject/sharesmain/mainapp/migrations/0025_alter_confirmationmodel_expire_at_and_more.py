# Generated by Django 4.1.7 on 2023-02-25 15:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677341619),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('245eca5f-db78-43e2-8818-5becb2250ff1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]