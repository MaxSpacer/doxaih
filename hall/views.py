from django.shortcuts import render
from .models import Preference

# Create your views here.
# def hall(request):
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#     return render(request, 'hall/hall.html', locals())
