# Generated by Django 4.2.1 on 2023-05-28 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignee',
            fields=[
                ('assigneeID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('assigneeName', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('taskName', models.CharField(max_length=40)),
                ('taskDesc', models.TextField(blank=True, null=True)),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('dueDate', models.DateTimeField()),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('taskStatus', models.CharField(max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('assignDate', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.assignee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.task')),
            ],
        ),
        migrations.AddField(
            model_name='assignee',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.project'),
        ),
    ]
