# Generated by Django 2.2.10 on 2020-07-18 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_auto_20181208_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='download_manager',
            field=models.TextField(default='wget {iurl} -O {output}'),
        ),
        migrations.CreateModel(
            name='URLCheckingResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('actual', models.CharField(max_length=2048, null=True)),
                ('updated_at', models.DateTimeField()),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Library')),
            ],
        ),
        migrations.CreateModel(
            name='URLChecking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected', models.CharField(max_length=2048)),
                ('script', models.CharField(max_length=2048)),
                ('activate', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField()),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Library')),
            ],
        ),
    ]