# WATCH_Django ⌚

A modern, responsive e-commerce showcase platform for premium watches built with **Django** and **Tailwind CSS**. This project demonstrates a clean UI/UX for browsing watch brands, exploring the latest products, and viewing customer testimonials.

## 🚀 Features

- **Dynamic Brand Showcase**: List and display various watch brands with descriptions.
- **Product Gallery**: Browse the latest watch collections with pricing and ratings.
- **Customer Reviews**: Integrated testimonial section to build trust.
- **Newsletter Subscription**: Capture user interest with a sleek newsletter signup.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop views using Tailwind CSS.
- **Django Admin Integration**: Easily manage brands, products, and reviews via the powerful Django admin interface.

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, Tailwind CSS (via CDN), Google Fonts
- **Database**: SQLite (default)
- **Media Management**: Django's built-in file handling for product and brand images.

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shamilahmdt/WATCH_Django.git
   cd WATCH_Django
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   *(Ensure Django is installed)*
   ```bash
   pip install django
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py run_server
   ```
   Access the site at `http://127.0.0.1:8000/`.

## 📂 Project Structure

```text
watch/
├── manage.py
├── watch/              # Main project configuration
├── watch_web/          # Core app (Models, Views, URLs)
├── templates/          # HTML templates (index.html)
├── static/             # CSS, Images, and JS files
└── media/              # Uploaded brand and product images
```

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---
Developed with ❤️ by [Shamil Ahammed T](https://github.com/shamilahmdt)
