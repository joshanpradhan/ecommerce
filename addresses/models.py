from django.db import models

from billing.models import BillingProfile
# Create your models here.
ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),

)


class Address(models.Model):
    billing_profile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length=120, blank=False, null=False)
    address_line_2 = models.CharField(max_length=120)
    city = models.CharField(
        max_length=120, default="Kathmandu", blank=False, null=False)
    mobile_number = models.CharField(max_length=120, blank=False, null=False)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        context = {
            "address_line_1" : self.address_line_1,
            "address_line_2" : self.address_line_2 or "Not Available",
            "city" : self.city,
            "mobile_number" : self.mobile_number,
            "postal_code" : self.postal_code or "Not Available",
        }
        # return "{address_line_1}\n,{address_line_2}\n,{city}\n,{mobile_number}\n,{postal_code}\n".format(
        # address_line_1=self.address_line_1,
        # address_line_2=self.address_line_2 or "Not Available",
        # city=self.city,
        # mobile_number=self.mobile_number,
        # postal_code=self.postal_code or "Not Available",

        return context
