# Generated by Django 4.0.1 on 2022-01-17 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_idx', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(blank=True, max_length=120)),
                ('ans1', models.TextField(null=True)),
                ('ans2', models.TextField(null=True)),
                ('ans3', models.TextField(null=True)),
                ('ans4', models.TextField(null=True)),
                ('statud', models.CharField(default='y', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_idx', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.IntegerField()),
                ('survey_idx', models.ForeignKey(db_column='survey_idx', on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='survey.survey')),
            ],
        ),
    ]
