from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UseGroup(models.Model):
    group = models.CharField(max_length=7)
    description = models.CharField(max_length=55)


class TypeOfConstruction(models.Model):
    type = models.CharField(max_length=7)
    description = models.CharField(max_length=55)


class BP(models.Model):
    number = models.CharField(max_length=55, unique = True)
    valuation = models.DecimalField(
        max_digits=15, decimal_places=2, default=2000)
    use_group = models.ForeignKey(UseGroup, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_use")
    type_of_construction = models.ForeignKey(TypeOfConstruction, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_type_of_const")

    owner_builder_form = models.BooleanField(
        "Owner-Builder Form Acknowledgement", default=False)
    owner_rep_form = models.BooleanField(
        "Owner's Authorization of a Representative", default=False)
    CSLB_Forms = models.BooleanField(
        "CSLB License Verification", default=False)
    employee_authorization = models.BooleanField(
        "CSLB Licensed Employer Authorization of Employee to Pull Permits", default=False)
    
    finaled = models.DateTimeField(null="True", blank=True)
    finaled_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_finaler")
    expiration_date = models.DateTimeField(null=True, blank=True,
        help_text="""
        Building Permits expire 12 months after 
        they are issued, except that they are 
        extended for specific reasons in 
        accordance with County policy.
        """)
    expiration_set_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_expirer")
    issued = models.DateTimeField(null=True, blank=True)
    issued_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_issuer")
    approved = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_approver")
    received = models.DateTimeField(null=True, blank=True)
    received_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_receiver")
   
    def apply():
        # run_application_checks()
        # add_inspections()
        # add_reviews()
        # add_fees()
        pass

    def pay_application_fees():
        pass

    def receive(self, request):
        self.number = self.set_number()
        self.division = "Building"
        self.status = "Under Review"
        self.forms.add(id = [1, 2, 3, 4]) # Air District, EH, IWM, Fire District
        self.reviews.add(id = 9) # Bldg Demolition
        self.inspections.add(id = [17, 18, 31]) # Demo 1, Demo 2, Permit Final
        self.fees.add(id = [601, 603, 608, 610, 613, 614, 644, 645, 810])
        self.received = timezone.now()
        self.received_by = request.user.id
        self.expiration_date = self.received + timezone.timedelta(days = 365)
        # run_application_checks()
        # prepare_documents()
        # send_application_receipt_email()

    def approve(self, request):
        # run_issuance_checks()
        # prepare_approval_documents()
        # prepare_issuance_documents()
        self.status = "Issued"
        self.approved = timezone.now()
        self.approved_by = request.user.id
        self.save()
        # send_approval_email()

    def pay_issuance_fees():
        pass

    def issue(self, request):
        self.issued = timezone.now()
        self.issued_by = request.user.id
        self.expiration_date = timezone.now() + timezone.timedelta(days=365)
        self.expiration_set_by = request.user.id
        self.save()

    def extend_expiration(self, request, extra_days=180):
        a = self.expiration_date + timezone.timedelta(extra_days)
        b = self.issued + timezone.timedelta(days=1095)
        self.expiration_date = min(a, b)
        self.expiration_set_by = request.user.id
        self.save()
    
    def expire(self):
        self.status = "Expired"
        self.save()

    def reinstate(self):
        if self.was_issued:
            self.status = "Issued"
        else:
            self.status = "Under Review"

    def suspend(self):
        self.status = "Suspended"
        # add_suspended_tag()
        self.save()

    def final(self, request):
        # run_final_checks()
        # prepare_occupancy_documents()
        self.status = "Finaled"
        self.finaled = timezone.now()
        self.finaled_by = request.user.id
        self.save()
        # send_occupancy_email()

    def __str__(self) -> str:
        return self.number
    
    class Meta:
        ordering = ["number"]
        verbose_name = "BP"
        verbose_name_plural = "BP's"
