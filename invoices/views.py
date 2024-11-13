from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import Invoice
from .serializers import InvoiceSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    @swagger_auto_schema(
        operation_description="Create a new invoice with details",
        responses={201: InvoiceSerializer()}
    )
    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing invoice with details",
        responses={200: InvoiceSerializer()}
    )
    def update(self, request, *args, **kwargs):
        with transaction.atomic():
            return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        with transaction.atomic():
            instance.details.all().delete()
            instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)