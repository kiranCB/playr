import razorpay
from django import views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views


from core import models as core_models
from core.forms import FeedbackForm
from django.conf import settings


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


class HostView(views.TemplateView):
    template_name = "core/room/host.html"
    


class JoinView(views.TemplateView):
    template_name = "core/room/join.html"


class PlaylistView(views.TemplateView):
    template_name = "core/playlist.html"


class QueueView(views.TemplateView):
    template_name = "core/queue.html"


class GenreDetailView(views.TemplateView):
    template_name = "core/genredetail.html"


class PlaylistDetailView(views.TemplateView):
    template_name = "core/playlistdetail.html"


# ===========================Song Cred End======================================#

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