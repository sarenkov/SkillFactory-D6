# Generated by Django 3.0.7 on 2020-06-20 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='Полное имя')),
                ('birth_year', models.SmallIntegerField(verbose_name='Год рождения')),
                ('country', models.CharField(max_length=2, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное имя')),
            ],
            options={
                'verbose_name': 'Друг-читатель',
                'verbose_name_plural': 'Друзья-читатели',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Полное имя')),
                ('city', models.TextField(verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.TextField(verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('year_release', models.SmallIntegerField(default=0, verbose_name='Год издания')),
                ('copy_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество копий')),
                ('price', models.FloatField(default=0.0, verbose_name='Цена')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author')),
                ('friend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='p_library.Friend')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Publisher')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='author',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Publisher'),
        ),
    ]
