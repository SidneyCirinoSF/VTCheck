import uuid
from django.db import models


class Viatura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    placa = models.CharField(max_length=10, unique=True)
    prefixo = models.CharField(max_length=20, unique=True, null=True, blank=True)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField(null=True, blank=True)

    STATUS_CHOICES = [
        ("ok", "Em condições de uso"),
        ("manutencao", "Em manutenção"),
        ("inoperante", "Inoperante"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ok"
    )

    descricao_problema = models.TextField(
        null=True,
        blank=True,
        help_text="Descrever o problema caso a viatura não esteja OK."
    )

    def __str__(self):
        return f"{self.prefixo or ''} - {self.placa}"
