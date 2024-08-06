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
        blank=True,
    )
    review_type = models.CharField(max_length=30)
    days_cycle1 = models.PositiveSmallIntegerField(default=15)
    days_cycle2 = models.PositiveSmallIntegerField(default=5)
    review_checklist = models.TextField("Review Checklist", blank=True)
    """ Record types that will default to include this review. """

    def __str__(self) -> str:
        return self.review_type

    class Meta:
        ordering = ["review_type"]
        verbose_name = "Review Type"
        verbose_name_plural = "Review Types"


class ReviewCycleResult(models.Model):
    result = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    causes_review_status = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.result

    class Meta:
        ordering = ["result"]
        verbose_name = "Review Cycle Result Option"
        verbose_name_plural = "Review Cycle Result Options"


class ReviewCycle(models.Model):
    cycle = models.PositiveSmallIntegerField(default=1)
    result = models.CharField(max_length=55)
    reviewer = models.CharField(max_length=255, default="unassigned")
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

    class Meta:
        ordering = ["cycle"]
        verbose_name = "Review Cycle"
        verbose_name_plural = "Review Cycles"


class ReviewStatus(models.Model):
    status = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.status

    class Meta:
        ordering = ["status"]
        verbose_name = "Review Status Option"
        verbose_name_plural = "Review Status Options"


class Review(models.Model):
    type_link = models.ForeignKey(
        ReviewType, on_delete=models.PROTECT, related_name="review"
    )
    record = models.CharField(max_length=55, blank=True)
    type = models.CharField(max_length=55, blank=True)
    status = models.CharField(max_length=55)
    notes = models.TextField(max_length=255)
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self) -> str:
        return f"{self.record.number} {self.type.review_type}"

    class Meta:
        ordering = ["record", "type", "status"]
