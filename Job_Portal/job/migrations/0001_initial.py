# Generated by Django 3.0.8 on 2020-07-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=40)),
                ('caddr', models.CharField(max_length=50)),
                ('cdetails', models.CharField(max_length=200)),
                ('ctype', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=30)),
                ('jobdesc', models.CharField(max_length=50)),
                ('jobsalary', models.FloatField()),
                ('jobopno', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField()),
                ('aname', models.CharField(max_length=30)),
                ('aphone', models.IntegerField()),
                ('abranch', models.CharField(max_length=30)),
                ('askills', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Company')),
            ],
        ),
    ]