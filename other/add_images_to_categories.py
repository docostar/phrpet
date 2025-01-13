import os
import requests
from django.core.files import File
from home.models import Category

# Unsplash API Access Key
ACCESS_KEY = 'YbdjhqhDqucBDII_FjUYzTqmjFEfQLxidQCdQ3Pv8CA'

# Categories to add images to
'''
categories = [
    'Dog Food',
    'Cat Toys',
    'Bird Supplies',
    'Aquarium Decor',
    'Pet Grooming',
    'Reptile Accessories',
    'Small Pet Cages',
    'Pet Vitamins',
]
'''
categories = [
    'Dog Health']
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

# Add categories with downloaded images
for category_name in categories:
    image_url = fetch_random_image_url(category_name)
    if image_url:
        filename = f"{category_name.replace(' ', '_').lower()}.jpg"
        image_path = download_image(image_url, filename)
        if image_path:
            # Save the image to the Category model
            category, created = Category.objects.get_or_create(name=category_name)
            with open(image_path, 'rb') as file:
                category.image.save(filename, File(file))
            category.save()
            print(f"Added image to category: {category_name}")
    else:
        print(f"Failed to fetch image for category: {category_name}")

print("Categories updated with downloaded images!")
