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


# Random Forest

def randforest_details(request):
    return render(request,'randforest_details/randforest_details.html')

def randforest_atelier(request):
    return render(request,'randforest_details/randforest_atelier.html')

def randforest_tester(request):
    return render(request , 'randforest_details/empolyees_form.html')

def randforest_prediction(request):
    #Tâche 1 : Recevoir le Colis
    if request.method == 'POST':
        # Tâche 2 : Déballer le Colis
        education = request.POST.get('Education')
        joining_year = int(request.POST.get('JoiningYear'))
        city = request.POST.get('City')
        payment_tier = int(request.POST.get('PaymentTier'))
        age = int(request.POST.get('Age'))
        gender = request.POST.get('Gender')
        ever_benched = request.POST.get('EverBenched')  # "Yes" ou "No"
        experience = float(request.POST.get('ExperienceInCurrentDomain'))

        if(education.lower()=='Bachelors'):
            education_model=0
        elif(education.lower()=='Masters'):
            education_model=1
        else:
            education_model=2

        City_Pune=0
        City_New_Delhi=0
        City_Bangalore=0
        if(city.lower()=='bangalore'):
            City_Bangalore=1
        elif(city.lower()=='new delhi'):
            City_New_Delhi=1
        else:
            City_Pune=0
        

        # Convertir EverBenched en binaire si nécessaire
        ever_benched_model = 1 if ever_benched.lower() == 'yes' else 0
        gender_model = 1 if gender.lower() == 'male' else 0
        
        # Tâche 3 : Réveiller l'Expert
        # cette fonction (load_models) est défini avant
        model = load_models('random_forest_model.pkl')
        
        # Tâche 4 : Poser la Question à l'Expert
        prediction = model.predict([[education_model,joining_year,payment_tier,age,gender_model,ever_benched_model,experience,City_Bangalore,City_New_Delhi,City_Pune]])
        predicted_class = prediction[0]

        # Debug : afficher la prédiction dans la console
        print("=== DEBUG ===")
        print("Input DataFrame :")
        print(predicted_class)
        print("Predicted Class :", predicted_class)
        print("================")
        
        # Tâche 5 : Traduire la Réponse
        employee_leave = {0: 'NOT LEAVING', 1: 'LEAVING'}
        img_url = {'NOT LEAVING':'images/random_forest.jpeg', 'LEAVING':'images/random_forest1.jpeg'}
        pred_vehicule = employee_leave[predicted_class]
        pred_img = img_url[pred_vehicule]
        
        # Tâche 6 : Préparer le Plateau-Repas (context)
        input_data = {
            'education':education,
            'joining_year':joining_year,
            'city':city,
            'payment_tier':payment_tier,
            'age':age,
            'gender':gender,
            'ever_benched':ever_benched,
            'experience':experience
           
        }
        
        context = {
            'leaving':pred_vehicule,
            'img_emp':pred_img,
            'inital_data' : input_data # NOTE: Il y a une faute de frappe dans l'image ('inital_data' au lieu de 'initial_data')
        }
        
        return render(request, 'randforest_details/randforest_results.html', context)
        
    return render(request, 'randforest_details/empolyees_form.html')

