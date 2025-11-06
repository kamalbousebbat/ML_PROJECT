from django.shortcuts import render
import os,joblib

# Create your views here.

def index(request):
    return render(request,'index.html')

def regLog_details(request):
    return render(request,'regLog_details.html')

def regLog_atelier(request):
    return render(request,'regLog_atelier.html')

def regLog_tester(request):
    return render(request , 'vehicles_form.html')

def load_models(name):
    # Remonte d'un niveau dans la structure des dossiers (pour aller de 'app/views.py' à 'app/')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Construit le chemin vers le dossier contenant les modèles (e.g., 'app/models_ai')
    models_dir = os.path.join(base_dir, 'models_ai')
    
    # Construit le chemin complet du fichier du modèle (e.g., 'app/models_ai/logreg_model.pkl')
    model_path = os.path.join(models_dir, name)
    
    # Charge le modèle sérialisé à l'aide de la librairie joblib
    ml_model = joblib.load(model_path)
    
    return ml_model

def reglog_prediction(request):
    #Tâche 1 : Recevoir le Colis
    if request.method == 'POST':
        # Tâche 2 : Déballer le Colis
        hauteur = float(request.POST.get('hauteur'))
        nbr_roues = float(request.POST.get('Nombre_de_roues'))
        
        # Tâche 3 : Réveiller l'Expert
        # cette fonction (load_models) est défini avant
        model = load_models('logreg_model.pkl')
        
        # Tâche 4 : Poser la Question à l'Expert
        prediction = model.predict([[hauteur, nbr_roues]])
        predicted_class = prediction[0]
        
        # Tâche 5 : Traduire la Réponse
        type_vehicules = {0: 'Camion', 1: 'Touristique'}
        img_url = {'Camion':'images/camion.jpg', 'Touristique':'images/touristique.jpg'}
        pred_vehicule = type_vehicules[predicted_class]
        pred_img = img_url[pred_vehicule]
        
        # Tâche 6 : Préparer le Plateau-Repas (context)
        input_data = {
            'hauteur':hauteur,
            'nbr_roues':nbr_roues
        }
        
        context = {
            'type_vehicule':pred_vehicule,
            'img_vehicule':pred_img,
            'inital_data' : input_data # NOTE: Il y a une faute de frappe dans l'image ('inital_data' au lieu de 'initial_data')
        }
        
        return render(request, 'reglog_results.html', context)
        
    return render(request, 'vehicles_form.html')