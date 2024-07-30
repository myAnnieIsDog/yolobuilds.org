from django.contrib.auth.models import User
from django.db import models


class ReviewGroup(models.Model):
    group = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.group
    
    class Meta:
        ordering = ["group"]
        verbose_name = "Review Group"
        verbose_name_plural = "Review Groups"
        
class ReviewType(models.Model): 
    default_reviewer = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name="default_reviewer_for", 
        null=True, 
        blank=True)
    review_type = models.CharField(max_length=30)
    days_cycle1 = models.PositiveSmallIntegerField(default=15)
    days_cycle2 = models.PositiveSmallIntegerField(default=5)
    review_checklist = models.TextField("Review Checklist", blank=True)
    """ Record types that will default to include this review. """  

    def __str__(self) -> str:
        return self.review_type

    class Meta():
        ordering = ["review_type"]
        verbose_name = "Review Type"
        verbose_name_plural = "Review Types"
