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

### API Documentation

- **Vendor Management**:

  - `POST /api/vendors/`: Create a new vendor.
  - `GET /api/vendors/`: List all vendors.
  - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
  - `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
  - `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

- **Purchase Order Tracking**:

  - `POST /api/purchase_orders/`: Create a purchase order.
  - `GET /api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
  - `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
  - `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
  - `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

- **Vendor Performance Evaluation**:

  - `GET /api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

- **Token Authentication**:
  - Endpoints for token authentication.

## 🤝 Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
