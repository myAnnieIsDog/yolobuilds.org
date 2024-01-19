from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):      
    tag = models.CharField(max_length=100, blank = True, unique=True)
    policy = models.TextField(max_length=255, blank = True)

    def __str__(self) -> str:
        return self.tag   

    class Meta:
        ordering = ["tag"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Restriction(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.PROTECT, blank = True, null = True)
    policy = models.CharField(max_length = 255, null = True, blank = True)

    lock = models.BooleanField(
        "Lock this record?", default=False)
    lock_related = models.BooleanField(
        "Lock related records?", default=False)
    alert = models.BooleanField(
        "Popup notification on this record?", default=True)
    alert_related = models.BooleanField(
        "Popup notification on related records?", default=False)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return self.tag.tag
    
    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id",],),]
        ordering = ["tag"]
        verbose_name = "Restriction"
        verbose_name_plural = "Restrictions"
