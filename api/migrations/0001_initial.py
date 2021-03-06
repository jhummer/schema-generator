# Generated by Django 4.0.4 on 2022-05-02 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('meeting_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('assignee_count', models.IntegerField()),
                ('qualifiers', models.ManyToManyField(related_name='qualified_for', to='api.person')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTaskPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='api.meeting')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task')),
            ],
            options={
                'ordering': ('meeting__date',),
            },
        ),
        migrations.AddField(
            model_name='meeting',
            name='assignees',
            field=models.ManyToManyField(through='api.MeetingTaskPerson', to='api.person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='task',
            field=models.ManyToManyField(to='api.task'),
        ),
    ]
