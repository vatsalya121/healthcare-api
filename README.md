# **Hospital Management API**

A RESTful API for managing users, patients, doctors, and their mappings in a hospital system. Built using **Django REST Framework (DRF)** with **JWT authentication**.

---

## **📌 Features**
- **User Authentication** (Register & Login with JWT)
- **Patient Management** (CRUD Operations)
- **Doctor Management** (CRUD Operations)
- **Patient-Doctor Mapping** (Assign and Remove Doctors)

---

## **⚙️ Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/hospital-management-api.git
cd hospital-management-api
```

### **2️⃣ Create & Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations & Create Superuser**
```sh
python manage.py migrate
python manage.py createsuperuser
```

### **5️⃣ Run the Server**
```sh
python manage.py runserver
```

---

## **🛠 API Endpoints**

### **🔑 Authentication APIs**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Log in a user and get a JWT token |

---

### **🏥 Patient Management APIs**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/patients/` | Add a new patient (Authenticated users only) |
| `GET` | `/api/patients/` | Retrieve all patients created by the user |
| `GET` | `/api/patients/<id>/` | Get details of a specific patient |
| `PUT` | `/api/patients/<id>/` | Update patient details |
| `DELETE` | `/api/patients/<id>/` | Delete a patient |

---

### **👨‍⚕️ Doctor Management APIs**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/doctors/` | Add a new doctor (Authenticated users only) |
| `GET` | `/api/doctors/` | Retrieve all doctors |
| `GET` | `/api/doctors/<id>/` | Get details of a specific doctor |
| `PUT` | `/api/doctors/<id>/` | Update doctor details |
| `DELETE` | `/api/doctors/<id>/` | Delete a doctor |

---

### **🔗 Patient-Doctor Mapping APIs**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/mappings/` | Assign a doctor to a patient |
| `GET` | `/api/mappings/` | Retrieve all patient-doctor mappings |
| `GET` | `/api/mappings/<patient_id>/` | Get all doctors assigned to a specific patient |
| `DELETE` | `/api/mappings/delete/<id>/` | Remove a doctor from a patient |

---

## **🔑 JWT Authentication**
- After **login**, the API returns an **access token**.
- Pass this token in the **Authorization header** for all protected routes.

**Example:**
```sh
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## **🚀 How to Push Project to GitHub**
### **1️⃣ Initialize Git**
```sh
git init
```

### **2️⃣ Add Remote Repository**
```sh
git remote add origin https://github.com/yourusername/hospital-management-api.git
```

### **3️⃣ Add & Commit Files**
```sh
git add .
git commit -m "Initial commit"
```

### **4️⃣ Push to GitHub**
```sh
git branch -M main
git push -u origin main
```

---

## **📌 Deployment (Optional)**
If you want to deploy your API:
- Use **Heroku** / **Render** / **DigitalOcean**
- Set environment variables for database and JWT secret

---
