# Generated by Django 4.2.4 on 2023-08-17 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('headquarters', models.CharField(max_length=255)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('banner', models.ImageField(upload_to='banners/')),
                ('headline', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('certificate_image', models.FileField(upload_to='certificate/')),
                ('certificate_links', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endorsement_count', models.PositiveIntegerField(default=0)),
                ('User_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.userprofile')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.skill')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill',
            field=models.ManyToManyField(blank=True, through='job.UserSkill', to='job.skill'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(default='remote', max_length=200)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('application_deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.company')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_image', models.ImageField(upload_to='companyImage/')),
                ('location', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.BooleanField(default='present')),
                ('User_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.industry'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('cover_latter', models.TextField()),
                ('resume', models.FileField(upload_to='Applications/')),
                ('User_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.userprofile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]