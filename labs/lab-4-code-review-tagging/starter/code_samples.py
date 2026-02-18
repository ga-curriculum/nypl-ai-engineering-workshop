"""
Lab 4: Code Review and Tagging — Code Samples

Review each code sample below. For each one, determine whether it is:
  - AI-Generated: Written entirely by an AI tool
  - AI-Assisted: Written by a human with AI suggestions accepted
  - Human-Written: Written entirely by a human

Then apply the Security Auditor persona to any AI-generated samples.
"""


# ============================================================
# SAMPLE A
# ============================================================

def validate_user_input(data: dict) -> tuple[bool, list[str]]:
    """Validate user registration data.

    Args:
        data: Dictionary containing user registration fields.

    Returns:
        Tuple of (is_valid, list_of_errors).
    """
    errors: list[str] = []

    if not data.get("username"):
        errors.append("Username is required")
    elif len(data["username"]) < 3:
        errors.append("Username must be at least 3 characters")
    elif len(data["username"]) > 50:
        errors.append("Username must be at most 50 characters")

    if not data.get("email"):
        errors.append("Email is required")
    elif "@" not in data["email"]:
        errors.append("Email must contain @")
    elif "." not in data["email"].split("@")[-1]:
        errors.append("Email domain must contain a period")

    if not data.get("password"):
        errors.append("Password is required")
    elif len(data["password"]) < 8:
        errors.append("Password must be at least 8 characters")
    elif not any(c.isupper() for c in data["password"]):
        errors.append("Password must contain at least one uppercase letter")
    elif not any(c.isdigit() for c in data["password"]):
        errors.append("Password must contain at least one digit")

    return (len(errors) == 0, errors)


# ============================================================
# SAMPLE B
# ============================================================

def calc_shipping(weight, dest):
    # domestic
    if dest == "US":
        if weight < 1:
            return 5.99
        elif weight < 5:
            return 8.99
        elif weight < 20:
            return 12.99
        else:
            return 12.99 + (weight - 20) * 0.50
    # canada
    elif dest == "CA":
        if weight < 1:
            return 9.99
        elif weight < 5:
            return 14.99
        else:
            return 14.99 + (weight - 5) * 0.75
    # international - just a flat calculation for now
    # TODO: need to get real rates from API, asked matt about this 2/3
    else:
        return 24.99 + weight * 1.25


# ============================================================
# SAMPLE C
# ============================================================

from typing import Any, Optional
from datetime import datetime, timezone


class BookReservation:
    """Manages book reservation operations for library patrons.

    This class handles the creation, validation, and management of
    book reservations. It ensures that reservations follow library
    policies including maximum hold duration and concurrent reservation
    limits.

    Attributes:
        patron_id: Unique identifier for the library patron.
        book_isbn: ISBN of the reserved book.
        reservation_date: UTC timestamp when the reservation was created.
        expiration_date: UTC timestamp when the reservation expires.
        status: Current status of the reservation.
    """

    MAX_CONCURRENT_RESERVATIONS = 5
    DEFAULT_HOLD_DAYS = 7
    VALID_STATUSES = ("pending", "active", "fulfilled", "cancelled", "expired")

    def __init__(
        self,
        patron_id: str,
        book_isbn: str,
        hold_days: int = DEFAULT_HOLD_DAYS,
    ) -> None:
        """Initialize a new book reservation.

        Args:
            patron_id: Unique identifier for the library patron.
            book_isbn: ISBN of the book to reserve.
            hold_days: Number of days to hold the reservation.

        Raises:
            ValueError: If patron_id or book_isbn is empty, or if
                hold_days is not positive.
        """
        if not patron_id or not patron_id.strip():
            raise ValueError("patron_id must be a non-empty string")
        if not book_isbn or not book_isbn.strip():
            raise ValueError("book_isbn must be a non-empty string")
        if hold_days <= 0:
            raise ValueError("hold_days must be a positive integer")

        self.patron_id = patron_id.strip()
        self.book_isbn = book_isbn.strip()
        self.reservation_date = datetime.now(timezone.utc)
        self.expiration_date = self.reservation_date + __import__(
            "datetime"
        ).timedelta(days=hold_days)
        self.status: str = "pending"

    def is_expired(self) -> bool:
        """Check if the reservation has passed its expiration date.

        Returns:
            True if the current time is past the expiration date.
        """
        return datetime.now(timezone.utc) > self.expiration_date

    def cancel(self) -> None:
        """Cancel the reservation.

        Raises:
            RuntimeError: If the reservation is already fulfilled.
        """
        if self.status == "fulfilled":
            raise RuntimeError("Cannot cancel a fulfilled reservation")
        self.status = "cancelled"

    def fulfill(self) -> None:
        """Mark the reservation as fulfilled (book picked up).

        Raises:
            RuntimeError: If the reservation is not in 'active' status.
        """
        if self.status != "active":
            raise RuntimeError(
                f"Can only fulfill active reservations, current status: {self.status}"
            )
        self.status = "fulfilled"

    def to_dict(self) -> dict[str, Any]:
        """Serialize the reservation to a dictionary.

        Returns:
            Dictionary representation of the reservation.
        """
        return {
            "patron_id": self.patron_id,
            "book_isbn": self.book_isbn,
            "reservation_date": self.reservation_date.isoformat(),
            "expiration_date": self.expiration_date.isoformat(),
            "status": self.status,
        }


