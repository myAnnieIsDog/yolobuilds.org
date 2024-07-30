from django.db import models

from .profiles import Profile


class ContactType(models.Model):
    role = models.CharField(max_length=55)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.role

    class Meta():
        ordering = ["description"]
        verbose_name = "Contact Type"
        verbose_name_plural = "Contacts Types"


class Contact(models.Model):
    contact = models.ForeignKey(Profile, on_delete=models.PROTECT)
    contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.contact} is the {self.role} on {self.record}."
    
    class Meta():
        ordering = ["contact"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
