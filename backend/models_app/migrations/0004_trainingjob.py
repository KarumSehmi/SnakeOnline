# Generated by Django 5.0.6 on 2024-11-24 17:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0003_alter_modelentry_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingJob',
            fields=[
                ('job_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('learning_rate', models.FloatField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('RUNNING', 'Running'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='PENDING', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trained_model', models.FileField(blank=True, null=True, upload_to='trained_models/')),
            ],
        ),
    ]
