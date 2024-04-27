# Vendor Management System 💼

Vendor Management System is a comprehensive web application developed using Django and Django REST Framework. It provides functionalities to manage vendors, track purchase orders, and evaluate vendor performance metrics.

## 🚀 Features

- **Vendor Profile Management**:

  - Create, update, retrieve, and delete vendor profiles.
  - Store essential information about each vendor including name, contact details, address, and a unique vendor code.

- **Purchase Order Tracking**:

  - Create, update, retrieve, and delete purchase orders.
  - Track details of each purchase order such as PO number, vendor reference, order date, items, quantity, and status.

- **Vendor Performance Evaluation**:

  - Calculate various performance metrics for vendors including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
  - Retrieve performance metrics for a specific vendor.

- **Token-based Authentication**:
  - Secure API endpoints with token-based authentication.
  - Obtain tokens for users to authenticate and access protected endpoints.

## 🛠️ Get Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/VitthalGund/vendor-management-system.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd vendor-management-system
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the API endpoints** at `http://localhost:8000/api/`.

### Vendor Management System API Documentation 📝

Welcome to the API documentation for the Vendor Management System. This documentation provides detailed information about each API endpoint, including the type of request, data passed, and the expected response.

## Base URL

All API endpoints are relative to the base URL:

```
http://localhost:8000/api/
```

## Authentication

The API endpoints require token-based authentication. To authenticate, obtain a token using the following endpoint:

- **Token Obtainment**: `POST /api/token/`

### Request

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Response

```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

Include the access token in the Authorization header for subsequent requests.

## Endpoints

### Vendor Management

#### Create a New Vendor

- **Request Type**: `POST`
- **Endpoint**: `/api/vendors/`
- **Data Passed**:

```json
{
  "name": "Vendor Name",
  "contact_details": "Contact Details",
  "address": "Vendor Address",
  "vendor_code": "Unique Vendor Code"
}
```

- **Return Data**: 

```json
{
  "id": 1,
  "name": "Vendor Name",
  "contact_details": "Contact Details",
  "address": "Vendor Address",
  "vendor_code": "Unique Vendor Code",
  "on_time_delivery_rate": 0.0,
  "quality_rating_avg": 0.0,
  "average_response_time": 0.0,
  "fulfillment_rate": 0.0
}
```

#### List All Vendors

- **Request Type**: `GET`
- **Endpoint**: `/api/vendors/`
- **Return Data**:

```json
[
  {
    "id": 1,
    "name": "Vendor Name",
    "contact_details": "Contact Details",
    "address": "Vendor Address",
    "vendor_code": "Unique Vendor Code",
    "on_time_delivery_rate": 0.0,
    "quality_rating_avg": 0.0,
    "average_response_time": 0.0,
    "fulfillment_rate": 0.0
  },
  { ... }
]
```

#### Retrieve a Specific Vendor

- **Request Type**: `GET`
- **Endpoint**: `/api/vendors/{vendor_id}/`
- **Return Data**:

```json
{
  "id": 1,
  "name": "Vendor Name",
  "contact_details": "Contact Details",
  "address": "Vendor Address",
  "vendor_code": "Unique Vendor Code",
  "on_time_delivery_rate": 0.0,
  "quality_rating_avg": 0.0,
  "average_response_time": 0.0,
  "fulfillment_rate": 0.0
}
```

#### Update a Vendor

- **Request Type**: `PUT`
- **Endpoint**: `/api/vendors/{vendor_id}/`
- **Data Passed**:

```json
{
  "name": "Updated Vendor Name",
  "contact_details": "Updated Contact Details",
  "address": "Updated Vendor Address",
  "vendor_code": "Updated Unique Vendor Code"
}
```

- **Return Data**: Same as Retrieve a Specific Vendor

#### Delete a Vendor

- **Request Type**: `DELETE`
- **Endpoint**: `/api/vendors/{vendor_id}/`
- **Return Data**: HTTP 204 No Content

### Purchase Order Tracking

#### Create a New Purchase Order

- **Request Type**: `POST`
- **Endpoint**: `/api/purchase_orders/`
- **Data Passed**:

```json
{
  "po_number": "PO-001",
  "vendor": 1,
  "order_date": "2024-04-30T12:00:00Z",
  "delivery_date": "2024-05-10T12:00:00Z",
  "items": [
    {
      "name": "Item 1",
      "quantity": 10,
      "price": 50.00
    },
    { ... }
  ]
}
```

- **Return Data**:

```json
{
  "id": 1,
  "po_number": "PO-001",
  "vendor": 1,
  "order_date": "2024-04-30T12:00:00Z",
  "delivery_date": "2024-05-10T12:00:00Z",
  "items": [
    {
      "name": "Item 1",
      "quantity": 10,
      "price": 50.00
    },
    { ... }
  ],
  "status": "pending"
}
```

#### List All Purchase Orders

- **Request Type**: `GET`
- **Endpoint**: `/api/purchase_orders/`
- **Return Data**: Same as Create a New Purchase Order

#### Retrieve a Specific Purchase Order

- **Request Type**: `GET`
- **Endpoint**: `/api/purchase_orders/{po_id}/`
- **Return Data**: Same as Create a New Purchase Order

#### Update a Purchase Order

- **Request Type**: `PUT`
- **Endpoint**: `/api/purchase_orders/{po_id}/`
- **Data Passed**: Same as Create a New Purchase Order
- **Return Data**: Same as Create a New Purchase Order

#### Delete a Purchase Order

- **Request Type**: `DELETE`
- **Endpoint**: `/api/purchase_orders/{po_id}/`
- **Return Data**: HTTP 204 No Content

### Vendor Performance Evaluation

#### Retrieve Vendor Performance Metrics

- **Request Type**: `GET`
- **Endpoint**: `/api/vendors/{vendor_id}/performance/`
- **Return Data**:

```json
{
  "on_time_delivery_rate": 95.0,
  "quality_rating_avg": 4.5,
  "average_response_time": 3.5,
  "fulfillment_rate": 98.0
}
```
 ##### Note: This a brief introduction of all listed api's please checkout ```urls.py``` file in particular app for more.

## 🤝 Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
