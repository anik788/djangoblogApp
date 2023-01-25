# Generated by Django 4.1.4 on 2022-12-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('tech', 'Tech'), ('education', 'Education'), ('sports', 'Sports'), ('general', 'General')], default='general', max_length=20),
        ),
    ]