# Generated by Django 4.0.5 on 2023-07-01 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BoredAPIApp', '0003_remove_activity_activity_type_remove_user_user_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='key',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='link',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='price',
        ),
        migrations.RemoveField(
            model_name='user',
            name='activities',
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='BoredAPIApp.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='activity_type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_view', models.BooleanField(default=False)),
                ('can_delete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BoredAPIApp.user')),
            ],
        ),
    ]
