# Generated by Django 4.1.7 on 2023-02-24 12:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_confirmationmodel_expire_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationmodel',
            name='expire_at',
            field=models.IntegerField(default=1677244383),
        ),
        migrations.AlterField(
            model_name='confirmationmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e73e4fea-a1ac-4298-b9ae-60d15887762c'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
