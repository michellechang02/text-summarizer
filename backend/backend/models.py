from django.db import models

class TextSummary(models.Model):
    original_text = models.TextField()
    summarized_text = models.TextField()
    class Meta:
        app_label = 'backend'