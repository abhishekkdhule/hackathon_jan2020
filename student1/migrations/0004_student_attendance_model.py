# Generated by Django 3.0.2 on 2020-01-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student1', '0003_auto_20200129_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_attendance_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.DecimalField(decimal_places=0, max_digits=10, unique=True)),
                ('subject1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('subject2', models.DecimalField(decimal_places=0, max_digits=2)),
                ('subject3', models.DecimalField(decimal_places=0, max_digits=2)),
                ('subject4', models.DecimalField(decimal_places=0, max_digits=2)),
                ('subject5', models.DecimalField(decimal_places=0, max_digits=2)),
                ('subject6', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
    ]