from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class User(AbstractUser):

	DESIGNATIONS = [
		('PM', 'Project Manager'),
		('SE', 'System Engineer'),
		('SH', 'Sub-System Head'),
		('TM', 'Team Member')
	]
	dept = models.CharField("Department", blank=True, max_length=255)
	designation = models.CharField("Designation", max_length=2, choices=DESIGNATIONS)
	mobileNumber = models.CharField("Mobile Number", blank=True, max_length=255)
	degree = models.CharField("Degree", blank=True, max_length=255)
	year = models.IntegerField("Year", blank=True, default = 1)
	alternateEmail = models.EmailField("Alternate Email", blank=True)
	subSystem = models.CharField("Name of subsystem", blank=True, max_length=255)
	presentSystem = models.CharField("Name of present system", blank=True, max_length=255)
	Experience = models.IntegerField("Experience", blank=True, default = 0)
	topicWorkingOn = models.CharField("Topic working on", blank=True, max_length=255)
	profilePic =models.URLField("Profile Picture", blank=True)
	hobbies = models.TextField("Hobbies", blank=True)
	softwaresKnown = models.TextField("Softwares Known", blank=True)
	

	def __str__(self):
		return "@{}".format(self.username)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
