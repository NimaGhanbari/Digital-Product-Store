from django.db import models
#این ایمپورت پایین برای کار های ترنسلیت کردن میباشد
from django.utils.translation import ugettext_lazy as _


#در این قسمت ما برای کتگوری در دیتابیس فضا رزرو میکنیم

class Category(models.Model):
    title = models.CharField(verbose_name=_("title"),max_length=50)
    description = models.TextField(verbose_name=_("description"),blank=True)
    avatar = models.ImageField(verbose_name=_("avatar"),blank=True,upload_to='categories')
    is_enable = models.BooleanField(verbose_name=_("is enable"),default=True)
    parent = models.ForeignKey('self',verbose_name=_("parent"),blank=True,null=True, on_delete= models.CASCADE)
    create_time = models.DateTimeField(verbose_name=_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_("update time"),auto_now=True)
    
    class Meta:
        #اسم تیبلی که برای کاتگوری در دیتابیس در نظر گرفته میشود است
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        
    def __str__(self):
        return self.title
    
#در این قسمت ما برای فقط فیلم و اطلاعات شخصی فیلم در دیتابیس فضا رزرو کردیم 
   
class Products(models.Model):
    title = models.CharField(_("title"),max_length=50)
    description = models.TextField(_("description"),blank=True)
    avatar = models.ImageField(_("avatar"),blank=True,upload_to='products/')
    categories = models.ManyToManyField('Category',verbose_name=_("categories"),blank=True)
    is_enable = models.BooleanField(_("is enable"),default=True)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "products"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        
    def __str__(self):
        return self.title
        
#ما برای اینکه هر فیلم میتواند چندین تا قسمت داشته باشد یک دیتابیس براش در نظر میگیریم که کار دخیرهسازی آسان تر شود 
#وهر فایل که آپلود کردیم را به یک محصول فارنکی میکنیم      
class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO,_('audio')),
        (FILE_VIDEO,_('video')),
        (FILE_PDF,_('pdf'))
    )
    title = models.CharField(_("title"),max_length=50)
    file_type =models.PositiveSmallIntegerField(_("file type"), choices=FILE_TYPES)
    fil = models.FileField(_("file"),upload_to="files/%Y/%m/%d/")
    product = models.ForeignKey('Products',verbose_name=_("product"), on_delete=models.CASCADE)
    is_enable = models.BooleanField(_("is enable"),default=True)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "files"
        verbose_name = _("file")
        verbose_name_plural = _("files")
        
    def __str__(self):
        return self.title
        
    