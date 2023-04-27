from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.validators import validate_phone_number


class Gateway(models.Model):
    title = models.CharField(verbose_name=_("title"),max_length=50)
    description = models.TextField(verbose_name=_("description"),blank=True)
    avatar = models.ImageField(verbose_name=_("avatar"),blank=True,upload_to='Gateways/')
    is_enable = models.BooleanField(verbose_name=_("is enable"),default=True)
    create_time = models.DateTimeField(verbose_name=_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_("update time"),auto_now=True)
    
    class Meta:
        #اسم تیبلی که برای پکیج در دیتابیس در نظر گرفته میشود است
        db_table = "Gateways"
        verbose_name = _("Gateway")
        verbose_name_plural = _("Gateways")
        
         
class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID,_('void')),
        (STATUS_PAID,_('paid')),
        (STATUS_ERROR,_('error')),
        (STATUS_CANCELED,_('canceled')),
        (STATUS_REFUNDED,_('refunded'))
    )
    
    STATUS_TRANSLATIONS = {
        STATUS_VOID : _('payment could not be processed'),
        STATUS_PAID : _('payment succesfull'),
        STATUS_ERROR : _('payment has encontered an error . our technical team will check the'),
        STATUS_CANCELED : _('payment canceled by user.'),
        STATUS_REFUNDED :_('this payment has beed refunded')
    }
    
    
    user = models.ForeignKey('users.User',verbose_name=_('user'),related_name= '%(class)s', on_delete= models.CASCADE)
    package = models.ForeignKey('subscriptions.Package',verbose_name=_('package'),related_name='%(class)s', on_delete = models.CASCADE)
    gateway = models.ForeignKey(Gateway,related_name='%(class)s', on_delete = models.CASCADE)
    price = models.PositiveIntegerField(_("price"),default = 0)
    status = models.PositiveSmallIntegerField(verbose_name=_('status'),choices=STATUS_CHOICES,default=STATUS_VOID)
    device_uuid = models.CharField(max_length=40,blank=True)
    phone_number = models.BigIntegerField(validators=[validate_phone_number])
    #شماره پیگیری
    consumed_code = models.PositiveIntegerField(_("consumed refrence code"),null =True,db_index = True)
    create_time = models.DateTimeField(verbose_name=_("create time"),auto_now_add=True,db_index=True)
    update_time = models.DateTimeField(verbose_name=_("update time"),auto_now=True)
    
    class Meta:
        #اسم تیبلی که برای پکیج در دیتابیس در نظر گرفته میشود است
        db_table = "Payments"
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
    