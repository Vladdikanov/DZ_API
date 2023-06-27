# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorAllSerializer


class CreateAndShowAllAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorAllSerializer

class UdateAndShowOne(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
