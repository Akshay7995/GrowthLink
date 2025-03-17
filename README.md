# GrowthLink
Task1 for GrowthLink Intern
# **📌 Portfolio Website**

## **📖 Project Overview**
This project is a **personal portfolio website** designed to showcase my **skills, projects, and contact details** in a professional manner. The website serves as an **online resume** and reflects my expertise in various programming languages, frameworks, and developer tools.

## **🎯 Features**
- **About Section** – A brief introduction about me.
- **Skills Section** – Lists my technical and non-technical skills.
- **Projects Section** – Showcases my top projects with descriptions and links.
- **Contact Box** – Displays my mobile number, email, and other contact details.
- **Responsive Design** – Ensures a seamless experience across all devices.

## **🛠️ Tech Stack Used**
- **Frontend**: HTML5, CSS3
- **Backend**: Django (for dynamic content rendering)
- **Database**: SQLite (for storing project details)
- **Version Control**: Git & GitHub

## **🚀 Getting Started**

### **1️⃣ Prerequisites**
Ensure you have the following installed on your system:
- **Python** (Version 3.12 or higher)
- **Django** (Installed via `pip install django`)
- **Git** (for version control)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/your-portfolio-repo.git
cd your-portfolio-repo
```

### **3️⃣ Setup Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **5️⃣ Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```
The website will be accessible at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## **📂 Project Structure**
```
📁 portfolio2
│── 📁 base
│   ├── 📁 templates
│   │   ├── about.html
│   │   ├── index.html
│   │   ├── skills.html
│   │   ├── projects.html
│   │   ├── contact.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│── 📁 static
│   ├── 📁 css
│   │   ├── style.css
│   ├── 📁 images
│── manage.py
│── requirements.txt
│── README.md
```

## **📝 How to Modify the Content**
### **1️⃣ Update Personal Details**
- Modify the **Contact Box** in `contact.html` to add your personal information.

### **2️⃣ Add New Projects**
- Open `projects.html` and add new project details in the provided template.

### **3️⃣ Customize Skills**
- Edit `skills.html` to update the list of programming languages, frameworks, and tools.

### **4️⃣ Modify Styles**
- Update `style.css` to change the appearance of the website.

## **🐞 Troubleshooting & Common Issues**
**❌ Issue:** `TemplateDoesNotExist at /contact/`
✔ **Solution:** Ensure `contact.html` is located in the `templates` directory inside the `base` app.

**❌ Issue:** `django.core.exceptions.ImproperlyConfigured: STATIC_ROOT is not set`
✔ **Solution:** Add the following to `settings.py`:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
Then, run:
```sh
python manage.py collectstatic
```

## **📌 Deployment Guide**
To deploy the website on **GitHub Pages, PythonAnywhere, or Heroku**, follow these steps:

### **1️⃣ Push Code to GitHub**
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### **2️⃣ Deploy to PythonAnywhere (For Django Apps)**
- Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
- Upload your project and set up the virtual environment.
- Configure `wsgi.py` and `settings.py` for production.

### **3️⃣ Deploy to Heroku**
```sh
heroku login
heroku create my-portfolio
git push heroku main
```

## **👨‍💻 About Me**
I am proficient in a variety of programming languages including **Java, Python, MySQL, and HTML**, allowing me to tackle a wide range of technical challenges.  

### **🔹 My Key Skills**
- **Languages**: Java, Python, MySQL, HTML
- **Frameworks**: Spring Boot, Django
- **Developer Tools**: Git, GitHub, Postman
- **Core Concepts**: Object-Oriented Programming (OOP), Data Structures and Algorithms (DSA)

I have **strong problem-solving skills** and a passion for building **scalable applications**.

## **📞 Contact**
For any queries or collaboration opportunities, feel free to reach out:
- **📧 Email:** akshayenuguru3@gmail.com
- **📞 Phone:** +91 9959905305
- **🌐 GitHub:** [github.com/your-username](https://github.com/Akshay7995)
- **🔗 LinkedIn:** [linkedin.com/in/your-profile](https://www.linkedin.com/in/akshayenuguru/)
