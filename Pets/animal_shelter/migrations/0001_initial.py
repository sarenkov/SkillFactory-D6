# Generated by Django 3.0.7 on 2020-06-28 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Owner',
                'verbose_name_plural': 'Owners',
                'db_table': 'Owners',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.TextField()),
                ('description', models.TextField()),
                ('receipt_date', models.DateTimeField(auto_now_add=True)),
                ('type', models.TextField(choices=[('cat', 'Кошка'), ('dog', 'Собака'), ('parrot', 'Папугай')])),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('pet_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animal_shelter.Owner')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animals',
                'db_table': 'Animals',
                'ordering': ['type'],
            },
        ),
    ]
