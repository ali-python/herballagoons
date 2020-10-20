from __future__ import unicode_literals
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

class Registration(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	father_name = models.CharField(max_length=200, null=True, blank=True)
	cnic = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	education = models.CharField(max_length=100, null=True, blank=True)
	package = models.CharField(max_length=100, null=True, blank=True)
	course_study = models.CharField(max_length=100, null=True, blank=True)
	mobile_no = models.CharField(max_length=13, blank=True, null=True)
	date_of_birth = models.DateField(blank=True, null=True)
	status_not_sure = models.CharField(max_length=13, blank=True, null=True)
	status_intro_class = models.CharField(max_length=13, blank=True, null=True)
	message  = models.TextField(max_length=512, blank=True, null=True)