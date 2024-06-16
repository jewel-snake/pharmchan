from django.db import models
from django.contrib.auth.models import User
import compmodel.models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FutureSolution(models.Model):
    class StatusChoises(models.TextChoises):
        READY = "R",_("READY")
        COMPUTING = "C",_("COMPUTING")
        QUEUED = "Q",_("QUEUED")
        FAILED = "F",_("FAILED")
    
    #owner = models.ForeignKey(User,null=False)
    
    model = models.ForeignKey(compmodel.models.CompModel,null=False)
    dataset = models.ForeignKey(compmodel.models.Dataset)
    status = models.TextField(max_length=1,choises=StatusChoises,default=StatusChoises.QUEUED)
    result = models.ForeignKey(compmodel.models.Solution,null=True)
