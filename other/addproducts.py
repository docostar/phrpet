from random import choice
from datetime import datetime

# List of categories
categories = [
    'Dog Health',
    'Dog Food',
    'Cat Toys',
    'Bird Supplies',
    'Aquarium Decor',
    'Pet Grooming',
    'Reptile Accessories',
    'Small Pet Cages',
    'Pet Vitamins',
]

# Dummy products
products = [
    {
        "name": "Dog Dental Chews",
        "category": choice(categories),
        "description": "Chews designed to clean teeth and freshen your dog's breath.",
        "composition": "Natural chicken flavor, calcium, and zinc.",
        "benefits": "Reduces tartar buildup and promotes oral hygiene.",
        "packing": "10 pieces per pack",
        "mrp": 199.99,
    },
    {
        "name": "Premium Bird Seed Mix",
        "category": choice(categories),
        "description": "A mix of seeds enriched with nutrients for birds.",
        "composition": "Sunflower seeds, millet, and dried fruits.",
        "benefits": "Supports healthy feathers and energy for birds.",
        "packing": "1kg resealable pack",
        "mrp": 249.99,
    },
    {
        "name": "Cat Scratching Post",
        "category": choice(categories),
        "description": "Durable scratching post to satisfy your cat's instincts.",
        "composition": "Sisal rope and solid wood base.",
        "benefits": "Prevents furniture scratching and promotes exercise.",
        "packing": "1 piece",
        "mrp": 899.99,
    },
    {
        "name": "Aquarium LED Light",
        "category": choice(categories),
        "description": "Energy-efficient LED light for aquariums.",
        "composition": "LED, aluminum frame, and waterproof casing.",
        "benefits": "Enhances the aquarium's appearance and promotes plant growth.",
        "packing": "1 unit",
        "mrp": 499.99,
    },
    {
        "name": "Small Pet Chewing Toys",
        "category": choice(categories),
        "description": "Set of safe chewing toys for small pets.",
        "composition": "Natural wood and non-toxic dye.",
        "benefits": "Keeps pets entertained and supports dental health.",
        "packing": "5 pieces",
        "mrp": 349.99,
    },
    {
        "name": "Reptile Heat Lamp",
        "category": choice(categories),
        "description": "A heat lamp designed for reptiles requiring warmth.",
        "composition": "Ceramic bulb and metal reflector.",
        "benefits": "Provides essential heat for reptiles' health and comfort.",
        "packing": "1 unit",
        "mrp": 599.99,
    },
    {
        "name": "Cat Grooming Brush",
        "category": choice(categories),
        "description": "Soft-bristle brush for grooming your cat.",
        "composition": "Plastic handle and synthetic bristles.",
        "benefits": "Reduces shedding and maintains a healthy coat.",
        "packing": "1 piece",
        "mrp": 129.99,
    },
    {
        "name": "Dog Training Leash",
        "category": choice(categories),
        "description": "Adjustable leash for effective dog training.",
        "composition": "Nylon and stainless steel clip.",
        "benefits": "Improves control and safety during walks.",
        "packing": "1 leash",
        "mrp": 399.99,
    },
    {
        "name": "Vitamin Supplements for Cats",
        "category": choice(categories),
        "description": "Multivitamins to support a cat's health and vitality.",
        "composition": "Vitamin B complex, taurine, and Omega-3.",
        "benefits": "Boosts energy and supports a healthy coat.",
        "packing": "60 tablets",
        "mrp": 349.99,
    },
    {
        "name": "Reptile Hideout Cave",
        "category": choice(categories),
        "description": "Natural-looking cave for reptiles to hide and rest.",
        "composition": "Resin and eco-friendly materials.",
        "benefits": "Provides a safe and comfortable space for reptiles.",
        "packing": "1 piece",
        "mrp": 299.99,
    },
    {
        "name": "Aquarium Air Pump",
        "category": choice(categories),
        "description": "Silent air pump to maintain oxygen levels in aquariums.",
        "composition": "Plastic casing and silicone diaphragm.",
        "benefits": "Ensures a healthy aquatic environment.",
        "packing": "1 unit",
        "mrp": 449.99,
    },
    {
        "name": "Small Pet Exercise Wheel",
        "category": choice(categories),
        "description": "Safe and silent exercise wheel for small pets.",
        "composition": "Plastic and anti-slip surface.",
        "benefits": "Encourages activity and reduces boredom.",
        "packing": "1 piece",
        "mrp": 299.99,
    },
    {
        "name": "Bird Perch Stand",
        "category": choice(categories),
        "description": "A sturdy perch stand for birds to rest and play.",
        "composition": "Natural wood and metal base.",
        "benefits": "Promotes exercise and comfort for birds.",
        "packing": "1 stand",
        "mrp": 199.99,
    },
    {
        "name": "Dog Flea Collar",
        "category": choice(categories),
        "description": "Adjustable collar to repel fleas and ticks.",
        "composition": "Natural essential oils and plastic.",
        "benefits": "Protects dogs from parasites for up to 8 months.",
        "packing": "1 collar",
        "mrp": 499.99,
    },
    {
        "name": "Fish Food Pellets",
        "category": choice(categories),
        "description": "Nutritious pellets for all types of aquarium fish.",
        "composition": "Fish meal, vitamins, and minerals.",
        "benefits": "Promotes vibrant colors and healthy growth.",
        "packing": "500g jar",
        "mrp": 149.99,
    },
]

# Inserting dummy products into the database
from home.models import Product, Category

for product in products:
    category_name = product.pop("category")
    category = Category.objects.get_or_create(name=category_name)[0]  # Ensure the category exists
    Product.objects.create(category=category, **product)

print("Dummy products added successfully!")
