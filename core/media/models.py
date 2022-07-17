from django.db import models

class Media(models.Model):
    file = models.FileField(upload_to="files", blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.pk}"