# Generated by Django 4.1.6 on 2023-03-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phonenum', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('date_joined', models.CharField(max_length=255)),
                ('is_superuser', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
    ]
