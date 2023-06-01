# Generated by Django 4.2.1 on 2023-05-31 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=30)),
                ('firstName', models.CharField(max_length=30)),
                ('birthPlace', models.CharField(max_length=30)),
                ('birthDate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('userName', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.role')),
            ],
        ),
    ]
