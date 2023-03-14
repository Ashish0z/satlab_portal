from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(defaults={'username': 'deleted1', 'password': 'deleted'})[0]

class Form(models.Model):

    class Meta:
        abstract = True
    
    STATUS = [
        ('0', 'Pending'),
        ('1', 'Approved'),
        ('2', 'Rejected'),
    ]

    SATLAB_USER = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user)
    )
    Comments = models.TextField()
    Date = models.DateField()

    Status = models.CharField(max_length=1, choices=STATUS, default='0',)


class LeaveForm(Form):

    MEETING_TYPE = [
        ('0', 'General'),
        ('1', 'SubSystem'),
        ('2', 'Worksession'),
        ('3', 'System'),
        ('4', 'Other'),
    ]

    LeaveID = models.AutoField(primary_key=True)
    MeetingDate = models.DateField()
    MeetingType = models.CharField(max_length=1, choices=MEETING_TYPE, default='4',)
    Reason = models.TextField()


class FineSheetForm(Form):

    MEETING_TYPE = [
        ('0', 'General'),
        ('1', 'SubSystem'),
        ('2', 'Worksession'),
        ('3', 'System'),
        ('4', 'Other'),
    ]
    STATUS = [
        ('0', 'Unpaid'),
        ('1', 'Paid'),
        ('2', 'Pending_Verification')
    ]

    FineSheetID = models.AutoField(primary_key=True)
    FineSheetAmount = models.IntegerField()
    FineSheetReason = models.TextField()
    MeetingDate = models.DateField()
    MeetingType = models.CharField(max_length=1, choices=MEETING_TYPE, default='4',)
    Status = models.CharField(max_length=1, choices=STATUS, default='2')
    MembersFined = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='MembersFined'
    )

class InventoryForm(Form):

    EquipmentID = models.AutoField(primary_key=True)
    EquipmentName = models.CharField(max_length=255)
    EquipmentDescription = models.TextField()
    EquipmentQuantity = models.IntegerField()
    EquipmentType = models.CharField(max_length=255)
    EquipmentPrice = models.IntegerField()
    Purpose = models.TextField()
    VendorDetails = models.TextField()
    ProjectName = models.CharField(max_length=255)
    SubSystemName = models.CharField(max_length=255)
