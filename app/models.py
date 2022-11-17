from django.db import models

# Create your models here.
class Checklist(models.Model):
    checklistid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ChecklistItem(models.Model):
    checklist = models.ForeignKey('app.Checklist', on_delete=models.CASCADE)
    itemName = models.CharField(max_length=255)

    def __str__(self):
        return self.itemName