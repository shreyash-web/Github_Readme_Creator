# Generated by Django 4.1.1 on 2022-09-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0031_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_on',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='personal_readme',
            name='add_ons',
        ),
        migrations.AddField(
            model_name='personal_readme',
            name='add_ons',
            field=models.ManyToManyField(blank=True, related_name='add_on', to='personal_readme.add_on'),
        ),
    ]