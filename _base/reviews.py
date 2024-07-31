from django.db import models

from .bp import BP
from .review_types import ReviewType


class ReviewStatus(models.Model): 
    status = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.status

    class Meta():
        ordering = ["status"]
        verbose_name = "Review Status Option"
        verbose_name_plural = "Review Status Options"


class Review(models.Model):
    record = models.ForeignKey(BP, on_delete=models.PROTECT, related_name="review") 
    type = models.ForeignKey(ReviewType, on_delete=models.PROTECT, related_name="review")   
    status = models.ForeignKey(ReviewStatus, on_delete=models.PROTECT)
    coa = models.TextField("Conditions of Approval", max_length=255)  
   
    # Fee Study
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self) -> str:
        return f"{self.record.number} {self.type.review_type}"

    class Meta:
        ordering = ["record", "type", "status"]


class ReviewCycleResult(models.Model):
    result = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    causes_review_status = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.result
    
    class Meta():
        ordering = ["result"]
        verbose_name = "Review Cycle Result Option"
        verbose_name_plural = "Review Cycle Result Options"


class ReviewCycle(models.Model):
    """ Inherits Label, Description, Created, Modified """
    # Fields for ReviewCycle.objects.filter(parent_review=review)
    review = models.ForeignKey(Review, on_delete=models.PROTECT, related_name="cycle")
    
    # Public fields
    cycle = models.PositiveSmallIntegerField(default=1)
    result = models.ForeignKey(ReviewCycleResult, on_delete=models.PROTECT, default="In Progress")
    reviewer = models.CharField(max_length=100, null=True)
    completed_date = models.DateTimeField(null=True)
    due = models.DateTimeField(null=True)
    sent = models.DateTimeField(null=True)
    notes = models.TextField(max_length=255)

    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)
    days_until_due = models.DurationField(null=True)
    age = models.DurationField(null=True)
    
    days_allotted = models.DurationField(null=True)

    def __str__(self) -> str:
        return f"{self.review} Review, Cycle {self.cycle}"
    
    class Meta():
        ordering = ["review"]
        verbose_name = "Review Cycle"
        verbose_name_plural = "Review Cycles"
