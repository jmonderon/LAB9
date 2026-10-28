Setup and Run Guide

Your file is a Django views.py, so you need a Django project around it. Here is the simplest setup, with no database or extra app required.

1. Create the project
You need Python 3.10 or newer. Open a terminal in the folder where you want the project:
bash
python -m venv venv

# Activate it:
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux
pip install django
django-admin startproject inventoryportal .
You should now have this structure:
manage.py
inventoryportal/
    __init__.py
    settings.py
    urls.py
    wsgi.py
    asgi.py
    
2. Add your views
Save your code as inventoryportal/views.py, in the same folder as urls.py.

3. Set up the URLs
Replace the contents of inventoryportal/urls.py with:

python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("item/<str:product_name>/", views.item_detail, name="item_detail"),
]

handler404 = "inventoryportal.views.custom_404"
The handler404 line is what activates your custom_404 function.

4. Adjust settings
In inventoryportal/settings.py, change these two lines:

python
DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
Django only uses a custom 404 handler when DEBUG = False. With DEBUG = True you’ll see Django’s yellow debug page instead. Your app uses inline CSS and no static files, so it works fine this way.

5. Run the server
bash
python manage.py runserver

Then open http://127.0.0.1:8000/ in your browser.

6. Test it
URL	Expected result
/	Home page with product buttons
/about/	About page
/item/laptop/	Laptop details table
/item/keyboard/ and /item/mouse/	Their detail pages
/item/tablet/	“Product Not Found” page, handled by item_detail (404 status)
/anything-else/	“404 - Page Not Found” page, handled by custom_404

Stop the server with Ctrl + C.

Troubleshooting
DisallowedHost error: ALLOWED_HOSTS is missing 127.0.0.1 or localhost.
Yellow Django error page on a bad URL: DEBUG is still True.
ModuleNotFoundError: inventoryportal.views: views.py is in the wrong folder, or your project name differs from inventoryportal. Update the handler404 string to match.
python not found: try python3 (macOS/Linux) or py (Windows).
