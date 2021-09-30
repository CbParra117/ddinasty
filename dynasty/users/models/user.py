from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
#from django.contrib.auth.models import User

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager
from users.utils import get_default_share_code

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    """
    See https://github.com/django/django/blob/main/django/contrib/auth/base_user.py
    """

    MALE, FEMALE = 'male', 'female'

    SEX_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=120,
        blank=True)
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=255,
        blank=True,
        null=True)
    email = models.EmailField(
        verbose_name=_('Email'),
        max_length=255,
        unique=True,)
    avatar = models.ImageField(
        verbose_name=_('Avatar'),
        upload_to='avatars',
        blank=True,
        null=True)
    biography = models.TextField(
        verbose_name=_('Biography'),
        blank=True,
        null=True)
    date_of_birth = models.DateField(
        verbose_name=_('Birth Date'),
        blank=True,
        null=True)
    sex = models.CharField(
        verbose_name=_('Sex'),
        max_length=15,
        null=True,
        blank=True,
        choices=SEX_CHOICES)
    share_code = models.CharField(
        verbose_name=_('share code'),
        max_length=45,
        unique=True,
        default=get_default_share_code)
    telephone = models.CharField(
        verbose_name=_('telephone'),
        max_length=20,)
    mobile = models.CharField(
        verbose_name=_('mobile'),
        max_length=20,
        blank=True,
        null=True)
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now)

    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        if self.first_name:
            return self.get_full_name()

        return self.email

    @property
    def address(self):
        return self.user_address.all()

    class Meta:
        app_label = "users"
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def send_welcome_email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
