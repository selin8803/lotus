# Burnout Analysis Dashboard

## Project Description

This project implements a Decision Tree classifier from scratch to predict burnout levels based on daily work habits and stress indicators.

The system provides an interactive dashboard where users can enter their parameters and instantly receive a prediction. In addition, the decision-making process is visualized using an interactive decision tree.

---

## Algorithm Chosen

The project uses the **Decision Tree algorithm** with **Entropy** and **Information Gain** as the splitting criterion.

The algorithm supports:

* Numerical features using optimal threshold search.
* Categorical features (Yes/No).
* Recursive tree construction.
* Multi-class classification.

No machine learning libraries such as Scikit-learn were used.

---

## Why Decision Tree?

Decision Trees are easy to understand and visualize. They provide interpretable decision paths and support both numerical and categorical attributes, making them suitable for burnout classification.

---

## Dataset Features

### Input Features

* **Sleep** – Average number of sleeping hours.
* **Meetings** – Number of meetings/calls per day.
* **Weekends** – Working on weekends (Yes/No).
* **Stress** – Subjective stress level from 1 to 10.

### Target Classes

* Healthy
* Risk of burnout
* Vacation required
* Critical condition

---

## Algorithm Implementation

The following functions were implemented manually:

* `entropy()`
* `information_gain()`
* `information_gain_numeric()`
* `find_best_threshold()`
* `find_best_feature()`
* `build_tree()`
* `predict()`

Tree construction is performed recursively.

---

## Backend

The backend was implemented using **Python** and **Flask**.

### Available APIs

#### Train Model

```text
POST /api/train
```

Retrains the decision tree using the dataset.

#### Prediction

```text
POST /api/predict
```

Receives user parameters and returns a burnout prediction.

#### Tree Structure

```text
GET /api/tree
```

Returns the decision tree in JSON format for visualization.

---

## Frontend

The frontend was developed using:

* React
* TypeScript
* Vite

The graphical interface includes:

* Interactive sliders.
* Checkbox input.
* Instant prediction.
* Decision tree visualization.
* Color-coded leaf nodes.
* Hover statistics for each node.

---

## Error Handling

The system validates user input and rejects invalid values.

Examples:

* Sleep must be between 1 and 12 hours.
* Meetings must be between 0 and 10.
* Stress level must be between 1 and 10.
* Weekends must be either "Yes" or "No".

Invalid input returns an HTTP 400 error.

---

## Technologies Used

### Backend

* Python
* Flask
* Flask-CORS

### Frontend

* React
* TypeScript
* Vite

### Deployment

* Render
* Vercel

---

## Deployment

### Frontend

https://lotus-psi-teal.vercel.app/

### Backend

https://lotus-rtib.onrender.com

---

## GitHub Repository

https://github.com/selin8803/lotus

---

## AI Collaboration

AI tools (ChatGPT) were used throughout the development process.

AI assistance included:

* Explaining Entropy and Information Gain.
* Debugging recursive tree construction.
* Designing Flask APIs.
* Building the React user interface.
* Styling the decision tree visualization.
* Deployment configuration and troubleshooting.

AI was used as a development assistant, while all algorithmic logic and project integration were completed and verified manually.

---

## Project Structure

```text
lotus
│
├── Backend
│   ├── server.py
│   ├── Entropy.py
│   ├── Dataset.json
│   └── requirements.txt
│
├── Frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```
