import razorpay
from django import views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.core.mail import send_mail
from django.contrib import messages
from core import models as core_models
from core.forms import FeedbackForm
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.core.serializers import json


# ============================ Core Views start ====================================#
class HomeView(views.TemplateView):
    template_name = "core/home.html"
    extra_context = {
        "songs": core_models.SongModel.objects.all(),
        "artists":core_models.ArtistModel.objects.all(),
        "genres":core_models.GenreModel.objects.all(),
    }

    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
    #     songs = core_models.SongModel.objects.all()
    #     context.update({"songs":songs})
    #     return context


class AboutUsView(views.TemplateView):
    template_name = "core/about_us.html"


# ============================ Core Views end ======================================#


# ===========================Feedback Cred start====================================#

# feedback create view
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback/feedback_create.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        response =  super().form_valid(form)
        # send mail
        try:
            data = form.cleaned_data
            email_to = data["email"]
            from_email = settings.EMAIL_HOST_USER
            subject = "Thank you for your valuable feedback"
            name = data["name"]
            message = f"""
            Hi {name},

            This is autogenerated mail. 
            We will reach you very soon.
            
            Thank you,
            Ecart Team
            """
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=[email_to],
            )
            messages.success(self.request, "Feedback sent successfully!")
        except Exception as e:
            print("error", e)
            messages.error(self.request, "Feedback sent failed!")
            return redirect(self.success_url)
        return response

class FeedbackDeleteView(views.DeleteView):
    template_name = "core/feedback/delete_feedback.html"
    model = core_models.FeedbackModel
    success_url = reverse_lazy("core:feedback_list")


class FeedbackUpdateView(views.UpdateView):
    template_name = "core/feedback/update_feedback.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:feedback_list")


class FeedbackListView(views.ListView):
    template_name = "core/feedback/feedback_list.html"
    model = core_models.FeedbackModel
    context_object_name = "feedbacks"


# feedback detailview
class FeedbackDetailView(views.DetailView):
    template_name = "core/feedback/feedback_detail.html"
    model = core_models.FeedbackModel
    context_object_name = "feedback"


# ===========================Feedback Cred end======================================#

# ===========================Song Cred Start======================================#


class PlayerView(views.DetailView):
    template_name = "core/player.html"
    model = core_models.SongModel
    context_object_name = "song"
    


class FavouriteView(views.TemplateView):
    template_name = "core/favourites.html"


class GenreView(views.TemplateView):
    template_name = "core/genre.html"
    extra_context = {
        "genres":core_models.GenreModel.objects.all(),
    }
class GenreDetailView(views.DetailView):
    template_name = "core/genredetail.html"
    model = core_models.GenreModel
    context_object_name = "genre"
    extra_context = {
        "songs": core_models.SongModel.objects.all(),
    }
class PlaylistView(views.ListView):
    template_name = "core/playlist.html"

class PlaylistDetailView(views.DetailView):
    template_name = "core/playlistdetail.html"


class QueueView(views.DetailView):
    template_name = "core/queue.html"
    model = core_models.SongModel
    context_object_name = "song"





# ===========================Song Cred End======================================#


# ===========================Room Views Start===================================#

class HostView(views.TemplateView):
    template_name = "core/room/host.html"
    
class JoinView(views.TemplateView):
    template_name = "core/room/join.html"

# ===========================Room Views End=====================================#


# ===========================Subscription Start=================================#

class PaymentView(views.View):
    def get(self, request):

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )
        payment = client.order.create(  # type: ignore
            {"amount": 10000, "currency": "INR", "payment_capture": "1"}
        )


# ===========================Subscription End====================================#


class SongsAPIView(views.View):
    model = core_models.SongModel
    
    def get(self, request, *args, **kwargs):
        data = self.get_context_data()["songs"]
        songs = self.model.objects.filter().order_by("-name")
        song_serializer = json.Serializer()
        songs_json = song_serializer.serialize(songs)
        print(songs_json)
        return JsonResponse(songs_json, safe=False)

    def get_context_data(self):
        songs = self.model.objects.filter().order_by("-name")
        context = {
            "songs" : songs
        }
        return context

