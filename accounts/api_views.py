from accounts.serializers import CustomRegisterSerializer
from rest_auth.registration.views import RegisterView

class CustomRegistrationView(RegisterView):
    
    serializer_class = CustomRegisterSerializer