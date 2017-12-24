# Generated by Django 2.0 on 2017-12-24 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
        ('criteria', '0002_auto_20171224_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriaScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('notes', models.TextField(blank=True)),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criteria.Criteria')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Tool')),
            ],
        ),
    ]
