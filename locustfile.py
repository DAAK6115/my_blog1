from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def about_page(self):
        self.client.get("/about/")  # Test de la vue "about"

    @task(1)
    def contact_page(self):
        self.client.get("/about/contact")  # Test de la vue "contact"

    @task(2)
    def poeme_page(self):
        self.client.get("/oeuvre/")  # Test de la vue "poeme"

    @task(1)
    def index_page(self):
        self.client.get("/")  # Test de la vue principale

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    host = "http://127.0.0.1:8000"  # URL de base de votre application
    wait_time = between(1, 5)  # Temps d'attente aléatoire entre 1 et 5 secondes
