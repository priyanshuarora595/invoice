from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'price', 'line_total']
        read_only_fields = ['line_total']

    def validate(self, data):
        """
        Calculate line_total based on quantity and price
        """
        quantity = data.get('quantity')
        price = data.get('price')
        if quantity and price:
            data['line_total'] = quantity * price
        return data

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        
        # Update invoice fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Delete existing details
        instance.details.all().delete()
        
        # Create new details
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=instance, **detail_data)
        
        return instance

    def validate_invoice_number(self, value):
        """
        Validate invoice number format and uniqueness
        """
        if not value.startswith('INV'):
            raise serializers.ValidationError(
                "Invoice number must start with 'INV'"
            )
        return value