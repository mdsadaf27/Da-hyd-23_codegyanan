#!/usr/bin/env python3
"""
Library Management System
---------------------------------------
A pure-Python, terminal-based library management system.
    python3 library_system.py

Data is saved to library_data.json in the same folder, so your
users, books, and transactions persist between runs.

Demo accounts:
    Member   -> username: devika        password: demo1234
    Admin    -> username: librarian     password: admin123
"""

import json
import os
import random
import sys
from datetime import date, timedelta

# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library_data.json")

MEMBERSHIPS = {
    "basic":   {"name": "Basic",   "max_books": 2, "loan_days": 14, "renewals": 1, "fine_discount": 0.0},
    "premium": {"name": "Premium", "max_books": 5, "loan_days": 21, "renewals": 2, "fine_discount": 0.25},
    "gold":    {"name": "Gold",    "max_books": 8, "loan_days": 30, "renewals": 3, "fine_discount": 0.5},
}
FINE_PER_DAY = 5
CATEGORIES = ["Fiction", "Science", "History", "Poetry", "Biography", "Technology"]

ADMIN_USERNAME = "librarian"
ADMIN_PASSWORD = "admin123"

TODAY = date.today()

# ------------------------------------------------------------------
# Data persistence
# ------------------------------------------------------------------

def default_data():
    return {
        "users": {
            "U100": {
                "id": "U100", "name": "Devika Rao", "email": "devika.rao@mail.com",
                "username": "devika", "password": "demo1234",
                "membership": "premium", "status": "approved", "joined": str(TODAY),
            }
        },
        "pending": {
            "U201": {
                "id": "U201", "name": "Sam Ferreira", "email": "sam.f@mail.com",
                "username": "samf", "password": "pass1234",
                "membership": "basic", "requested_at": str(TODAY),
            }
        },
        "books": {
            "B001": {"id": "B001", "title": "The Salt Path Home", "author": "Nadia Okoro",
                      "category": "Fiction", "total": 3, "available": 2},
            "B002": {"id": "B002", "title": "Quiet Mechanics", "author": "Felix Aran",
                      "category": "Science", "total": 2, "available": 1},
            "B003": {"id": "B003", "title": "A Ledger of Rivers", "author": "Marta Solheim",
                      "category": "History", "total": 4, "available": 4},
            "B004": {"id": "B004", "title": "Loose Threads", "author": "Priya Chandran",
                      "category": "Poetry", "total": 2, "available": 1},
            "B005": {"id": "B005", "title": "Building Small Machines", "author": "Wren Castillo",
                      "category": "Technology", "total": 2, "available": 2},
        },
        "issues": {
            "I001": {"id": "I001", "user_id": "U100", "book_id": "B002",
                       "issue_date": str(TODAY - timedelta(days=10)),
                       "due_date": str(TODAY + timedelta(days=11)), "status": "issued"},
        },
        "returns": {},
        "next_id": {"user": 202, "book": 6, "issue": 2, "return": 1},
    }


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    data = default_data()
    save_data(data)
    return data


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def next_id(data, kind):
    n = data["next_id"][kind]
    data["next_id"][kind] += 1
    prefix = {"user": "U", "book": "B", "issue": "I", "return": "R"}[kind]
    return f"{prefix}{n}"


# ------------------------------------------------------------------
# Small display helpers
# ------------------------------------------------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header(title, subtitle=None):
    clear()
    print("=" * 62)
    print(f"  ATHENAEUM — {title}")
    if subtitle:
        print(f"  {subtitle}")
    print("=" * 62)
    print()


def pause():
    input("\nPress Enter to continue... ")


def divider():
    print("-" * 62)


def table(rows, headers):
    """rows: list of tuples/lists; headers: list of column names."""
    if not rows:
        print("  (nothing to show)")
        return
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    fmt = "  " + "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers))
    print("  " + "-" * (sum(widths) + 2 * (len(widths) - 1)))
    for row in rows:
        print(fmt.format(*[str(c) for c in row]))


