from django.db import models
class PPT(models.Model):
    ppt = models.FileField(upload_to="ppt/")
    ppt_modified = models.FileField(upload_to="ppt_modified/",blank=True)
    ppt_name = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=100,default="loading")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PPT {self.pk} - {self.status}"
    




