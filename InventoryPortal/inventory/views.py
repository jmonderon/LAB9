from django.http import HttpResponse
from django.utils.html import escape

SYSTEM_NAME = "InventoryPortal"

PRODUCTS = {
    "laptop": {
        "name": "Laptop",
        "price": "₱35,000",
        "stock": 12,
        "description": "15.6-inch laptop, 16GB RAM, 512GB SSD.",
    },
    "keyboard": {
        "name": "Keyboard",
        "price": "₱1,500",
        "stock": 40,
        "description": "Mechanical keyboard with RGB backlight.",
    },
    "mouse": {
        "name": "Mouse",
        "price": "₱800",
        "stock": 55,
        "description": "Wireless optical mouse, 1600 DPI.",
    },
}

CSS = """
<style>
  body { font-family: Arial, sans-serif; margin: 0; background: #f4f6f8; color: #222; }
  header { background: #1f3a5f; color: #fff; padding: 16px 32px; }
  header h1 { margin: 0 0 8px; font-size: 24px; }
  nav a { color: #cfe3ff; margin-right: 16px; text-decoration: none; font-weight: bold; }
  nav a:hover { text-decoration: underline; }
  main { max-width: 720px; margin: 32px auto; background: #fff; padding: 24px 32px;
         border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,.1); }
  .products a { display: inline-block; margin: 6px 8px 6px 0; padding: 8px 16px;
                background: #1f3a5f; color: #fff; border-radius: 4px; text-decoration: none; }
  .products a:hover { background: #2c5282; }
  table { border-collapse: collapse; width: 100%; }
  td { padding: 8px; border-bottom: 1px solid #ddd; }
  td:first-child { font-weight: bold; width: 30%; }
</style>
"""


def render_page(title, body, status=200):
    """Wrap content in the shared layout (system name + navigation on every page)."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{escape(title)} | {SYSTEM_NAME}</title>
  {CSS}
</head>
<body>
  <header>
    <h1>{SYSTEM_NAME}</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/about/">About</a>
      <a href="/item/laptop/">Laptop</a>
      <a href="/item/keyboard/">Keyboard</a>
      <a href="/item/mouse/">Mouse</a>
    </nav>
  </header>
  <main>{body}</main>
</body>
</html>"""
    return HttpResponse(html, status=status)


def home(request):
    body = """
      <h2>Welcome to InventoryPortal</h2>
      <p>Welcome to the computer shop's inventory system. Browse our sample products:</p>
      <div class="products">
        <a href="/item/laptop/">Laptop</a>
        <a href="/item/keyboard/">Keyboard</a>
        <a href="/item/mouse/">Mouse</a>
      </div>
    """
    return render_page("Home", body)


def about(request):
    body = """
      <h2>About InventoryPortal</h2>
      <p>InventoryPortal is a simple inventory management system for a computer shop.
         It lets staff navigate between pages and view information about available
         products such as laptops, keyboards, and mice.</p>
      <p>Built with Django using URL routing and function-based views.</p>
    """
    return render_page("About", body)


def item_detail(request, product_name):
    product = PRODUCTS.get(product_name.lower())

    if product is None:
        body = f"""
          <h2>Product Not Found</h2>
          <p>Sorry, no product named "<strong>{escape(product_name)}</strong>" exists.</p>
          <p><a href="/">Return to Home</a></p>
        """
        return render_page("Product Not Found", body, status=404)

    body = f"""
      <h2>{product['name']}</h2>
      <table>
        <tr><td>Product</td><td>{product['name']}</td></tr>
        <tr><td>Price</td><td>{product['price']}</td></tr>
        <tr><td>Stock</td><td>{product['stock']} units</td></tr>
        <tr><td>Description</td><td>{product['description']}</td></tr>
      </table>
    """
    return render_page(product['name'], body)


def custom_404(request, exception):
    body = """
      <h2>404 - Page Not Found</h2>
      <p>The page you requested does not exist.</p>
      <p><a href="/">Return to Home</a></p>
    """
    return render_page("Not Found", body, status=404)