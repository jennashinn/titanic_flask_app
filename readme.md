## Titanic Survival Prediction App

This is a Flask-based web application that predicts whether a passenger would survive the Titanic disaster based on certain characteristics such as passenger class, age, gender, and the number of people traveling with them. The app uses a machine learning model built with PyCaret and provides an interactive form for users to input passenger details and receive a prediction.

### Table of Contents

- [Titanic Survival Prediction App](#titanic-survival-prediction-app)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Install Required Libraries](#install-required-libraries)
  - [How to Run the App](#how-to-run-the-app)
  - [Usage](#usage)
  - [Model Information](#model-information)
  - [File Structure](#file-structure)
  - [Future Improvements](#future-improvements)
  - [Contributing](#contributing)
  - [License](#license)

---

### Features

- User-friendly interface built with Flask and Bootstrap.
- Input form for users to enter details such as **passenger class**, **age**, **sex**, and **number of people traveling with them**.
- Provides predictions on whether the passenger would survive, along with the predicted probability.
- Built with a machine learning model using **PyCaret**.
- Dynamic form that retains user inputs after submission.

---

### Setup and Installation

#### Prerequisites

1. **Python 3.x**: Ensure that Python is installed. You can download it from [python.org](https://www.python.org/).
2. **Pip**: Make sure you have pip, Python’s package installer, installed.

#### Clone the Repository

```bash
git clone https://github.com/your-username/titanic_flask_app.git
cd titanic_flask_app
```

#### Install Required Libraries

First, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

### How to Run the App

1. **Set Flask App Environment**:

   ```bash
   export FLASK_APP=app.py
   ```

2. **Run the Flask Development Server**:

   ```bash
   flask run
   ```

3. **Access the App**:
   - The app will be accessible locally at: `http://127.0.0.1:5000/`

---

### Usage

1. **Open the app in your browser** (`http://127.0.0.1:5000/`).
2. **Fill out the form**:
   - **Passenger Class**: Choose between First, Second, or Third Class.
   - **Age**: Enter the passenger's age.
   - **Sex**: Select the gender.
   - **Number of People Traveling With**: Enter the number of people traveling with the passenger.
3. **Submit**: Click the "Would you survive?" button to get the prediction.
4. **View the Prediction**: After submission, the app will display the probability of survival based on the inputs.

---

### Model Information

- The app uses a machine learning model built with **PyCaret's CatBoost Model** to predict the survival of passengers.
- The model is trained on the Titanic dataset, which includes various features like passenger class, age, sex, and family size.
- The model outputs both a prediction label (survived or not) and the probability of survival.

### File Structure

```
.
├── app.py               # Main Flask application
├── model/
│   └── best_titanic_model  # Pre-trained PyCaret model
├── templates/
│   └── index.html        # HTML template for the app
├── static/
│   └── style.css         # Custom CSS file
├── requirements.txt      # Python dependencies
└── README.md             # This README file
```

---

### Future Improvements

- **Model Improvements**: Fine-tune the model or use different algorithms to improve prediction accuracy.
- **Additional Features**: Allow users to input more features (e.g., port of embarkation, ticket fare, etc.).
- **Data Visualization**: Add data visualizations to show how different factors affect survival probability.

