# 💻 Laptop Price Predictor

A user-friendly Machine Learning web application that predicts the estimated price of a laptop based on its hardware and brand specifications. 

---

## 🚀 Features
* **Brand Selection:** Choose from various popular laptop brands (HP, Dell, Lenovo, Apple, etc.).
* **Hardware Customization:** Select CPU type, RAM size, Storage capacity, and Operating System.
* **Instant Prediction:** Predicts the market price in LKR instantly using an interactive web interface.

---

## 🛠️ Tech Stack
* **Programming Language:** Python
* **Web Framework:** Streamlit
* **Machine Learning Library:** Scikit-learn (Random Forest Regressor, Pipeline, OneHotEncoder)
* **Data Manipulation:** Pandas, NumPy

---

## 📦 Dataset & Model
* The model was trained on a comprehensive laptop dataset.
* Categorical features like `Company`, `CPU`, `Ram`, `Storage`, and `OpSys` were encoded using **OneHotEncoder** within a Scikit-learn **Pipeline**.
* A **Random Forest Regressor** was used to achieve high training accuracy and reliable predictions.

---

## 🏃‍♂️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
