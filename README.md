# Product Catalog Capstone

## Live Application

**Live URL:**
https://capstone-johnny.pathway4.click

**GitHub Repository:**
https://github.com/jjdavis-dev/product-catalog-capstone

---

## Overview

The Product Catalog Capstone is a full-stack inventory management application built using React, Flask, PostgreSQL, AWS EC2, Nginx, Gunicorn, n8n, and AWS Bedrock AI.

The application allows users to manage products through a web interface while also providing an AI-powered chat assistant capable of answering questions about the product catalog using live data from the PostgreSQL database.

---

## Features

### Product Management

* View all products
* Add new products
* Edit existing products
* Store product information in PostgreSQL

### AI Product Assistant

* Embedded n8n chat widget
* AWS Bedrock AI integration
* PostgreSQL Tool integration
* Answers questions using live database data
* Provides inventory summaries and product information

### Cloud Deployment

* Hosted on AWS EC2
* Flask backend served through Gunicorn
* Nginx reverse proxy
* PostgreSQL database hosted on AWS RDS
* SSL secured using HTTPS

---

## Technology Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* Flask
* Flask-CORS
* Gunicorn

### Database

* PostgreSQL
* AWS RDS

### AI & Automation

* n8n
* AWS Bedrock
* PostgreSQL Tool

### Hosting & Infrastructure

* AWS EC2
* Nginx
* Route 53
* SSL Certificate

---

## Database Structure

### Schema

```sql
catalog
```

### Table

```sql
products
```

### Columns

| Column   | Type    |
| -------- | ------- |
| id       | SERIAL  |
| name     | VARCHAR |
| price    | DECIMAL |
| quantity | INTEGER |

---

## API Endpoints

### Get Products

```http
GET /products/
```

### Add Product

```http
POST /products/
```

### Update Product

```http
PUT /products/<id>
```

### Product Count

```http
GET /products/count
```

### Product Summary

```http
GET /products/summary
```

---

## AI Assistant Examples

The AI assistant can answer questions such as:

* How many products are in the catalog?
* What is the most expensive product?
* Which product has the lowest quantity?
* List the first five products.
* What is the average product price?

The AI assistant retrieves live information directly from the PostgreSQL database using n8n and AWS Bedrock.

---

## Application Architecture

```text
React Frontend
        ↓
Flask API
        ↓
PostgreSQL Database

React Frontend
        ↓
n8n Chat Widget
        ↓
AWS Bedrock AI
        ↓
PostgreSQL Tool
        ↓
catalog.products
```

---

## Deployment Process

1. Build React application using Vite
2. Copy production build into Flask templates and static folders
3. Deploy application to AWS EC2
4. Run Flask application using Gunicorn
5. Configure Nginx as reverse proxy
6. Configure Route 53 domain
7. Install SSL certificate
8. Publish n8n workflow
9. Connect embedded chat assistant

---

## Project Files

* Source Code
* n8n Workflow Export
* Deployment Screenshots
* README Documentation

---

## Author

Johnny Davis

CodeX Academy – Pathway 4 Capstone Project
