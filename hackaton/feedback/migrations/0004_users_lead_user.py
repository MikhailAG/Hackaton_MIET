# Generated by Django 4.2.6 on 2023-10-21 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_delete_aboba_feedbacks_from_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='lead_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.users'),
        ),
    ]