def ask(prompt, required=True, validator=None, error_msg="That doesn't look right, try again."):
    while True:
        val = input(prompt).strip()
        if not val and required:
            print(f"  This field is required.")
            continue
        if validator and val and not validator(val):
            print(f"  {error_msg}")
            continue
        return val


def ask_choice(prompt, options):
    """options: list of (key, label). Returns chosen key."""
    for i, (key, label) in enumerate(options, start=1):
        print(f"  {i}. {label}")
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1][0]
        print("  Please enter a valid option number.")


def is_valid_email(s):
    return "@" in s and "." in s.split("@")[-1]


# ------------------------------------------------------------------
# Registration & OTP verification
# ------------------------------------------------------------------

def generate_otp():
    return str(random.randint(1000, 9999))


def register_flow(data):
    header("Register", "Step 1 of 3 — your details")
    name = ask("Full name: ")
    email = ask("Email address: ", validator=is_valid_email, error_msg="Enter a valid email like name@example.com")
    mobile = ask("Mobile number: ")
    username = ask("Choose a username: ")

    if any(u["username"] == username for u in data["users"].values()) or \
       any(u["username"] == username for u in data["pending"].values()):
        print("\n  That username is already taken. Please start again.")
        pause()
        return

    password = ask("Choose a password (min 6 chars): ", validator=lambda s: len(s) >= 6,
                    error_msg="Password must be at least 6 characters.")

    print()
    print("  Preferred membership:")
    membership = ask_choice(
        "  Choose 1-3: ",
        [(k, f"{v['name']} — {v['max_books']} books, {v['loan_days']}-day loans") for k, v in MEMBERSHIPS.items()]
    )

    # ---- OTP step ----
    header("Register", "Step 2 of 3 — verify your email")
    otp = generate_otp()
    print(f"  A verification code has been sent to {email}.")
    print(f"  [DEMO MODE — your code is: {otp}]\n")

    attempts = 0
    while attempts < 3:
        entered = ask("  Enter the 4-digit code: ")
        if entered == otp:
            print("\n  ✓ Email verified.")
            break
        attempts += 1
        print(f"  Incorrect code. {3 - attempts} attempt(s) left.")
    else:
        print("\n  Too many incorrect attempts. Please register again.")
        pause()
        return

    # ---- Send to admin queue ----
    header("Register", "Step 3 of 3 — awaiting librarian approval")
    uid = next_id(data, "user")
    data["pending"][uid] = {
        "id": uid, "name": name, "email": email, "mobile": mobile,
        "username": username, "password": password, "membership": membership,
        "requested_at": str(TODAY),
    }
    save_data(data)
    print("  Your registration has been submitted.")
    print("  A librarian must approve your account before you can log in.")
    print(f"  Your request ID is {uid}.")
    pause()


# ------------------------------------------------------------------
# Login
# ------------------------------------------------------------------

def member_login(data):
    header("Member Login")
    username = ask("Username: ")
    password = ask("Password: ")

    for u in data["users"].values():
        if u["username"] == username and u["password"] == password and u["status"] == "approved":
            print(f"\n  Welcome back, {u['name'].split()[0]}.")
            pause()
            return u["id"]

    # helpful message if they're still pending
    for p in data["pending"].values():
        if p["username"] == username:
            print("\n  Your registration is still awaiting librarian approval.")
            pause()
            return None

    print("\n  We couldn't find an approved account with those credentials.")
    pause()
    return None


def admin_login():
    header("Administrator Login")
    username = ask("Staff ID: ")
    password = ask("Password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\n  Signed in to the admin desk.")
        pause()
        return True
    print("\n  Incorrect staff credentials.")
    pause()
    return False


# ------------------------------------------------------------------
# Member area
# ------------------------------------------------------------------

