# Generated by Django 4.1.4 on 2022-12-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rating_post_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('tech', 'Tech'), ('education', 'Education'), ('general', 'General')], default='general', max_length=20)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='post_categories', to='blog.category'),
        ),
    ]