# ============================================================
# SAMPLE D
# ============================================================

import hashlib
import os


def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return salt + key


def verify_password(stored, provided):
    salt = stored[:32]
    stored_key = stored[32:]
    new_key = hashlib.pbkdf2_hmac(
        "sha256", provided.encode("utf-8"), salt, 100000
    )
    return stored_key == new_key


# ============================================================
# SAMPLE E
# ============================================================

def process_library_fines(patron_records: list[dict]) -> dict[str, Any]:
    """Process and summarize outstanding library fines for all patrons.

    Calculates total fines, identifies patrons with overdue balances,
    and generates a summary report suitable for the finance department.

    Args:
        patron_records: List of patron dictionaries, each containing:
            - patron_id (str): Unique patron identifier
            - name (str): Patron's full name
            - fines (list[dict]): List of fine records with 'amount',
              'date', 'reason', and 'paid' fields

    Returns:
        Dictionary containing:
            - total_outstanding (float): Sum of all unpaid fines
            - total_collected (float): Sum of all paid fines
            - patrons_with_fines (int): Count of patrons with unpaid fines
            - highest_fine (dict): Patron with the largest unpaid balance
            - summary (list[dict]): Per-patron breakdown

    Raises:
        TypeError: If patron_records is not a list.
        ValueError: If any fine amount is negative.
    """
    if not isinstance(patron_records, list):
        raise TypeError("patron_records must be a list")

    total_outstanding = 0.0
    total_collected = 0.0
    patrons_with_fines = 0
    highest_fine_amount = 0.0
    highest_fine_patron = None
    summary = []

    for patron in patron_records:
        patron_id = patron.get("patron_id", "unknown")
        name = patron.get("name", "Unknown Patron")
        fines = patron.get("fines", [])

        patron_outstanding = 0.0
        patron_collected = 0.0

        for fine in fines:
            amount = fine.get("amount", 0)
            if amount < 0:
                raise ValueError(
                    f"Fine amount cannot be negative for patron {patron_id}"
                )

            if fine.get("paid", False):
                patron_collected += amount
            else:
                patron_outstanding += amount

        if patron_outstanding > 0:
            patrons_with_fines += 1

        if patron_outstanding > highest_fine_amount:
            highest_fine_amount = patron_outstanding
            highest_fine_patron = {
                "patron_id": patron_id,
                "name": name,
                "outstanding": patron_outstanding,
            }

        total_outstanding += patron_outstanding
        total_collected += patron_collected

        summary.append({
            "patron_id": patron_id,
            "name": name,
            "outstanding": round(patron_outstanding, 2),
            "collected": round(patron_collected, 2),
        })

    return {
        "total_outstanding": round(total_outstanding, 2),
        "total_collected": round(total_collected, 2),
        "patrons_with_fines": patrons_with_fines,
        "highest_fine": highest_fine_patron,
        "summary": summary,
    }