def member_menu(data, user_id):
    while True:
        u = data["users"][user_id]
        m = MEMBERSHIPS[u["membership"]]
        header("My Desk", f"{u['name']}  ·  {m['name']} member")

        my_issues = [i for i in data["issues"].values() if i["user_id"] == user_id and i["status"] == "issued"]
        overdue = [i for i in my_issues if date.fromisoformat(i["due_date"]) < TODAY]
        fine = sum(current_fine(i, m) for i in overdue)

        print(f"  Books out: {len(my_issues)}/{m['max_books']}   "
              f"Overdue: {len(overdue)}   Current fine: Rs.{fine}")
        divider()
        print("  1. Search books")
        print("  2. My borrowed books")
        print("  3. Borrow a book")
        print("  4. Return a book")
        print("  5. My membership")
        print("  6. Log out")
        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            search_books(data)
        elif choice == "2":
            my_books_view(data, user_id)
        elif choice == "3":
            borrow_flow(data, user_id)
        elif choice == "4":
            return_flow(data, user_id)
        elif choice == "5":
            profile_view(data, user_id)
        elif choice == "6":
            return
        else:
            print("  Not a valid option.")
            pause()


def current_fine(issue, membership):
    due = date.fromisoformat(issue["due_date"])
    overdue_days = max(0, (TODAY - due).days)
    return round(overdue_days * FINE_PER_DAY * (1 - membership["fine_discount"]))


def search_books(data):
    header("Search Books")
    q = input("  Search by title/author (Enter to browse all): ").strip().lower()
    print()
    print("  Categories: " + ", ".join(CATEGORIES))
    cat = input("  Filter by category (Enter for all): ").strip()

    results = []
    for b in data["books"].values():
        if q and q not in b["title"].lower() and q not in b["author"].lower():
            continue
        if cat and cat.lower() != b["category"].lower():
            continue
        results.append(b)

    print()
    rows = [(b["id"], b["title"], b["author"], b["category"], f"{b['available']}/{b['total']}") for b in results]
    table(rows, ["ID", "Title", "Author", "Category", "Available"])
    pause()


def my_books_view(data, user_id):
    header("My Borrowed Books")
    m = MEMBERSHIPS[data["users"][user_id]["membership"]]
    my_issues = [i for i in data["issues"].values() if i["user_id"] == user_id and i["status"] == "issued"]
    rows = []
    for i in my_issues:
        b = data["books"][i["book_id"]]
        due = date.fromisoformat(i["due_date"])
        status = f"{(TODAY - due).days}d overdue" if due < TODAY else "on time"
        rows.append((i["id"], b["title"], i["issue_date"], i["due_date"], status))
    table(rows, ["Issue ID", "Title", "Issued", "Due", "Status"])
    pause()


def borrow_flow(data, user_id):
    header("Borrow a Book")
    u = data["users"][user_id]
    m = MEMBERSHIPS[u["membership"]]
    my_issues = [i for i in data["issues"].values() if i["user_id"] == user_id and i["status"] == "issued"]

    if len(my_issues) >= m["max_books"]:
        print(f"  You're at your {m['name']} plan's limit of {m['max_books']} books.")
        print("  Return one before borrowing another.")
        pause()
        return

    book_id = ask("  Enter the Book ID to borrow (see 'Search books' for IDs): ").strip().upper()
    book = data["books"].get(book_id)
    if not book:
        print("  No book with that ID.")
        pause()
        return
    if book["available"] <= 0:
        print(f"  '{book['title']}' has no available copies right now.")
        pause()
        return
    if any(i["book_id"] == book_id for i in my_issues):
        print("  You already have this book issued.")
        pause()
        return

    book["available"] -= 1
    issue_id = next_id(data, "issue")
    due_date = TODAY + timedelta(days=m["loan_days"])
    data["issues"][issue_id] = {
        "id": issue_id, "user_id": user_id, "book_id": book_id,
        "issue_date": str(TODAY), "due_date": str(due_date), "status": "issued",
    }
    save_data(data)
    print(f"\n  '{book['title']}' is yours until {due_date}.")
    pause()


