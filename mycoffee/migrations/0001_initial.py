# Generated by Django 2.0 on 2017-12-06 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('espresso_shots', models.PositiveIntegerField(default=1)),
                ('water', models.FloatField()),
                ('steamed_milk', models.BooleanField(default=False)),
                ('foam', models.BooleanField()),
                ('extra_instructions', models.CharField(blank=True, max_length=160, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('bean', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mycoffee.Bean')),
            ],
        ),
        migrations.CreateModel(
            name='Powders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Roast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Syrups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='coffee',
            name='powders',
            field=models.ManyToManyField(blank=True, to='mycoffee.Powders'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='roast',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mycoffee.Roast'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='syrups',
            field=models.ManyToManyField(blank=True, to='mycoffee.Syrups'),
        ),
        migrations.AddField(
            model_name='coffee',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
