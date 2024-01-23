from django.contrib.auth import get_user_model
from django.db import models


class RequestStatusChoices(models.TextChoices):
    POSTED = 'posted', 'ارسال شده'
    FAILED_SUPERVISOR = 'failed_supervisor', 'رد شده توسط سرپرست'
    ACCEPTED_SUPERVISOR = 'accepted_supervisor', 'تایید شده توسط سرپرست'
    FAILED_MANAGER = 'failed_manager', 'رد شده توسط مدیر'
    ACCEPTED_MANAGER = 'accepted_manager', 'تایید شده توسط مدیر'


class Requests(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=64, choices=RequestStatusChoices.choices, default=RequestStatusChoices.POSTED)
    created_by = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.created_by.username}'

