from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Task(models.Model):
    name = models.CharField(
        "Task description",
        max_length=100,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
    )
    estimated_duration = models.IntegerField(
        "Estimated duration (integer field, decide on a unit yourself per your use-case)",
        blank=True,
    )
    importance = models.IntegerField(
        "Approximate importance, e.g. how much you would pay to delegate it",
        blank=True,
        )
    due_date = models.DateField(
        blank=True,
    )
    done = models.BooleanField(
        default=False,
    )

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})