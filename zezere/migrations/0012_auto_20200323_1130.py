# Generated by Django 2.2.9 on 2020-03-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zezere", "0011_runrequest_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sshkey",
            name="key",
            field=models.CharField(max_length=1024, verbose_name="SSH Key"),
        ),
    ]
