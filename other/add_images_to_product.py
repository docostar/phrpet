import os
import requests
import random
from django.core.files import File
from home.models import Product, Category, ProductImage

# Unsplash API Access Key
ACCESS_KEY = 'YbdjhqhDqucBDII_FjUYzTqmjFEfQLxidQCdQ3Pv8CA' 

# Directory to save downloaded images
image_dir = os.path.join('media', 'download')
os.makedirs(image_dir, exist_ok=True)  # Ensure directory exists

# Function to fetch random image URL from Unsplash
def fetch_random_image_url(query):
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('urls', {}).get('regular')  # Fetch regular-sized image URL
    else:
        print(f"Error fetching image for {query}: {response.json()}")
        return None

# Function to download image and save locally
def download_image(image_url, filename):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        filepath = os.path.join(image_dir, filename)
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return filepath
    else:
        print(f"Failed to download image: {image_url}")
        return None

# Function to add random images to products
def add_images_to_products():
    products = Product.objects.all()
    for product in products:
        num_images = random.randint(2, 4)  # Assign 2–4 images
        for i in range(num_images):
            image_url = fetch_random_image_url(product.name)
            if image_url:
                filename = f"{product.name.replace(' ', '_').lower()}_{i+1}.jpg"
                image_path = download_image(image_url, filename)
                if image_path:
                    # Save the image to the ProductImage model
                    with open(image_path, 'rb') as file:
                        ProductImage.objects.create(product=product, image=File(file))
                    print(f"Added image {filename} to product: {product.name}")
            else:
                print(f"Failed to fetch image for product: {product.name}")

# Run the function to add images to products
add_images_to_products()

print("Products updated with random images!")