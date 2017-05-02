from django.db.models import Manager
from django.utils import timezone


class EmailManager(Manager):

    def logging(self, email, recipients, subject, body='', **extra_fields):
        logging = self.model(from_email=email, recipients=recipients, ok=True,
                             subject=subject, body=body, **extra_fields)
        logging.save(using=self._db)
        return logging
