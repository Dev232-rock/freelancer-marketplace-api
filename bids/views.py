from rest_framework import generics
from .models import Bid
from .serializers import BidSerializer
from rest_framework.permissions import IsAuthenticated

class BidListCreateView(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]
