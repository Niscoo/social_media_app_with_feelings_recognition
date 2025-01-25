from django.db import models

# Create your models here.
from django.db import models

class Publication(models.Model):
    content = models.TextField()
    sentiment = models.CharField(max_length=10, default='neutral')  # 'positive', 'negative', 'neutral'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Affiche les 50 premiers caractères du contenu