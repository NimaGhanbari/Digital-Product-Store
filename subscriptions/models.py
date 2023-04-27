from django.db import models
from django.utils.translation import ugettext_lazy as _


from users.models import User
from utils.validators import validate_sku

class Package(models.Model):
    title = models.CharField(verbose_name=_("title"),max_length=50)
    sku = models.CharField(_('stock keeping unit'),max_length=20,validators=[validate_sku])
    description = models.TextField(verbose_name=_("description"),blank=True)
    avatar = models.ImageField(verbose_name=_("avatar"),blank=True,upload_to='packages/')
    is_enable = models.BooleanField(verbose_name=_("is enable"),default=True)
    price = models.PositiveIntegerField(_("price"))
    duration = models.DurationField(_('duraton'),blank=True,null=True)
    create_time = models.DateTimeField(verbose_name=_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_("update time"),auto_now=True)

    class Meta:
        db_table = "packages"
        verbose_name = _("package")
        verbose_name_plural = _("packages")
        
    def __str__(self):
        return self.title
    
    
class Subscription(models.Model):
    user = models.ForeignKey('users.User',related_name= '%(class)s', on_delete = models.CASCADE)
    package = models.ForeignKey(Package,related_name='%(class)s', on_delete = models.CASCADE)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    expaire_time = models.DateTimeField(_('expaire time'),blank=True,null=True)
    
    
    class Meta:
        db_table = "Subscriptions"
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")
    
    
    