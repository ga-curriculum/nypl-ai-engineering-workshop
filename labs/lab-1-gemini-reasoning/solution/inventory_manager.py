"""
Inventory Manager — Reference Solution for Lab 1

This module manages a simple product inventory for a bookstore.
Issues from the starter code have been identified and fixed.
"""

import json
import os
from pathlib import Path
from typing import Any

INVENTORY_FILE = "inventory.json"


def load_inventory(filepath: str = INVENTORY_FILE) -> list[dict[str, Any]]:
    """Load inventory from a JSON file.

    Args:
        filepath: Path to the inventory JSON file.

    Returns:
        List of book dictionaries. Empty list if file doesn't exist.
    """
    path = Path(filepath)
    if not path.exists():
        return []

    with open(path) as f:
        data = json.load(f)

    return data


def save_inventory(data: list[dict[str, Any]], filepath: str = INVENTORY_FILE) -> None:
    """Save inventory to a JSON file.

    Args:
        data: List of book dictionaries to save.
        filepath: Path to the inventory JSON file.
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def search_books(inventory: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Search books by title or author.

    Args:
        inventory: List of book dictionaries.
        query: Search string to match against title or author.

    Returns:
        List of matching books (no duplicates).
    """
    if not query:
        return []

    results = []
    query_lower = query.lower()

    for book in inventory:
        title = book.get("title", "")
        author = book.get("author", "")

        if query_lower in title.lower() or query_lower in author.lower():
            results.append(book)

    return results


def calculate_total_value(inventory: list[dict[str, Any]]) -> float:
    """Calculate the total value of all inventory.

    Args:
        inventory: List of book dictionaries.

    Returns:
        Total value (price * quantity) across all items.
    """
    if not inventory:
        return 0.0

    return sum(
        book.get("price", 0) * book.get("quantity", 0)
        for book in inventory
    )


def apply_discount(
    inventory: list[dict[str, Any]], category: str, discount: float
) -> list[dict[str, Any]]:
    """Apply a percentage discount to all books in a category.

    Args:
        inventory: List of book dictionaries.
        category: Category to apply discount to.
        discount: Discount as a decimal (e.g., 0.1 for 10%).

    Returns:
        Updated inventory with discounted prices.

    Raises:
        ValueError: If discount is not between 0 and 1.
    """
    if not 0 <= discount <= 1:
        raise ValueError(f"Discount must be between 0 and 1, got {discount}")

    for book in inventory:
        if book.get("category") == category:
            book["price"] = round(book["price"] * (1 - discount), 2)

    return inventory


def get_low_stock(
    inventory: list[dict[str, Any]], threshold: int = 5
) -> list[dict[str, Any]]:
    """Get books with stock below a threshold.

    Args:
        inventory: List of book dictionaries.
        threshold: Stock level below which a book is considered low stock.

    Returns:
        List of books with quantity below the threshold.
    """
    return [
        book for book in inventory
        if book.get("quantity", 0) < threshold
    ]


def add_book(
    inventory: list[dict[str, Any]],
    title: str,
    author: str,
    price: float,
    quantity: int,
    category: str,
) -> list[dict[str, Any]]:
    """Add a new book to the inventory.

    Args:
        inventory: List of book dictionaries.
        title: Book title.
        author: Book author.
        price: Book price.
        quantity: Number in stock.
        category: Book category.

    Returns:
        Updated inventory with the new book added.
    """
    book = {
        "title": title,
        "author": author,
        "price": price,
        "quantity": quantity,
        "category": category,
    }
    inventory.append(book)
    return inventory


def remove_book(inventory: list[dict[str, Any]], title: str) -> list[dict[str, Any]]:
    """Remove a book from inventory by title.

    Args:
        inventory: List of book dictionaries.
        title: Title of the book to remove.

    Returns:
        Updated inventory with the book removed.
    """
    return [book for book in inventory if book.get("title") != title]


def get_books_by_category(
    inventory: list[dict[str, Any]], category: str
) -> list[dict[str, Any]]:
    """Get all books in a specific category.

    Args:
        inventory: List of book dictionaries.
        category: Category to filter by.

    Returns:
        List of books in the specified category.
    """
    return [book for book in inventory if book.get("category") == category]


def generate_report(inventory: list[dict[str, Any]]) -> str:
    """Generate a formatted inventory report.

    Args:
        inventory: List of book dictionaries.

    Returns:
        Formatted string report of all inventory.
    """
    lines = [
        "INVENTORY REPORT",
        "================",
        "",
    ]

    for book in inventory:
        lines.extend([
            f"Title: {book.get('title', 'Unknown')}",
            f"Author: {book.get('author', 'Unknown')}",
            f"Price: ${book.get('price', 0):.2f}",
            f"Stock: {book.get('quantity', 0)}",
            f"Category: {book.get('category', 'Uncategorized')}",
            "---",
        ])

    total_value = calculate_total_value(inventory)
    lines.extend([
        "",
        f"Total items: {len(inventory)}",
        f"Total value: ${total_value:.2f}",
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    inv = load_inventory("sample_inventory.json")
    print(generate_report(inv))
    results = search_books(inv, "python")
    print(f"\nFound {len(results)} results for 'python'")
