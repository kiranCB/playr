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
import core.payment as payment
from core import payment


# ============================ Core Views start ====================================#
class HomeView(views.TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "songs": core_models.SongModel.objects.all(),
                "artists": core_models.ArtistModel.objects.all(),
                "genres": core_models.GenreModel.objects.all(),
                "favorite_lists": core_models.FavouriteListModel.objects.filter(
                    user=self.request.user
                ),
            }
        )
        return context


class AboutUsView(views.TemplateView):
    template_name = "core/about_us.html"

# ============================ Core Views end ======================================#


# ===========================Subscription Start=================================#
class PaymentView(LoginRequiredMixin, views.View):
    template_name = "core/pay.html"
    RAZORPAY_CLIENT = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        service = core_models.ServiceModel.objects.get(id=pk)
        client = self.RAZORPAY_CLIENT
        # params
        amount = service.cost
        currency = "INR"
        payment_capture = "1"
        callback_url = reverse_lazy("core:payment_completed", kwargs={"pk":kwargs.get("pk")})

        order = payment.create_order(
            client, amount, callback_url, receipt=None, currency=currency
        )
        print(order)
        context = {}
        context.update(order)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get("razorpay_payment_id", "")
            amount = request.POST.get("razorpay_amount", "0")
            razorpay_order_id = request.POST.get("razorpay_order_id", "")
            signature = request.POST.get("razorpay_signature", "")

            params_dict = {
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature,
            }
            print("#DEBUG: Amount", type(amount), amount)
            try:
                amount = int(float(amount))/100
            except Exception as e:
                print("#DEBUG: amount can be converted into integer", e)
                amount = 5000
            print("#DEBUG: verifying the payment signature...", params_dict, amount)

            # verify the payment signature.
            result = self.RAZORPAY_CLIENT.utility.verify_payment_signature(params_dict)
            print("#DEBUG: verifying the payment signature... Completed.") 

            if result is not None:

                try:
                    print("#DEBUG: Payment capturing...")
                    # capture the payment
                    self.RAZORPAY_CLIENT.payment.capture(payment_id, amount)
                    print("#DEBUG: Payment captured...")
                    print("#DEBUG: Payment model creating...")

                    core_models.Payment.objects.create(
                        razorpay_order_id=razorpay_order_id,
                        razorpay_payment_id=payment_id,
                        status=core_models.Payment.PaymentStatusChoices.completed,
                        mode="",
                    )
                    print("#DEBUG: Payment model created...")


                    # render success page on successful caputre of payment
                    return render(request, "core/paymentsuccess.html")
                except Exception as e:
                    print("#DEBUG: there is an error while capturing payment...", e)
                    
                    # if there is an error while capturing payment.
                    return render(request, "core/paymentfail.html")
            else:
                print("#DEBUG: signature verification failed...", e)
                # if signature verification fails.
                return render(request, "core/paymentfail.html")
        except Exception as e:
            print("#DEBUG: we don't find the required parameters in POST data", e)
            # if we don't find the required parameters in POST data
            return redirect(reverse_lazy("core:payment_completed", kwargs={"pk":self.kwargs.get("pk")}))

# ===========================Subscription End====================================#




# ===========================Feedback Cred start====================================#

# feedback create view
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback/feedback_create.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        response = super().form_valid(form)
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


class GenreView(views.TemplateView):
    template_name = "core/genre.html"
    extra_context = {
        "genres": core_models.GenreModel.objects.all(),
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


class FavouriteView(views.ListView):
    template_name = "core/favourites.html"
    model = core_models.FavouriteItemModel
    context_object_name = "favourites"


class AddToFavouriteView(views.View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        song = core_models.SongModel.objects.get(id=pk)
        favourite_list_id = request.POST.get("favorite_list")
        favourite_list = core_models.FavouriteListModel.objects.get(
            id=favourite_list_id
        )
        favorite_item, created = core_models.FavouriteItemModel.objects.get_or_create(
            favourite_list=favourite_list,
            song=song,
        )
        url = request.META.get("HTTP_REFERER", "/")
        return redirect(url)


# ===========================Song Cred End======================================#


# ===========================Room Views Start===================================#


class HostView(views.TemplateView):
    template_name = "core/room/host.html"

class HostDetailView(views.DetailView):
    template_name = "core/room/hostroom.html"
    model = core_models.HostModel
    context_object_name = "host"


class JoinView(views.TemplateView):
    template_name = "core/room/join.html"


# ===========================Room Views End=====================================#





# ===========================Song Api End====================================#
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
        context = {"songs": songs}
        return context
