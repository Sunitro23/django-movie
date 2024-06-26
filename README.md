# django-movie

This is a Django web application that allows you to search for movies.

## Getting Started

To get started with the Django app, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Sunitro23/django-movie.git
   ```

2. Navigate to the project directory:

   ```shell
   cd django-movie
   ```

3. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add the following line:

   ```shell
   API_KEY=<your_api_key_from_omdbapi>
   ```

5. Apply database migrations:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Launch the development server:

   ```shell
   python manage.py runserver
   ```

7. Open your web browser and visit `http://localhost:8000` to access the Django app.

8. Alternatively, you can also see a demo of the application at [movie.sunitro.de](http://movie.sunitro.de).
