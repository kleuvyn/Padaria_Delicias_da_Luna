from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('O campo Email deve ser definido'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Adicione o related_name aqui
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        help_text=_('Specific permissions for this user.')
    )

 

    objects = CustomUserManager()

class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    observacao = models.TextField(blank=True)
    endereco = models.CharField(max_length=255)
    pagamento = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido de {self.usuario.username} - {self.nome}"

