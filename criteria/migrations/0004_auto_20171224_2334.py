# Generated by Django 2.0 on 2017-12-24 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_tool_scores'),
        ('criteria', '0003_criteriascore'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='criteriascore',
            unique_together={('criteria', 'tool')},
        ),
    ]
