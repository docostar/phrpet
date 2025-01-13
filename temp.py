import requests
from home.models import Category

# Unsplash API Access Key
ACCESS_KEY = 'YbdjhqhDqucBDII_FjUYzTqmjFEfQLxidQCdQ3Pv8CA'

# Categories to add images to
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

# Add categories with images
for category_name in categories:
    image_url = fetch_random_image_url(category_name)
    if image_url:
        # Create or update category with random image
        category, created = Category.objects.get_or_create(name=category_name)
        category.image = image_url  # Assuming Category.image is a URL field or handled appropriately
        category.save()
        print(f"Added image to category: {category_name}")
    else:
        print(f"Failed to fetch image for category: {category_name}")

print("Categories updated with random images!")
