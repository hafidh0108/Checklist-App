# Generated by Django 4.1.3 on 2022-11-17 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('checklistid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=255)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.checklist')),
            ],
        ),
    ]
