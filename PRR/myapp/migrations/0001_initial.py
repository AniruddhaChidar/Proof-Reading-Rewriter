# Generated by Django 2.2.6 on 2019-11-24 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Sentence')),
            ],
        ),
        migrations.CreateModel(
            name='CorWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corWord', models.CharField(max_length=50)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Word')),
            ],
        ),
    ]