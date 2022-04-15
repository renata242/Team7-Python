from django.db import migrations, models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class Medicaments(models.Model):

    # field to store article category
    meds_category = models.CharField(max_length=200)

    # field to store artcile name
    meds_name = models.CharField(max_length=200)

    # field to store article's text
    meds_description = models.TextField()

    # field to store article's date
    meds_packing_date = models.DateTimeField(auto_now_add=True)

    # article rating field
    meds_rating = models.FloatField(default=0.0)

    # field to store link to editor (foreign key, M to 1 relationship)
    meds_manufacturer = models.CharField(max_length=200)

    # magic method to retrieve str value of article name and
    # return it when the method is called
    def __str__(self) -> str:
        return self.meds_name

