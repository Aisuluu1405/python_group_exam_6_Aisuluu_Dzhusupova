from django.db import models


STATUS_CHOICES = (
    ('active', 'Active'),
    ('blocked', 'Blocked'),
)


class Register(models.Model):
    author = models.CharField(max_length=50, verbose_name='Author')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(max_length=3000, verbose_name='Text')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    update = models.DateTimeField(auto_now=True, verbose_name='Change date')
    status = models.CharField(max_length=20, null=False, blank=False, verbose_name='Status',
                              default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.author

