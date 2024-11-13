from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail
from decimal import Decimal
from django.urls import reverse

class InvoiceTests(APITestCase):
    def setUp(self):
        self.invoice_data = {
            "invoice_number": "INV001",
            "customer_name": "Test Customer",
            "date": "2024-11-12",
            "details": [
                {
                    "description": "Product A",
                    "quantity": 2,
                    "price": "50.00",
                },
                {
                    "description": "Product B",
                    "quantity": 1,
                    "price": "75.00",
                }
            ]
        }

    def test_create_invoice(self):
        url = reverse('invoice-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    def test_update_invoice(self):
        # First create an invoice
        create_url = reverse('invoice-list')
        response = self.client.post(create_url, self.invoice_data, format='json')
        invoice_id = response.data['id']

        # Update the invoice
        update_url = reverse('invoice-detail', args=[invoice_id])
        updated_data = self.invoice_data.copy()
        updated_data['customer_name'] = "Updated Customer"
        response = self.client.put(update_url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], "Updated Customer")

    def test_invalid_invoice_number(self):
        url = reverse('invoice-list')
        invalid_data = self.invoice_data.copy()
        invalid_data['invoice_number'] = "123"  # Should start with INV
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
