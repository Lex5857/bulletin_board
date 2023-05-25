# Generated by Django 4.2.1 on 2023-05-20 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ads_author_alter_responses_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ads.ads')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
            ],
        ),
    ]
