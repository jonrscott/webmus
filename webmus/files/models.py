from django.db import models


class UploadedFileTag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class UploadedFile(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(UploadedFileTag, blank=True, null=True)
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='fileimages', blank=True)
    data = models.FileField(upload_to='files')

    def __unicode__(self):
        if self.tag:
            return "%s/%s" % (self.tag.name, self.filename)
        return self.filename
