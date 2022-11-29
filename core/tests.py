from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core import models as core_models
from core import forms as core_forms


class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse("core:home")
        response = self.client.get(url)
        status_code = response.status_code
        self.assertEquals(status_code, 200)

class AboutUsViewTest(TestCase):
    def test_aboutus_view_status_code(self):
        url = reverse("core:about_us")
        response = self.client.get(url)
        status_code = response.status_code
        self.assertEquals(status_code,200) 
class FeedbackViewTest(TestCase):

    def create_feedback(
        self,
        name="Kiran",
        email="playr.kiran@gmail.com",
        subject="Some Test",
        message="Some message",
    ):
        feedback_object = core_models.FeedbackModel.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return feedback_object

    def test_feedback_model_object_create(self):
        feedback_object = self.create_feedback()

    def test_Feedback_create_view_get_status_code(self):
        url = reverse("core:feedback")
        response = self.client.get(url)
        status_code = response.status_code
        self.assertEquals(status_code,200) 
    
    def test_Feedback_create_view_post_status_code(self):
        url = reverse("core:feedback")
        data = {
            "name":"Kiran",
            "email":"playr.kiran@gmail.com",
            "subject":"Some Test",
            "message":"Some message",
            }
        response = self.client.get(url,data=data)
        status_code = response.status_code
        self.assertEquals(status_code,200) 

    


