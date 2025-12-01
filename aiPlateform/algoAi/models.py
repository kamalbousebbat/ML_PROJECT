from django.db import models
from django.conf import settings
# Create your models here.

class classdataset(models.Model):
    # Meilleure pratique : utiliser settings.AUTH_USER_MODEL au lieu de User directement
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='predictions',
        verbose_name='predection'
    )
    model_name = models.CharField(max_length=200)
    niveau_etude = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    affectation = models.CharField(max_length=200)
    annee_ambauche = models.CharField(max_length=200)
    salaire_cat = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    experience_domain = models.CharField(max_length=200)
    target = models.CharField(max_length=200, default='')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'predection'
        verbose_name_plural = 'predections'
    
    def __str__(self):
        return f"{self.model_name} - {self.user.username}"
    
class FitnessDataset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='fitness_predictions',
        verbose_name='Utilisateur'
    )
    model_name = models.CharField(max_length=200, verbose_name='Nom du modèle')
    

    age = models.FloatField(verbose_name='Âge')
    gender = models.CharField(max_length=50, verbose_name='Genre')
    weight = models.FloatField(verbose_name='Poids (kg)')
    height = models.FloatField(verbose_name='Taille (cm)')
    bmi = models.FloatField(verbose_name='IMC')
    fat_percentage = models.FloatField(verbose_name='Pourcentage de graisse (%)')
    max_bpm = models.FloatField(verbose_name='BPM Maximum')
    avg_bpm = models.FloatField(verbose_name='BPM Moyen')
    resting_bpm = models.FloatField(verbose_name='BPM au repos')
    session_duration = models.FloatField(verbose_name='Durée session (min)')
    workout_type = models.CharField(max_length=100, verbose_name='Type d\'entraînement')
    water_intake = models.FloatField(verbose_name='Consommation d\'eau (L)')
    workout_frequency = models.FloatField(verbose_name='Fréquence d\'entraînement (jours/semaine)')
    experience_level = models.IntegerField(verbose_name='Niveau d\'expérience')
    
    # Prédiction
    target = models.CharField(max_length=200, blank=True, default='', verbose_name='Résultat')
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    date_modification = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    
    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'Prédiction Fitness'
        verbose_name_plural = 'Prédictions Fitness'
    
    def __str__(self):
        return f"{self.model_name} - {self.user.username} - {self.date_creation.strftime('%d/%m/%Y')}"

