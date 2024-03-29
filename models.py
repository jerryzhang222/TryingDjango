from django.db import models

# Create your models here.

class Join(models.Model):
    email = models.EmailField()
    ref_id = models.CharField(max_length=120, default ='ABC')
    file = models.FileField(default = 'http://www.hooyou.com/services/contracts/I539B1.pdf')
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return self.email
        
    class Meta:
        unique_together = ("email", "ref_id")