
# 📚 BookVibe

**BookVibe** is a community-driven Uzbek book review platform where users can discover books, write reviews, and share their reading experiences with others. Inspired by Goodreads, but focused on the Uzbek-speaking community.

---

## 🌟 Features

- 🧠 Browse a growing collection of books
- ✍️ Add reviews with ratings and comments
- 🛠️ Edit or delete your reviews
- 📖 View detailed book pages with user feedback
- 🔐 Admin panel for content management (Django admin)

---

## 🧰 Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, Tailwind CSS (or Bootstrap)
- **Deployment:** Docker (optional), Gunicorn, Nginx
- **CI/CD:** GitHub Actions (planned)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/fazliddinorg/bookvibe.git
cd bookvibe
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Make sure PostgreSQL is running and a database is created.

Update your `.env` or `settings.py` with the correct database credentials.

Then run:

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🛠️ Project Structure

```
bookvibe/
├── books/                 # App for book & review models, views, and templates
├── bookvibe/              # Project settings and main URLs
├── templates/             # Shared templates (base.html, etc.)
├── static/                # Static files (CSS, JS)
├── manage.py
└── requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📬 Contact

Maintainer: **Fazliddin Mamutkhanov**
Email: [fmamutkhanov@gmail.com](mailto:fmamutkhanov@gmail.com)
GitHub: [@fazliddinorg](https://github.com/fazliddinorg)

---

## 🔮 Future Plans

* User authentication
* Book search and filter
* Like/dislike reviews
* Social sharing (Telegram, LinkedIn, WhatsApp)
* Responsive mobile UI

```
