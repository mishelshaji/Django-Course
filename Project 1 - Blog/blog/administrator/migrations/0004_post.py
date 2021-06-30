# Generated by Django 3.2.3 on 2021-06-18 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_alter_category_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.CharField(max_length=150, verbose_name='Meta Description')),
                ('featured_image', models.ImageField(upload_to='posts')),
                ('body', models.TextField(verbose_name='Content')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('published_on', models.DateTimeField(verbose_name='Published On')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Pending', 'Pending Review'), ('Published', 'Published')], max_length=20, verbose_name='Status')),
                ('catgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.category', verbose_name='Category')),
            ],
        ),
    ]