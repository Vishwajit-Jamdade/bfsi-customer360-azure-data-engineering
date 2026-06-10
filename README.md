# BFSI Customer 360 Data Engineering Project

## Project Overview

This project demonstrates an end-to-end enterprise-grade Data Engineering solution for a Banking, Financial Services, and Insurance (BFSI) organization.

The objective is to build a Customer 360 platform that ingests customer and transaction data, stores it in a Data Lake, performs data transformation and enrichment, loads curated data into a Data Warehouse, and enables reporting through Power BI.

---

## Business Problem

A BFSI organization receives data from multiple operational systems:

* Customer Management System
* Account Management System
* Loan Management System
* Credit Card System
* Complaint Management System
* Transaction Processing System

Business users need:

* Single Customer View
* Customer Risk Profiling
* Loan Performance Analysis
* Complaint Analytics
* Customer Segmentation
* Executive Reporting Dashboards

---

## Technology Stack

### Data Ingestion

* Azure Data Factory (ADF)

### Data Storage

* Azure Data Lake Storage Gen2 (ADLS Gen2)

### Data Transformation

* Azure Data Factory Mapping Data Flows

### Data Warehouse

* Azure Synapse Analytics

### Reporting

* Power BI

### Version Control

* Git
* GitHub

### Dataset Generation

* Python
* Pandas
* Faker

---

## Solution Architecture

Source Files
→ Azure Data Factory
→ ADLS Gen2 Raw Layer
→ ADF Mapping Data Flows
→ ADLS Gen2 Silver Layer
→ ADF Mapping Data Flows
→ ADLS Gen2 Gold Layer
→ Azure Synapse Analytics
→ Power BI

---

## Dataset Overview

### Customers

* 100,000 Records

### Accounts

* 150,000 Records

### Loans

* 50,000 Records

### Credit Cards

* 80,000 Records

### Complaints

* 25,000 Records

### Transactions

* 2,000,000 Records

---

## Data Lake Layers

### Raw Layer

Stores source data exactly as received.

### Silver Layer

Stores cleansed and standardized data.

### Gold Layer

Stores business-ready curated datasets.

---

## Key Features

* Metadata-Driven Pipelines
* Incremental Data Loading
* Watermark Framework
* Dynamic Parameterization
* Data Validation
* Error Handling
* Audit Logging
* Customer 360 View
* Risk Profiling
* Synapse Integration
* Power BI Reporting

---

## Project Phases

### Phase 0

* Repository Setup
* Dataset Generation
* GitHub Integration

### Phase 1

* Azure Resource Provisioning
* ADLS Gen2 Setup

### Phase 2

* Azure Data Factory Setup
* Linked Services Configuration

### Phase 3

* Raw to Silver Data Pipelines

### Phase 4

* Customer Data Cleansing

### Phase 5

* Customer 360 Data Flow

### Phase 6

* Incremental Load Framework

### Phase 7

* Metadata-Driven Framework

### Phase 8

* Synapse Integration

### Phase 9

* Power BI Dashboard Development

---

## Current Status

✅ Repository Setup

✅ Dataset Generation

⬜ ADLS Gen2 Setup

⬜ Azure Data Factory Setup

⬜ Raw Layer Ingestion

⬜ Silver Layer Transformation

⬜ Gold Layer Creation

⬜ Synapse Integration

⬜ Power BI Dashboard

---

## Author

Vishwajit Sandip Jamdade

Senior Software Engineer | Data Engineering Enthusiast

Azure Data Factory | ADLS Gen2 | Synapse | Power BI | Python
