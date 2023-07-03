from django.db import models
from django_extensions.db.models import TimeStampedModel


def brand_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'static/brand_{0}/{1}'.format(instance.name, filename)


class Brand(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.FileField(upload_to=brand_directory_path)
    description = models.CharField(max_length=255, blank=True, null=True)
    product_description = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    numbers_of_daily_post = models.IntegerField(blank=True, null=True)


class BrandPostTemplate(TimeStampedModel):
    """
    This is the template the Brand wants his post in or fashioned against
        Post Template Table:
        brand_id (Foreign Key referencing the Brand table)
        date
        head
        body
        close
        character_id (Foreign Key referencing the Character table)
        topic_id (Foreign Key referencing the Post Topic table)

    """
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_post_templates')
    header = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    footer = models.CharField(max_length=255, blank=True, null=True)


class BrandPostTemplate(TimeStampedModel):
    """
    This is the template the Brand wants his post in or fashioned against
        Post Template Table:
        brand_id (Foreign Key referencing the Brand table)
        date
        head
        body
        close
        character_id (Foreign Key referencing the Character table)
        topic_id (Foreign Key referencing the Post Topic table)

    """
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_post_templates')
    header = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    footer = models.CharField(max_length=255, blank=True, null=True)
