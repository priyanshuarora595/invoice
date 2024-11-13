# Invoice API Project

This is a Django REST Framework project for managing invoices and their details.

## Features

- Create and update invoices with multiple line items in a single API call
- Automatic calculation of line totals
- Input validation for all fields
- API documentation with Swagger/ReDoc
- Transaction management for data integrity
- Comprehensive test suite

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/priyanshuarora595/invoice.git
   cd invoice-project
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/invoices/`: Create a new invoice with details
- `PUT /api/invoices/{id}/`: Update an existing invoice with details
- `GET /api/invoices/`: List all invoices
- `GET /api/invoices/{id}/`: Retrieve a specific invoice
- `DELETE /api/invoices/{id}/`: Delete an invoice

API documentation is available at:

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Assumptions

1. Invoice numbers must start with "INV"
2. Line totals are calculated automatically based on quantity and price
3. All monetary values are stored with 2 decimal places
4. Quantities must be positive integers
5. Prices must be positive decimal numbers
6. When updating an invoice, all existing details are replaced with the new ones
7. Database transactions are used to ensure data consistency

## Testing

Run the test suite:

```bash
python manage.py test
```
