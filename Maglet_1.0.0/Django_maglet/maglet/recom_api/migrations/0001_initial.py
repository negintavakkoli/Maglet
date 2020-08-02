# Generated by Django 3.0.3 on 2020-08-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='journal_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_id', models.IntegerField()),
                ('title', models.CharField(max_length=200, null=True)),
                ('owner', models.CharField(max_length=200, null=True)),
                ('release_period', models.CharField(max_length=200, null=True)),
                ('general_subject', models.CharField(max_length=200, null=True)),
                ('exclusive_subject', models.CharField(max_length=200, null=True)),
                ('url', models.URLField(null=True)),
                ('cover_address', models.CharField(max_length=200, null=True)),
                ('organizer', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]