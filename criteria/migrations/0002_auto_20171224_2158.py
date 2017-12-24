# Generated by Django 2.0 on 2017-12-24 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criteria.Criteria'),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
