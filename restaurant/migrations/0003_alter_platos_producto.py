# Generated by Django 4.1.3 on 2022-11-22 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_platos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.project'),
        ),
    ]
