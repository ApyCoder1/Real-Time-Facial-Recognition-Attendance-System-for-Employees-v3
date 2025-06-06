# Generated by Django 5.0.7 on 2025-03-08 06:55

import app1.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Give a name to this camera configuration', max_length=100, unique=True)),
                ('camera_source', models.CharField(help_text='Camera index (0 for default webcam or RTSP/HTTP URL for IP camera)', max_length=255)),
                ('threshold', models.FloatField(default=0.6, help_text='Face recognition confidence threshold')),
                ('location', models.CharField(default='Gate 1', help_text='Location of the camera (optional)', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Course name', max_length=255, unique=True)),
                ('description', models.TextField(help_text='Course description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host', models.CharField(max_length=255)),
                ('email_port', models.IntegerField()),
                ('email_use_tls', models.BooleanField(default=True)),
                ('email_host_user', models.CharField(max_length=255)),
                ('email_host_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Semester name (e.g., Fall 2024)', max_length=100, unique=True)),
                ('start_date', models.DateField(help_text='Start date of the semester')),
                ('end_date', models.DateField(help_text='End date of the semester')),
                ('description', models.TextField(blank=True, help_text='Brief description of the semester', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('face_embedding', models.JSONField(blank=True, null=True)),
                ('authorized', models.BooleanField(default=False)),
                ('roll_no', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('joining_date', models.DateField()),
                ('mother_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('department', models.ManyToManyField(related_name='students', to='app1.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employe_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('check_in_time', models.DateTimeField(blank=True, null=True)),
                ('check_out_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], default='Absent', max_length=20)),
                ('is_late', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('paid', models.BooleanField(default=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('added_month', models.PositiveIntegerField()),
                ('added_year', models.PositiveIntegerField()),
                ('advance_payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Partial', 'Partial')], default='Pending', max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='app1.employe')),
            ],
        ),
        migrations.CreateModel(
            name='AdvancePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advance_payments', to='app1.fee')),
            ],
        ),
        migrations.CreateModel(
            name='FeePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Bank Transfer', 'Bank Transfer')], default='Cash', max_length=15)),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='app1.fee')),
            ],
        ),
        migrations.CreateModel(
            name='LateCheckInPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(default=app1.models.LateCheckInPolicy.get_default_start_time)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='late_checkin_policy', to='app1.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='Leave start date')),
                ('end_date', models.DateField(help_text='Leave end date')),
                ('reason', models.TextField(blank=True, help_text='Reason for the leave', null=True)),
                ('approved', models.BooleanField(default=False, help_text='Whether the leave has been approved')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves', to='app1.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the lesson', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Brief description of the lesson', null=True)),
                ('youtube_embed_link', models.URLField(blank=True, help_text='Embed link for YouTube video', null=True)),
                ('youtube_video_url', models.URLField(blank=True, help_text='Direct YouTube video URL', null=True)),
                ('video_file', models.FileField(blank=True, help_text='Upload video file for the lesson', null=True, upload_to='lessons/videos/')),
                ('lesson_notes', models.TextField(blank=True, help_text='Additional notes or materials for the lesson', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='app1.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app1.session'),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_time_threshold', models.IntegerField(default=60)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='app1.employe')),
            ],
        ),
    ]
