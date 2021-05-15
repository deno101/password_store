from django.db import models
from store.encryption import AESCiper


# Create your models here.

class EncryptedTextField(models.TextField):
    def to_python(self, value):
        if isinstance(value, EncryptedTextField):
            return value

        if isinstance(value, str):
            return AESCiper().decrypt(value)

        return None

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if isinstance(value, str):
            return AESCiper().encrypt(value)
        return None


class PasswordStore(models.Model):
    site = models.TextField(blank=False)
    username = EncryptedTextField(blank=False)
    password = EncryptedTextField(blank=False)