def return_flow(data, user_id):
    header("Return a Book")
    m = MEMBERSHIPS[data["users"][user_id]["membership"]]
    my_issues = [i for i in data["issues"].values() if i["user_id"] == user_id and i["status"] == "issued"]
    if not my_issues:
        print("  You don't have any books out right now.")
        pause()
        return

    rows = [(i["id"], data["books"][i["book_id"]]["title"], i["due_date"]) for i in my_issues]
    table(rows, ["Issue ID", "Title", "Due"])
    issue_id = ask("\n  Enter the Issue ID to return: ").strip().upper()
    issue = next((i for i in my_issues if i["id"] == issue_id), None)
    if not issue:
        print("  That issue ID isn't one of your current loans.")
        pause()
        return

    fine = current_fine(issue, m)
    book = data["books"][issue["book_id"]]
    issue["status"] = "returned"
    book["available"] += 1
    overdue_days = max(0, (TODAY - date.fromisoformat(issue["due_date"])).days)
    rid = next_id(data, "return")
    data["returns"][rid] = {
        "id": rid, "issue_id": issue_id, "return_date": str(TODAY),
        "overdue_days": overdue_days, "fine": fine,
    }
    save_data(data)
    if fine > 0:
        print(f"\n  Returned. Fine: Rs.{fine} for {overdue_days} overdue day(s).")
    else:
        print("\n  Returned on time — nice work.")
    pause()


def profile_view(data, user_id):
    header("My Membership")
    u = data["users"][user_id]
    m = MEMBERSHIPS[u["membership"]]
    print(f"  Name:        {u['name']}")
    print(f"  Email:       {u['email']}")
    print(f"  Membership:  {m['name']}")
    divider()
    print(f"  Max books:      {m['max_books']}")
    print(f"  Loan period:    {m['loan_days']} days")
    print(f"  Renewals:       {m['renewals']}")
    print(f"  Fine discount:  {int(m['fine_discount']*100)}%")
    pause()


# ------------------------------------------------------------------
# Admin area
# ------------------------------------------------------------------

def admin_menu(data):
    while True:
        header("Admin Desk")
        pending_n = len(data["pending"])
        issued_n = sum(1 for i in data["issues"].values() if i["status"] == "issued")
        print(f"  Pending registrations: {pending_n}   Books currently on loan: {issued_n}")
        divider()
        print("  1. Review pending users")
        print("  2. Manage book catalog")
        print("  3. View issues & returns")
        print("  4. Reports")
        print("  5. Log out")
        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            review_pending(data)
        elif choice == "2":
            manage_books(data)
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            reports(data)
        elif choice == "5":
            return
        else:
            print("  Not a valid option.")
            pause()


def review_pending(data):
    while True:
        header("Pending Registrations")
        pending = list(data["pending"].values())
        if not pending:
            print("  Queue is clear — nothing waiting.")
            pause()
            return

        rows = [(p["id"], p["name"], p["email"], p["membership"], p["requested_at"]) for p in pending]
        table(rows, ["ID", "Name", "Email", "Requested Plan", "Requested"])

        print("\n  Enter a request ID to review, or press Enter to go back.")
        pid = input("  Request ID: ").strip().upper()
        if not pid:
            return
        p = data["pending"].get(pid)
        if not p:
            print("  No pending request with that ID.")
            pause()
            continue

        print(f"\n  {p['name']} ({p['email']}) requested {MEMBERSHIPS[p['membership']]['name']} membership.")
        decision = input("  Approve or reject? [a/r]: ").strip().lower()
        if decision == "a":
            uid = p["id"]
            data["users"][uid] = {
                "id": uid, "name": p["name"], "email": p["email"], "username": p["username"],
                "password": p["password"], "membership": p["membership"], "status": "approved",
                "joined": str(TODAY),
            }
            del data["pending"][pid]
            save_data(data)
            print(f"\n  *** {p['name']} — APPROVED ***")
        elif decision == "r":
            del data["pending"][pid]
            save_data(data)
            print(f"\n  *** {p['name']} — REJECTED ***")
        else:
            print("  No changes made.")
        pause()


