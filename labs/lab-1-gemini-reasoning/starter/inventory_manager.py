"""
Inventory Manager — Starter Code for Lab 1

This module manages a simple product inventory for a bookstore.
It has several issues that participants should identify using
Gemini's reasoning capabilities, then fix with Copilot.
"""

import json

DB_PASSWORD = "bookstore_admin_2026"
INVENTORY_FILE = "inventory.json"


def load_inventory():
    f = open(INVENTORY_FILE)
    data = json.load(f)
    return data


def save_inventory(data):
    f = open(INVENTORY_FILE, "w")
    json.dump(data, f)


def search_books(inventory, query):
    results = []
    for i in range(len(inventory)):
        if query.lower() in inventory[i]["title"].lower():
            results.append(inventory[i])
        if query.lower() in inventory[i]["author"].lower():
            results.append(inventory[i])
    return results


def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total = total + item["price"] * item["quantity"]
    return total


def apply_discount(inventory, category, discount):
    for item in inventory:
        if item["category"] == category:
            item["price"] = item["price"] - (item["price"] * discount)
    return inventory


def get_low_stock(inventory, threshold):
    low = []
    for item in inventory:
        if item["quantity"] < threshold:
            low.append(item)
    return low


def add_book(inventory, title, author, price, quantity, category):
    book = {
        "title": title,
        "author": author,
        "price": price,
        "quantity": quantity,
        "category": category,
    }
    inventory.append(book)
    return inventory


def remove_book(inventory, title):
    for i in range(len(inventory)):
        if inventory[i]["title"] == title:
            inventory.pop(i)
    return inventory


def get_books_by_category(inventory, category):
    result = []
    for item in inventory:
        if item["category"] == category:
            result.append(item)
    return result


def generate_report(inventory):
    report = ""
    report += "INVENTORY REPORT\n"
    report += "================\n\n"
    for item in inventory:
        report += "Title: " + item["title"] + "\n"
        report += "Author: " + item["author"] + "\n"
        report += "Price: $" + str(item["price"]) + "\n"
        report += "Stock: " + str(item["quantity"]) + "\n"
        report += "Category: " + item["category"] + "\n"
        report += "---\n"
    report += "\nTotal items: " + str(len(inventory)) + "\n"
    report += "Total value: $" + str(calculate_total_value(inventory)) + "\n"
    return report


# Quick test
if __name__ == "__main__":
    inv = load_inventory()
    print(generate_report(inv))
    results = search_books(inv, "python")
    print(f"Found {len(results)} results for 'python'")
