from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
###
from kernel import models as km
###
from logmail import managers as lmr


@python_2_unicode_compatible
class Email(km.KernelModel):
    """
    Model to store outgoing email information
    """
    ADMIN = True

    from_email = models.TextField(_("from email"))
    recipients = models.TextField(_("recipients"))
    subject = models.TextField(_("subject"))
    body = models.TextField(_("body"))
    ok = models.BooleanField(_("ok"), default=False, db_index=True)
    date_sent = models.DateTimeField(_("date sent"), auto_now_add=True, db_index=True)

    objects = lmr.EmailManager()

    def __str__(self):
        return "{s.recipients}: {s.subject}".format(s=self)

    class Meta:
        verbose_name = _("email")
        verbose_name_plural = _("email")
        ordering = ('-date_sent', )

    @classmethod
    def list_display(cls):
        return 'from_email', 'recipients', 'subject', 'ok', 'date_sent'


