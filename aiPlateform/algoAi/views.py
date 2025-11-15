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

# Decision Tree

def decTree_details(request):
    return render(request,'Decision_tree/decTree_details.html')

def decTree_atelier(request):
    return render(request,'Decision_tree/decTree_atelier.html')
def decTree_tester(request):
    return render(request , 'Decision_tree/decTree_form.html')

def decTree_prediction(request):
    #Tâche 1 : Recevoir le Colis
    if request.method == 'POST':
        # Tâche 2 : Déballer le Colis
        education = request.POST.get('Education')
        joining_year = int(request.POST.get('JoiningYear'))
        city = request.POST.get('City')
        payment_tier = int(request.POST.get('PaymentTier'))
        age = int(request.POST.get('Age'))
        gender = request.POST.get('Gender')
        ever_benched = request.POST.get('EverBenched') 
        experience = float(request.POST.get('ExperienceInCurrentDomain'))

        if(education.lower()=='Bachelors'):
            education_model=0
        elif(education.lower()=='Masters'):
            education_model=1
        else:
            education_model=2

        if city.lower() == 'bangalore':
            city_model = 0
        elif city.lower() == 'new delhi':
            city_model = 1
        else:
            city_model = 2

        

        # Convertir EverBenched en binaire si nécessaire
        ever_benched_model = 1 if ever_benched.lower() == 'yes' else 0
        gender_model = 1 if gender.lower() == 'male' else 0
        
        # Tâche 3 : Réveiller l'Expert
        # cette fonction (load_models) est défini avant
        model = load_models('decision_tree_model.pkl')
        
        # Tâche 4 : Poser la Question à l'Expert
        prediction = model.predict([[education_model,joining_year,payment_tier,age,gender_model,ever_benched_model,experience,city_model]])
        predicted_class = prediction[0]

        # Debug : afficher la prédiction dans la console
        print("=== DEBUG ===")
        print("Input DataFrame :")
        print(predicted_class)
        print("Predicted Class :", predicted_class)
        print("================")
        
        # Tâche 5 : Traduire la Réponse
        employee_leave = {0: 'NOT LEAVING', 1: 'LEAVING'}
        img_url = {'NOT LEAVING':'images/decTree1.jpg', 'LEAVING':'images/decTree2.jpg'}
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
        
        return render(request, 'Decision_tree/decTree_results.html', context)
        
    return render(request, 'Decision_tree/decTree_form.html')

# SVM

def SVM_details(request):
    return render(request,'Support_Vector_Machine/SVM_details.html')

def SVM_atelier(request):
    return render(request,'Support_Vector_Machine/SVM_atelier.html')

def SVM_tester(request):
    return render(request , 'Support_Vector_Machine/SVM_form.html')

def SVM_prediction(request):
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
        model = load_models('support_vector_machine_model.pkl')
        
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
        img_url = {'NOT LEAVING':'images/SVM_image1.jpg', 'LEAVING':'images/SVM_image2.jpg'}
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
        
        return render(request, 'Support_Vector_Machine/SVM_results.html', context)
        
    return render(request, 'Support_Vector_Machine/SVM_form.html')


# SVM REGRESSION 

def SVM_Reg_details(request):
    return render(request, 'SVM_Regression/SVM_Reg_details.html')


def SVM_Reg_atelier(request):
    return render(request, 'SVM_Regression/SVM_Reg_atelier.html')


def SVM_Reg_tester(request):
    return render(request, 'SVM_Regression/SVM_Reg_form.html')


def SVM_Reg_prediction(request):
    if request.method == 'POST':
        try:
            age = float(request.POST.get('Age'))
            gender = request.POST.get('Gender')
            weight = float(request.POST.get('Weight (kg)'))
            height = float(request.POST.get('Height (m)'))
            max_bpm = float(request.POST.get('Max_BPM'))
            avg_bpm = float(request.POST.get('Avg_BPM'))
            resting_bpm = float(request.POST.get('Resting_BPM'))
            session_duration = float(request.POST.get('Session_Duration (hours)'))
            workout_type = request.POST.get('Workout_Type')
            fat_percentage = float(request.POST.get('Fat_Percentage'))
            water_intake = float(request.POST.get('Water_Intake (liters)'))
            workout_freq = float(request.POST.get('Workout_Frequency (days/week)'))
            experience = request.POST.get('Experience_Level')
            bmi = float(request.POST.get('BMI'))

        except Exception as e:
            return render(request, 'SVM_Regression/SVM_Reg_form.html', {
                'error': '⚠️ Vérifiez que toutes les valeurs numériques sont correctement remplies.'
            })

        # Encoder les valeurs catégorielles
        gender_val = 1 if gender.lower() == "male" else 0

        workout_map = {"Yoga": 0, "Cardio": 1, "Strength": 2, "HIIT": 3, "Other": 4}
        workout_val = workout_map.get(workout_type, 4)

        exp_map = {"Beginner": 0, "Intermediate": 1, "Advanced": 2}
        exp_val = exp_map.get(experience, 1)

        # Charger modèle
        model = load_models('SVR_model.pkl')

        # Features
        features = [[
            age, gender_val, weight, height, max_bpm, avg_bpm, resting_bpm,
            session_duration, workout_val, fat_percentage, water_intake,
            workout_freq, exp_val, bmi
        ]]

        # Prédiction
        prediction = model.predict(features)
        calories_pred = round(float(prediction[0]), 2)
        
        # Choisir image selon genre
        if gender.lower() == "male":
           img_path = "images/SVRimage2.jpg"
        else:
           img_path = "images/SVRimage1.jpg"

        context = {
            'prediction': calories_pred,
            'initial_data': {
                'Age': age,
                'Gender': gender,
                'Weight (kg)': weight,
                'Height (m)': height,
                'Max_BPM': max_bpm,
                'Avg_BPM': avg_bpm,
                'Resting_BPM': resting_bpm,
                'Session_Duration (hours)': session_duration,
                'Workout_Type': workout_type,
                'Fat_Percentage': fat_percentage,
                'Water_Intake (liters)': water_intake,
                'Workout_Frequency (days/week)': workout_freq,
                'Experience_Level': experience,
                'BMI': bmi,
            },
            'img_reg': img_path
        }

        return render(request, 'SVM_Regression/SVM_Reg_results.html', context)

    return render(request, 'SVM_Regression/SVM_Reg_form.html')
