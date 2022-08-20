from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from post.helper import seo
USER_MODEL = settings.AUTH_USER_MODEL

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), null=True, max_length=100, unique=False)
    first_name = models.CharField(_('first name'), max_length=255, blank=True, )
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    image=models.ImageField(_('Sekil elave et'),null=True)

    email = models.EmailField(_('email address'), unique=True, max_length=255, blank=False)

    slug = models.SlugField(unique=True, editable=False, null=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Hesab'
        verbose_name_plural = 'Hesablar'
        ordering = ['-id']

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(seo(self.first_name + "-" + self.last_name), self.id)
        super(MyUser, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()