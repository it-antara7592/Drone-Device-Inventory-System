# Drone Device Inventory Management System

A Python-driven NoSQL database application built with **PyMongo** to manage drone device inventories. This system transitions drone tracking from manual spreadsheets and paper logs into a centralized MongoDB database, supporting full inventory control across device lifecycles, maintenance schedules, operator assignments, and operational status monitoring.

---

## Case Study Overview

A drone technology company operating devices across aerial photography, agriculture, surveillance, mapping, and delivery services faces operational bottlenecks from spreadsheet-based tracking. This manual approach leads to duplicate records, untracked maintenance, missing equipment, and location errors. 

This **MongoDB Drone Device Inventory System** provides a menu-driven command-line application executing real-time CRUD operations to streamline inventory management and ensure accurate device tracking.

---

## System Architecture & Database Configuration

- **Database Engine:** MongoDB (NoSQL)
- **Database Name:** `DDInventorySystem_414`
- **Collection Name:** `DroneDevices_414`
- **Driver / Library:** `pymongo` (MongoDB Python Driver)
- **Host / Port:** `localhost:27017`

### Data Schema (Sample Document)

json
{
  "_id": { "$oid": "6891a123456789abcdef1234" },
  "droneId": "DRN001",
  "model": "DJI Matrice 300 RTK",
  "manufacturer": "DJI",
  "serialNumber": "DJI30098765",
  "batteryCapacity": "5935 mAh",
  "status": "Available",
  "purchaseDate": "2025-02-10",
  "location": "Warehouse A",
  "assignedOperator": "John Smith",
  "maintenanceDate": "2026-07-15",
  "conditionStatus": "Working"
}


## Features & CRUD Capabilities

### 1. Create (Insert Drone Record)
- Prompts input for essential hardware and operational fields.
- Features strict input validation loops for:
  - **Operational Status:** Restricted to `Available`, `Working`, or `Unavailable`.
  - **Condition Status:** Restricted to `Working`, `Repair`, or `Obsolete`.
- Automatically formats standard attributes like `droneId` and `serialNumber` to uppercase.

### 2. Read (Display & Search)
- **Read All Records:** Fetches and displays all documents stored in the `DroneDevices_414` collection.
- **Granular Search Menu:** Supports query lookup across 11 specific fields:
  1. **Drone ID** (Unique single match using `find_one`)
  2. **Model Number**
  3. **Manufacturer**
  4. **Serial Number** (Unique single match using `find_one`)
  5. **Battery Capacity**
  6. **Operational Status**
  7. **Purchase Date** (`YYYY-MM-DD`)
  8. **Location**
  9. **Assigned Operator**
  10. **Maintenance Date** (`YYYY-MM-DD`)
  11. **Condition Status**

### 3. Update (Modify Existing Records)
- Locates target drone by `droneId`.
- Provides targeted attribute updates for dynamic fields:
  - **Operational Status** (validated)
  - **Current Location**
  - **Assigned Operator**
  - **Maintenance Date**
  - **Condition Status** (validated)

### 4. Delete (Purge Records)
- **Obsolete Purge:** Safely removes drones marked with `conditionStatus = 'Obsolete'` after user confirmation (`yes`/`no`).
- **Bulk Delete:** Purges the entire inventory collection (`delete_many({})`).

---

## Tech Stack & Requirements

- **Python:** 3.x
- **MongoDB Server:** Local Community Edition running on default port `27017`
- **Dependencies:** `pymongo`

---

## Setup & Installation

### Step 1: Save the Application Script
Save the provided code in your project directory as `drone_inventory.py`.

### Step 2: Install Required Dependencies
Ensure you have `pymongo` installed in your Python environment:

```bash
pip install pymongo
## Interactive Menu Interface

Inventory Operations Menu 

1. Insert Drone Data
2. Read All Drone Data
3. Update a Drone Data
4. Search a Drone Data
5. Delete Drone Data having Obsolete Condition
6. Delete All Drone Data
7. Exit

## Field Specifications & Validation Rules

Field Input Format / Allowed Values Validation Constraint
Drone ID String (e.g., DRN001) Converted to Uppercase
Serial Number String (e.g., SN123456) Converted to Uppercase
Status Available, Working, Unavailable Loop validation (Title Case)
Condition Status Working, Repair, Obsolete Loop validation (Title Case)
Dates YYYY-MM-DD String input format

## Error Handling
All database operations and interactive inputs are wrapped in try-except blocks to catch execution errors gracefully without breaking the interactive CLI session.




