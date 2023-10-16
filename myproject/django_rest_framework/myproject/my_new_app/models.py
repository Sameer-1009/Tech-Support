from django.db import models
# from .models import MyModel


# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField (auto_now_add=True)
    
    # FULL_TIME_POSITION = models.CharField(max_length=50)
    # PREVAILING_WAGE = models.CharField(max_length=50)
    # PW_UNIT_OF_PAY = models.CharField(max_length=50)
    # PW_WAGE_SOURCE = models.CharField(max_length=50)
    # PW_SOURCE_YEAR = models.CharField(max_length=50)
    # PW_SOURCE_OTHER = models.CharField(max_length=50)

    WAGE_RATE_OF_PAY_FROM = models.CharField(max_length=50)
    # WAGE_RATE_OF_PAY_TO = models.CharField(max_length=50)
    WAGE_UNIT_OF_PAY = models.CharField(max_length=50)

    # H1B_DEPENDENT = models.CharField(max_length=50)
    # WILLFUL_VIOLATOR = models.CharField(max_length=50)
    # WORKSITE_CITY = models.CharField(max_length=50)
    # WORKSITE_COUNTY = models.CharField(max_length=50)
    # WORKSITE_STATE = models.CharField(max_length=50)
    # WORKSITE_POSTAL_CODE = models.CharField(max_length=50)
    # ORIGINAL_CERT_DATE = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
