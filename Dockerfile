# Use an official Python runtime as the base image
FROM python

# Set the working directory inside the container
WORKDIR /app

# Install any dependencies required by the application
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . .

# Expose the port that the Django app will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
