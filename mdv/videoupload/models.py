from django.db import models

class VideoFragment(models.Model):
    vidfile = models.FileField(verbose_name="Video file",
                               upload_to="videofragments")
    prev_video = models.ForeignKey('self',
                                   related_name="+",
                                   null=True,
                                   blank=True) 
    next_video = models.ForeignKey('self',
                                  related_name="+",
                                  null=True,
                                  blank=True) 
    link = models.URLField()
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.description
