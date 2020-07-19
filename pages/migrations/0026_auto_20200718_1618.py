# Generated by Django 2.2.10 on 2020-07-18 08:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20200718_1613'),
    ]

    operations = [
       migrations.AlterField(
            model_name='urlchecking',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Library'),
        ),
        migrations.AlterField(
            model_name='urlcheckingresult',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Library'),
        ),
        migrations.AddField(
            model_name='urlchecking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urlcheckingresult',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        )
    ]
