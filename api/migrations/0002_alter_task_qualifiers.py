# Generated by Django 4.0.4 on 2022-05-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='qualifiers',
            field=models.ManyToManyField(null=True, related_name='qualified_for', to='api.person'),
        ),
    ]