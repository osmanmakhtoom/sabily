from django.db import models

from apps.charity.models.contribution import Contribution


class CashContribution(Contribution):
    class PaymentMethdos(models.TextChoices):
        CREDIT_CARD = "credit_card", "CREDIT_CARD"
        BANK_TRANSFER = "bank_transfer", "BANK_TRANSFER"
        WALLET = "wallet", "WALLET"
        CRYPTO = "crypto", "Cryptocurrency"

    contribution_type = models.ForeignKey(
        "DonationItemType",
        on_delete=models.PROTECT,
        limit_choices_to={"category": "cash"},
    )
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, default="IRR")
    payment_method = models.CharField(
        max_length=50,
        choices=PaymentMethdos.choices,
        default=PaymentMethdos.BANK_TRANSFER,
    )
    transaction_id = models.CharField(max_length=100, blank=True)
    tax_deductible = models.BooleanField(default=True)

    class Meta:
        ordering = ("id", "amount", "-created_at")
