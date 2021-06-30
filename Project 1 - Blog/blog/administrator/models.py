from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=15,
        unique=True
    )

    description = models.TextField(
        max_length=500
    )

    color = models.CharField(
        max_length=10,
        default='#000000'
    )

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Pending', 'Pending Review'),
        ('Published', 'Published'),
    )

    id = models.BigAutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )

    slug = models.SlugField(
        verbose_name='Slug',
        unique=True
    )

    description = models.CharField(
        max_length=150,
        verbose_name='Meta Description'
    )

    featured_image = models.ImageField(
        upload_to = 'posts'
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name='Category'
    )

    body = models.TextField(
        verbose_name='Content'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    published_on = models.DateTimeField(
        verbose_name='Published On'
    )

    status = models.CharField(
        choices=STATUS,
        verbose_name='Status',
        max_length=20
    )