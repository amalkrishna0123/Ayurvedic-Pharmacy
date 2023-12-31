# Generated by Django 4.1.5 on 2023-07-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('request', models.TextField(blank=True)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField()),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
        migrations.DeleteModel(
            name='ReceivedEmail',
        ),
    ]