def manage_books(data):
    while True:
        header("Book Catalog")
        rows = [(b["id"], b["title"], b["author"], b["category"], f"{b['available']}/{b['total']}")
                for b in data["books"].values()]
        table(rows, ["ID", "Title", "Author", "Category", "Available"])
        divider()
        print("  1. Add a book")
        print("  2. Remove a book")
        print("  3. Back")
        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            header("Add a Book")
            title = ask("  Title: ")
            author = ask("  Author: ")
            print("  Categories: " + ", ".join(CATEGORIES))
            category = ask("  Category: ")
            copies = ask("  Total copies: ", validator=str.isdigit, error_msg="Enter a whole number.")
            bid = next_id(data, "book")
            data["books"][bid] = {
                "id": bid, "title": title, "author": author, "category": category,
                "total": int(copies), "available": int(copies),
            }
            save_data(data)
            print(f"\n  Added '{title}' ({bid}) to the catalog.")
            pause()
        elif choice == "2":
            bid = ask("  Enter Book ID to remove: ").strip().upper()
            if bid in data["books"]:
                title = data["books"][bid]["title"]
                del data["books"][bid]
                save_data(data)
                print(f"\n  Removed '{title}'.")
            else:
                print("  No book with that ID.")
            pause()
        elif choice == "3":
            return
        else:
            print("  Not a valid option.")
            pause()


def view_transactions(data):
    header("Issues & Returns")
    print("  CURRENTLY ISSUED")
    rows = []
    for i in data["issues"].values():
        if i["status"] != "issued":
            continue
        b = data["books"].get(i["book_id"], {"title": "?"})
        u = data["users"].get(i["user_id"], {"name": i["user_id"]})
        due = date.fromisoformat(i["due_date"])
        status = f"{(TODAY - due).days}d overdue" if due < TODAY else "on time"
        rows.append((i["id"], b["title"], u["name"], i["due_date"], status))
    table(rows, ["Issue ID", "Book", "Member", "Due", "Status"])

    print("\n  RETURN LOG")
    rrows = [(r["id"], r["issue_id"], r["return_date"], r["overdue_days"], f"Rs.{r['fine']}")
             for r in data["returns"].values()]
    table(rrows, ["Return ID", "Issue ID", "Returned", "Overdue Days", "Fine"])
    pause()


def reports(data):
    header("Reports")
    tier_counts = {"basic": 0, "premium": 0, "gold": 0}
    for u in data["users"].values():
        tier_counts[u["membership"]] += 1
    total_fines = sum(r["fine"] for r in data["returns"].values())
    total_copies = sum(b["total"] for b in data["books"].values())

    print(f"  Titles in catalog:     {len(data['books'])}")
    print(f"  Total copies:          {total_copies}")
    print(f"  Approved members:      {len(data['users'])}")
    print(f"  Books returned:        {len(data['returns'])}")
    print(f"  Fines collected:       Rs.{total_fines}")
    divider()
    print("  Members by tier:")
    for k, v in MEMBERSHIPS.items():
        bar = "#" * tier_counts[k]
        print(f"    {v['name']:<8} {tier_counts[k]:>3}  {bar}")
    pause()


# ------------------------------------------------------------------
# Main menu
# ------------------------------------------------------------------

def main():
    data = load_data()
    while True:
        header("Welcome", "A quieter way to run the library")
        print("  1. Register as a member")
        print("  2. Member login")
        print("  3. Administrator login")
        print("  4. Exit")
        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            register_flow(data)
        elif choice == "2":
            uid = member_login(data)
            if uid:
                member_menu(data, uid)
        elif choice == "3":
            if admin_login():
                admin_menu(data)
        elif choice == "4":
            print("\n  Goodbye.")
            sys.exit(0)
        else:
            print("  Not a valid option.")
            pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Goodbye.")
        sys.exit(0)