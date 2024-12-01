from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    # path(route='register', view=views.register_user, name='register'),

    # Path for login
    # path(route='login', view=views.login_user, name='login'),

    # Path for dealer reviews view
    # path(route='dealer_reviews/<int:dealer_id>', view=views.dealer_reviews, name='dealer_reviews'),

    # Path for adding a review view
    
    path(route='add_review', view=views.add_review, name='add_review'),

    # path(route='add_review/<int:dealer_id>', view=views.add_review, name='add_review'),
    # path for reviews from dealer_id
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
    # Path for getting all dealers
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),

    # Path for getting dealers by state
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
