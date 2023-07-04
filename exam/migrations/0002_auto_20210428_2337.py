# Generated by Django 3.1.7 on 2021-04-28 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210423_0433'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ch1',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='ch2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='ch3',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='ch4',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='exam',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.teacherprofile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]
