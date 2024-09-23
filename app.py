from flask import Flask, request, render_template
from pycaret.classification import load_model, predict_model
import pandas as pd

# Load the trained model
model = load_model('model/best_titanic_model')


# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    # Preselected values when the form is first loaded
    preselected_values = {
        'Pclass': 1,
        'Age': 25,
        'Sex': 'male',
        'travel_party': 2
    }
    return render_template('index.html', preselected_values=preselected_values)


@app.route('/predict', methods=['POST'])
def predict():
    
    # Capture user input from the form submission
    preselected_values = {
        'Pclass': int(request.form['Pclass']),  # Convert to integer immediately
        'Age': int(request.form['Age']),
        'Sex': request.form['Sex'],
        'travel_party': int(request.form['travel_party'])
    }
    
    df = pd.DataFrame([preselected_values])
    
    # Make predictions using the loaded model
    prediction = predict_model(model, data=df)
    survival_prediction = prediction['prediction_label'][0]
    survival_chance = prediction['prediction_score'][0] * 100 
    non_survival_chance = 100 - survival_chance  # Pre-calculate the non-survival chance
    
    return render_template(
        'index.html',
        survival_prediction=survival_prediction,
        survival_chance=round(survival_chance, 2),  # Round to 2 decimal places
        non_survival_chance=round(non_survival_chance, 2),  # Pre-calculate and roun
        preselected_values =preselected_values)
    
if __name__ == "__main__":
    app.run(debug=True)