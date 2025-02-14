# SIGAS - Warehouse and Supermarket Management System

SIGAS is a shopping cart application that follows a microservices architecture. Each microservice is implemented using Flask (Python) or Express (Node.js) and communicates with a MongoDB database hosted on MongoDB Atlas. The application also includes a frontend developed with React.

## Project Overview

### Project Structure

- **Backend**: Contains multiple microservices handling different shopping cart functionalities.
  - `add_product`: Service to add products to the cart.
  - `checkout`: Payment service (currently not implemented).
  - `delete_product`: Service to remove products from the cart.
  - `get_cart`: Service to retrieve a user's cart.
  - `get_products`: Service to retrieve products.
  - `login`: User authentication service.
  - `register`: User registration service.
  - `reset_cart`: Service to empty the cart.
  - `search_products`: Service to search for products.
  - `sort_cart`: Service to sort the cart.
  - `update_quantity`: Service to update product quantities in the cart.

- **Frontend**: React application interacting with backend microservices.
  - **Components**: Login and registration forms, product search, shopping cart, etc.
  - **Pages**: Home page, product list, shopping cart, etc.

- **Node.js Services**: Additional services implemented in Node.js to add and remove products from the cart.

- **Docker**: Each microservice is containerized and orchestrated using Docker Compose.

## Key Files

- `docker-compose.yml`: Defines Docker services for each microservice.
- `.env`: Contains environment variables for database and email configuration.
- `seed_data.py`: Script to populate the database with initial data.

## New Service Examples

1. **Product Recommendation Service**
   - **Description**: Recommends products based on user purchase history.
   - **Endpoint**: `/recommendations`
   - **Method**: GET
   - **Implementation**: Uses machine learning techniques to analyze purchase history and recommend products.

2. **Purchase History Service**
   - **Description**: Allows users to view their purchase history.
   - **Endpoint**: `/purchase_history`
   - **Method**: GET
   - **Implementation**: Stores purchase history in a MongoDB collection for user queries.

3. **Notification Service**
   - **Description**: Sends email or SMS notifications to users about offers and updates.
   - **Endpoint**: `/notifications`
   - **Method**: POST
   - **Implementation**: Integrates with an email or SMS service.

4. **Inventory Management Service**
   - **Description**: Manages product inventory.
   - **Endpoint**: `/inventory`
   - **Method**: POST, GET, PATCH, DELETE
   - **Implementation**: Allows administrators to add, update, and delete products.

5. **Product Reviews Service**
   - **Description**: Allows users to leave reviews and ratings on products.
   - **Endpoint**: `/reviews`
   - **Method**: POST, GET
   - **Implementation**: Stores reviews and ratings in MongoDB.

## How to Run the Project

### Prerequisites

- Docker and Docker Compose installed.
- MongoDB Atlas configured and accessible.

### Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/sigas.git
   cd sigas
   ```

2. Configure environment variables in the `.env` file:
   ```env
   MONGO_INITDB_ROOT_USERNAME=myDockerUser
   MONGO_INITDB_ROOT_PASSWORD=myDockerPass
   MONGO_URI=mongodb://myDockerUser:myDockerPass@mongo:27017/shopping_cart?authSource=admin
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_gmail_password
   MAIL_DEFAULT_SENDER=your_email@gmail.com
   SECRET_KEY=your_secret_key
   ```

3. Build and start Docker services:
   ```sh
   docker-compose up --build
   ```

4. Access the frontend in your browser:
   ```
   http://localhost:3000
   ```

5. (Optional) Populate the database with initial data:
   ```sh
   python seed_data.py
   ```

## AWS Deployment

### Deploying to AWS with Elastic Beanstalk and MongoDB Atlas

1. **Create an AWS Elastic Beanstalk Application**
   - Go to AWS Elastic Beanstalk and create a new application.
   - Select **Docker** as the platform.
   - Upload a `Dockerfile` for your Flask/Node.js services.

2. **Configure AWS RDS (Optional, if using SQL instead of MongoDB Atlas)**
   - Create an RDS instance for PostgreSQL/MySQL.
   - Connect your backend services to RDS in the `.env` file.


3. **Push Your Code to AWS Elastic Beanstalk**
   ```sh
   eb init -p docker SIGAS-app
   eb create SIGAS-env
   ```

4. **Monitor Logs and Debug**
   ```sh
   eb logs
   ```

5. **Update Your Application**
   ```sh
   git add .
   git commit -m "Update application"
   git push origin main
   eb deploy
   ```

## CI/CD with GitHub Actions

This project uses GitHub Actions for continuous integration and deployment. Workflow files are located in the `.github/workflows/` directory.

Example for the `add_product` service:

```yaml
name: Add Product Service CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    services:
      mongo:
        image: mongo:latest
        ports:
          - 27017:27017

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r backend/add_product/requirements.txt

      - name: Run tests
        run: |
          pytest backend/add_product/tests
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/new-feature
   ```
3. Make your changes and commit:
   ```sh
   git commit -am 'Add new feature'
   ```
4. Push your changes:
   ```sh
   git push origin feature/new-feature
   ```
5. Open a Pull Request.

---

### Contact
For any questions or suggestions, feel free to reach out or create an issue in the repository. 🚀

