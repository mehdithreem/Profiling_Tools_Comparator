# Generated by Django 2.0 on 2017-12-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0003_criteriascore'),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='scores',
            field=models.ManyToManyField(through='criteria.CriteriaScore', to='criteria.Criteria'),
        ),
    ]