from django.urls import path

from measurement.views import CreateAndShowAPIView, UdateAndShowOne,CreateMeasurement

urlpatterns = [
    path('sensors/',CreateAndShowAPIView.as_view()),
    path('sensors/<pk>/',UdateAndShowOne.as_view()),
    path('measurements/',CreateMeasurement.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
