
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pickle
import os
from datetime import datetime
import random
import string

# File paths for data persistence
USERS_FILE = "users.pkl"
EVENTS_FILE = "events.pkl"
BOOKINGS_FILE = "bookings.pkl"
DISCOUNTS_FILE = "discounts.pkl"

# Utilities for saving and loading data with exception handling
def save_data(data, filename):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save data: {e}")

def load_data(filename):
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        messagebox.showerror("Load Error", f"Failed to load data: {e}")
        return {}

# Base Ticket class
class Ticket:
    def __init__(self, ticketID, ticket_type, price, seatNumber):
        self.ticketID = ticketID
        self.type = ticket_type
        self.price = price
        self.seatNumber = seatNumber
        self.isAvailable = True

    def getTicketID(self):
        return self.ticketID

    def setTicketID(self, id):
        self.ticketID = id

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getSeatNumber(self):
        return self.seatNumber

    def setSeatNumber(self, seat):
        self.seatNumber = seat

    def getisAvailable(self):
        return self.isAvailable

    def setAvailable(self, available):
        self.isAvailable = available

    # Basic discount calculation, overridden by subclasses for specifics
    def calculateDiscount(self, discounts):
        discount_rate = discounts.get(self.type, 0)
        return self.price * (1 - discount_rate)

#Single pass class
class SinglePassTicket(Ticket):
    def __init__(self, ticketID, price, seatNumber, validDate):
        super().__init__(ticketID, "Single Pass", price, seatNumber)
        self.validDate = validDate
#Validate date
    def getValidDate(self):
        return self.validDate

    def setValidDate(self, validDate):
        self.validDate = validDate

class GroupTicket(Ticket): #Group ticket class
    def __init__(self, ticketID, price, seatNumber, groupSize):
        super().__init__(ticketID, "Group", price, seatNumber)
        self.groupSize = groupSize

    def getGroupSize(self):
        return self.groupSize

    def setGroupSize(self, groupSize):
        self.groupSize = groupSize

class SeasonTicket(Ticket): #Season ticket class
    def __init__(self, ticketID, price, seatNumber, seasonDuration):
        super().__init__(ticketID, "Season", price, seatNumber)
        self.seasonDuration = seasonDuration

    def getSeasonDuration(self):
        return self.seasonDuration

    def setSeasonDuration(self, seasonDuration):
        self.seasonDuration = seasonDuration

class WeekendTicket(Ticket): #Weekend ticket
    def __init__(self, ticketID, price, seatNumber, validWeekend):
        super().__init__(ticketID, "Weekend", price, seatNumber)
        self.validWeekend = validWeekend

    def getValidWeekend(self):
        return self.validWeekend

    def setValidWeekend(self, validWeekend):
        self.validWeekend = validWeekend

class User: #User class
    def __init__(self, userID, username, email, password, contactNumber):
        self.userID = userID
        self.username = username
        self.email = email
        self.password = password
        self.contactNumber = contactNumber

    def getUserID(self):
        return self.userID

    def setUserID(self, id):
        self.userID = id

    def getUsername(self):
        return self.username

    def setUsername(self, name):
        self.username = name

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getContactNumber(self):
        return self.contactNumber

    def setContactNumber(self, number):
        self.contactNumber = number

    def login(self, email, password):
        return self.email == email and self.password == password

    def logout(self):
        pass

class Customer(User): #Customer class
    def __init__(self, userID, username, email, password, contactNumber):
        super().__init__(userID, username, email, password, contactNumber)
        self.purchaseHistory = []

    def makeBooking(self, booking):
        self.purchaseHistory.append(booking)

    def viewPurchaseHistory(self):
        return self.purchaseHistory

class Admin(User): #Admin class
    def __init__(self, userID, username, email, password, contactNumber, adminLevel="Super", department="Management"):
        super().__init__(userID, username, email, password, contactNumber)
        self.adminLevel = adminLevel
        self.department = department

    def getAdminLevel(self):
        return self.adminLevel

    def setAdminLevel(self, level):
        self.adminLevel = level

    def getDepartment(self):
        return self.department

    def setDepartment(self, dept):
        self.department = dept

class Event: #Event class
    def __init__(self, name, location, date, totalCapacity, eventType):
        self.name = name
        self.location = location
        self.date = date
        self.totalCapacity = totalCapacity
        self.eventType = eventType
        self.ticketList = []
        self.userList = []

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTotalCapacity(self):
        return self.totalCapacity

    def setTotalCapacity(self, capacity):
        self.totalCapacity = capacity

    def getEventType(self):
        return self.eventType

    def setEventType(self, type):
        self.eventType = type

    def getTicketList(self):
        return self.ticketList

    def setTicketList(self, tickets):
        self.ticketList = tickets

    def getUserList(self):
        return self.userList

    def setUserList(self, users):
        self.userList = users

    def addTicket(self, ticket):
        self.ticketList.append(ticket)

    def removeTicket(self, ticketID):
        self.ticketList = [t for t in self.ticketList if t.ticketID != ticketID]

    def addUser(self, user):
        self.userList.append(user)

    def removeUser(self, userID):
        self.userList = [u for u in self.userList if u.userID != userID]

    def getAvailableTickets(self):
        return [t for t in self.ticketList if t.isAvailable]

class Payment: #payement class
    def __init__(self, paymentID, amount, paymentDate, description=""):
        self.paymentID = paymentID
        self.amount = amount
        self.paymentDate = paymentDate
        self.status = "Pending"
        self.description = description

    def getPaymentID(self):
        return self.paymentID

    def setPaymentID(self, id):
        self.paymentID = id

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getPaymentDate(self):
        return self.paymentDate

    def setPaymentDate(self, date):
        self.paymentDate = date

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getDescription(self):
        return self.description

    def setDescription(self, desc):
        self.description = desc

    def processPayment(self):
        # Simulate successful payment
        self.status = "Completed"
        return True

    def refundPayment(self):
        self.status = "Refunded"
        return True

class Cash(Payment): # payment - cash class
    def __init__(self, paymentID, amount, paymentDate, cashReceived):
        super().__init__(paymentID, amount, paymentDate)
        self.cashReceived = cashReceived
        self.changeGiven = 0.0

    def getCashReceived(self):
        return self.cashReceived

    def setCashReceived(self, cash):
        self.cashReceived = cash

    def getChangeGiven(self):
        return self.changeGiven

    def setChangeGiven(self, change):
        self.changeGiven = change

    def calculateChange(self):
        change = self.cashReceived - self.amount
        self.changeGiven = change if change > 0 else 0
        return self.changeGiven

    def processPayment(self): #Processing payment
        if self.cashReceived >= self.amount:
            self.calculateChange()
            self.status = "Completed"
            return True
        else:
            self.status = "Failed"
            return False

class CreditDebitCard(Payment): #Paying by card class
    def __init__(self, paymentID, amount, paymentDate, cardNumber, cardholderName, expiryDate, cvv):
        super().__init__(paymentID, amount, paymentDate)
        self.cardNumber = cardNumber
        self.cardholderName = cardholderName
        self.expiryDate = expiryDate
        self.cvv = cvv

    def getCardNumber(self):
        return self.cardNumber

    def setCardNumber(self, number):
        self.cardNumber = number

    def getCardholderName(self):
        return self.cardholderName

    def setCardholderName(self, name):
        self.cardholderName = name

    def getExpiryDate(self):
        return self.expiryDate

    def setExpiryDate(self, date):
        self.expiryDate = date

    def getCVV(self):
        return self.cvv

    def setCVV(self, cvv):
        self.cvv = cvv

    def validateCard(self):
        # A very basic validation: length checks and numeric checks
        try:
            if len(self.cardNumber) != 16 or not self.cardNumber.isdigit():
                return False
            if len(self.cvv) != 3 or not self.cvv.isdigit():
                return False
            # Expiry date format MM/YY
            month, year = self.expiryDate.split('/')
            if int(month) < 1 or int(month) > 12:
                return False
            # Validate expiry date is not in past (somewhat simplified)
            current_year = datetime.now().year % 100
            current_month = datetime.now().month
            if int(year) < current_year or (int(year) == current_year and int(month) < current_month):
                return False
            return True
        except Exception:
            return False

    def processPayment(self):
        if self.validateCard():
            self.status = "Completed"
            return True
        else:
            self.status = "Failed"
            return False

class Booking: #Booking class
    def __init__(self, bookingID, customer, ticket, bookingDate):
        self.bookingID = bookingID
        self.customer = customer
        self.ticket = ticket
        self.bookingDate = bookingDate
        self.status = "Active"
        self.payment = None

    def getBookingID(self):
        return self.bookingID

    def setBookingID(self, id):
        self.bookingID = id

    def getCustomer(self):
        return self.customer

    def setCustomer(self, customer):
        self.customer = customer

    def getTicket(self):
        return self.ticket

    def setTicket(self, ticket):
        self.ticket = ticket

    def getBookingDate(self):
        return self.bookingDate

    def setBookingDate(self, date):
        self.bookingDate = date

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getPayment(self):
        return self.payment

    def setPayment(self, payment):
        self.payment = payment

    def confirmBooking(self):
        if self.payment and self.payment.status == "Completed":
            self.status = "Confirmed"
            self.ticket.setAvailable(False)
            return True
        return False

    def cancelBooking(self):
        if self.status == "Confirmed":
            self.status = "Cancelled"
            self.ticket.setAvailable(True)
            if self.payment:
                self.payment.refundPayment()
            return True
        return False

class PurchaseHistory: #Purchase history
    def __init__(self, customerID):
        self.customerID = customerID
        self.bookings = []
        self.totalSpent = 0.0
        self.lastPurchaseDate = None

    def getCustomerID(self):
        return self.customerID

    def setCustomerID(self, id):
        self.customerID = id

    def getBookings(self):
        return self.bookings

    def setBookings(self, bookings):
        self.bookings = bookings

    def addBooking(self, booking):
        self.bookings.append(booking)
        self.calculateTotalSpent()
        self.updateLastPurchaseDate()

    def removeBooking(self, bookingID):
        for b in self.bookings:
            if b.bookingID == bookingID:
                self.bookings.remove(b)
                self.calculateTotalSpent()
                self.updateLastPurchaseDate()
                return True
        return False

    def getTotalSpent(self):
        return self.totalSpent

    def setTotalSpent(self, amount):
        self.totalSpent = amount

    def calculateTotalSpent(self):
        self.totalSpent = sum(b.ticket.getPrice() for b in self.bookings if b.status == "Confirmed")

    def getLastPurchaseDate(self):
        return self.lastPurchaseDate

    def setLastPurchaseDate(self, date):
        self.lastPurchaseDate = date

    def updateLastPurchaseDate(self):
        dates = [b.bookingDate for b in self.bookings if b.status == "Confirmed"]
        if dates:
            self.lastPurchaseDate = max(dates)
        else:
            self.lastPurchaseDate = None

    def viewHistory(self):
        return self.bookings

# Main Application GUI with Tkinter
class GrandPrixExperienceApp:
    def __init__(self, root): #tittle for the GUI
        self.root = root
        self.root.title("Grand Prix Experience!")
        self.root.geometry("700x500") #Sizing the tittle
        self.root.resizable(False, False)

        # Load data
        self.users = load_data(USERS_FILE)  # userID: User object
        self.events = load_data(EVENTS_FILE)  # eventName: Event object
        self.bookings = load_data(BOOKINGS_FILE)  # bookingID: Booking object
        self.discounts = load_data(DISCOUNTS_FILE)  # ticketType:str -> discount float (e.g. 0.1 for 10%)

        # If no admin user exists, create default admin with fixed credentials
        self.default_admin = Admin("admin001", "admin", "admin@example.com", "1234", "0000000000")
        if "admin001" not in self.users:
            self.users["admin001"] = self.default_admin

        # Current logged in user and event
        self.current_user = None
        self.current_event = None

        # Initialize the GUI to main choice screen
        self.main_choice_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_choice_screen(self):
        self.clear_screen()
        title_label = tk.Label(self.root, text="Grand Prix Experience!", font=("Helvetica", 28, "bold"))
        title_label.pack(pady=30)

        admin_button = tk.Button(self.root, text="Admin", font=("Helvetica", 16), width=20, command=self.admin_login_screen)
        admin_button.pack(pady=20)

        customer_button = tk.Button(self.root, text="Customer", font=("Helvetica", 16), width=20, command=self.customer_login_screen)
        customer_button.pack(pady=20)

    ##############
    # Admin methods
    ##############
    def admin_login_screen(self):
        self.clear_screen()

        label = tk.Label(self.root, text="Admin Login", font=("Helvetica", 22, "bold"))
        label.pack(pady=20)

        email_label = tk.Label(self.root, text="Username:", font=("Helvetica", 14))
        email_label.pack()
        self.admin_username_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.admin_username_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:", font=("Helvetica", 14))
        password_label.pack()
        self.admin_password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*")
        self.admin_password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", font=("Helvetica", 14), command=self.admin_login)
        login_button.pack(pady=20)

        back_button = tk.Button(self.root, text="Back", font=("Helvetica", 12), command=self.main_choice_screen)
        back_button.pack()

    def admin_login(self):
        username = self.admin_username_entry.get().strip()
        password = self.admin_password_entry.get().strip()

        # Admin login in users dictionary, validate
        admin_user = None
        for user in self.users.values():
            if isinstance(user, Admin) and user.username == username and user.password == password:
                admin_user = user
                break

        if admin_user:
            self.current_user = admin_user
            messagebox.showinfo("Login Success", f"Welcome, Admin {admin_user.username}!")
            self.admin_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid admin username or password.")

    def admin_dashboard(self):
        self.clear_screen()
        header = tk.Label(self.root, text="Admin Dashboard", font=("Helvetica", 22, "bold"))
        header.pack(pady=15)

        sales_report_button = tk.Button(self.root, text="View Ticket Sales Report", font=("Helvetica", 14), width=30, command=self.show_sales_report)
        sales_report_button.pack(pady=8)

        manage_discounts_button = tk.Button(self.root, text="Manage Discounts", font=("Helvetica", 14), width=30, command=self.manage_discounts_screen)
        manage_discounts_button.pack(pady=8)

        manage_events_button = tk.Button(self.root, text="Manage Events", font=("Helvetica", 14), width=30, command=self.manage_events_screen)
        manage_events_button.pack(pady=8)

        manage_users_button = tk.Button(self.root, text="Manage Users", font=("Helvetica", 14), width=30, command=self.manage_users_screen)
        manage_users_button.pack(pady=8)

        logout_button = tk.Button(self.root, text="Logout", font=("Helvetica", 12), command=self.logout)
        logout_button.pack(pady=15)

    def show_sales_report(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Ticket Sales Report", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        # Aggregate ticket sales per event date
        # We'll create a dictionary of date -> count sold tickets
        sales_count = {}
        for b in self.bookings.values():
            if b.status == "Confirmed":
                event_name = None
                # Find event for this ticket seat number
                for event in self.events.values():
                    if b.ticket in event.ticketList:
                        event_name = event.name
                        break
                if event_name:
                    sales_count[event_name] = sales_count.get(event_name, 0) + 1

        if not sales_count:
            sales_count_str = "No sales data available."
        else:
            lines = []
            for event_name, count in sales_count.items():
                lines.append(f"Event: {event_name} - Tickets Sold: {count}")
            sales_count_str = "\n".join(lines)

        sales_label = tk.Label(self.root, text=sales_count_str, font=("Helvetica", 14), justify="left")
        sales_label.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard)
        back_button.pack(pady=10)

    def manage_discounts_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Manage Ticket Discounts", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        # List current discounts
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        i = 0
        self.discount_vars = {}
        ticket_types = ["Single Pass", "Group", "Season", "Weekend"]
        for ttype in ticket_types:
            tk.Label(frame, text=f"{ttype} Discount (%)", font=("Helvetica", 14)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            var = tk.StringVar()
            discount_val = self.discounts.get(ttype, 0)*100
            var.set(str(discount_val))
            self.discount_vars[ttype] = var
            tk.Entry(frame, textvariable=var, font=("Helvetica", 14), width=8).grid(row=i, column=1, pady=5)
            i += 1

        save_button = tk.Button(self.root, text="Save Discounts", font=("Helvetica", 14), command=self.save_discounts)
        save_button.pack(pady=15)

        back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard)
        back_button.pack(pady=10)

    def save_discounts(self): #discounts
        # Validate and save discounts
        try:
            for ttype, var in self.discount_vars.items():
                val = float(var.get())
                if val < 0 or val > 100:
                    messagebox.showerror("Value Error", "Discount must be between 0 and 100")
                    return
                self.discounts[ttype] = val/100
            save_data(self.discounts, DISCOUNTS_FILE)
            messagebox.showinfo("Success", "Discounts saved successfully.")
        except Exception:
            messagebox.showerror("Invalid Input", "Please enter a valid number for discounts.")

    def manage_events_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Manage Events", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill="x")

        self.events_tree = ttk.Treeview(frame, columns=("Location", "Date", "Capacity", "Type"), show="headings", height=8)
        self.events_tree.heading("Location", text="Location")
        self.events_tree.heading("Date", text="Date")
        self.events_tree.heading("Capacity", text="Capacity")
        self.events_tree.heading("Type", text="Event Type")
        self.events_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.events_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.events_tree.configure(yscrollcommand=scrollbar.set)

        for event in self.events.values():
            self.events_tree.insert("", "end", iid=event.name, values=(event.location, event.date, event.totalCapacity, event.eventType))

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        add_button = tk.Button(buttons_frame, text="Add Event", width=15, command=self.add_event_dialog)
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(buttons_frame, text="Edit Event", width=15, command=self.edit_event_dialog)
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(buttons_frame, text="Delete Event", width=15, command=self.delete_event)
        delete_button.pack(side="left", padx=5)

        back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard)
        back_button.pack(pady=10)

    def add_event_dialog(self):
        dialog = EventDialog(self.root, "Add Event")
        self.root.wait_window(dialog.top)
        if dialog.result:
            name, location, date, capacity, eventType = dialog.result
            if name in self.events: #Exception
                messagebox.showerror("Duplicate Event", "An event with this name already exists.")
                return
            try: #
                capacity_int = int(capacity)
                new_event = Event(name, location, date, capacity_int, eventType)
                self.events[name] = new_event
                save_data(self.events, EVENTS_FILE)
                self.manage_events_screen()
                messagebox.showinfo("Success", "Event added successfully.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Capacity must be a number.")

    def edit_event_dialog(self):
        selected = self.events_tree.selection()
        if not selected:
            messagebox.showerror("Select Event", "Please select an event to edit.")
            return
        event_name = selected[0]
        event = self.events.get(event_name)
        if not event:
            messagebox.showerror("Error", "Selected event not found.")
            return
        dialog = EventDialog(self.root, "Edit Event", event)
        self.root.wait_window(dialog.top)
        if dialog.result:
            name, location, date, capacity, eventType = dialog.result
            if name != event_name and name in self.events:
                messagebox.showerror("Duplicate Event", "An event with this name already exists.")
                return
            try:
                capacity_int = int(capacity)
                # Update event attributes
                event.setName(name)
                event.setLocation(location)
                event.setDate(date)
                event.setTotalCapacity(capacity_int)
                event.setEventType(eventType)
                # If name changed
                if name != event_name:
                    self.events[name] = event
                    del self.events[event_name]
                save_data(self.events, EVENTS_FILE)
                self.manage_events_screen()
                messagebox.showinfo("Success", "Event updated successfully.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Capacity must be a number.")

    def delete_event(self):
        selected = self.events_tree.selection()
        if not selected:
            messagebox.showerror("Select Event", "Please select an event to delete.")
            return
        event_name = selected[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete event '{event_name}'? This cannot be undone.")
        if confirm:
            del self.events[event_name]
            save_data(self.events, EVENTS_FILE)
            self.manage_events_screen()
            messagebox.showinfo("Deleted", "Event deleted successfully.")

    def manage_users_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Manage Users (Customers)", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill="x")

        self.users_tree = ttk.Treeview(frame, columns=("Username", "Email", "Contact"), show="headings", height=8)
        self.users_tree.heading("Username", text="Username")
        self.users_tree.heading("Email", text="Email")
        self.users_tree.heading("Contact", text="Contact Number")
        self.users_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.users_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.users_tree.configure(yscrollcommand=scrollbar.set)

        for userID, user in self.users.items():
            if isinstance(user, Customer):
                self.users_tree.insert("", "end", iid=userID, values=(user.username, user.email, user.contactNumber))

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        add_button = tk.Button(buttons_frame, text="Add User", width=15, command=self.add_user_dialog)
        add_button.pack(side="left", padx=5)

        edit_button = tk.Button(buttons_frame, text="Edit User", width=15, command=self.edit_user_dialog)
        edit_button.pack(side="left", padx=5)

        delete_button = tk.Button(buttons_frame, text="Delete User", width=15, command=self.delete_user)
        delete_button.pack(side="left", padx=5)

        back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard)
        back_button.pack(pady=10)

    def add_user_dialog(self):
        dialog = UserDialog(self.root, "Add Customer")
        self.root.wait_window(dialog.top)
        if dialog.result:
            username, email, password, contact = dialog.result
            # Validate duplicate email
            for user in self.users.values():
                if user.email == email:
                    messagebox.showerror("Duplicate Email", "A user with this email already exists.")
                    return
            userID = self.generate_user_id()
            new_customer = Customer(userID, username, email, password, contact)
            self.users[userID] = new_customer
            save_data(self.users, USERS_FILE)
            self.manage_users_screen()
            messagebox.showinfo("Success", "User added successfully.")

    def edit_user_dialog(self):
        selected = self.users_tree.selection()
        if not selected:
            messagebox.showerror("Select User", "Please select a user to edit.")
            return
        userID = selected[0]
        user = self.users.get(userID)
        if not user:
            messagebox.showerror("Error", "Selected user not found.")
            return
        dialog = UserDialog(self.root, "Edit Customer", user)
        self.root.wait_window(dialog.top)
        if dialog.result:
            username, email, password, contact = dialog.result
            # Duplicate email check except for current user
            for uid, u in self.users.items():
                if u.email == email and uid != userID:
                    messagebox.showerror("Duplicate Email", "Another user with this email exists.")
                    return
            user.username = username
            user.email = email
            user.password = password
            user.contactNumber = contact
            save_data(self.users, USERS_FILE)
            self.manage_users_screen()
            messagebox.showinfo("Success", "User updated successfully.")

    def delete_user(self):
        selected = self.users_tree.selection()
        if not selected:
            messagebox.showerror("Select User", "Please select a user to delete.")
            return
        userID = selected[0]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete user '{self.users[userID].username}'? This cannot be undone.")
        if confirm:
            del self.users[userID]
            save_data(self.users, USERS_FILE)
            self.manage_users_screen()
            messagebox.showinfo("Deleted", "User deleted successfully.")

    ####################
    # Customer methods #
    ####################
    def customer_login_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Customer Login", font=("Helvetica", 22, "bold"))
        label.pack(pady=20)

        email_label = tk.Label(self.root, text="Email:", font=("Helvetica", 14))
        email_label.pack()
        self.customer_email_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.customer_email_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:", font=("Helvetica", 14))
        password_label.pack()
        self.customer_password_entry = tk.Entry(self.root, show="*", font=("Helvetica", 14))
        self.customer_password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", font=("Helvetica", 14), command=self.customer_login)
        login_button.pack(pady=10)

        register_link = tk.Button(self.root, text="Register New Account", font=("Helvetica", 12), fg="blue", command=self.customer_register_screen)
        register_link.pack()

        back_button = tk.Button(self.root, text="Back", font=("Helvetica", 12), command=self.main_choice_screen)
        back_button.pack(pady=10)

    def customer_login(self):
        email = self.customer_email_entry.get().strip()
        password = self.customer_password_entry.get().strip()

        login_user = None
        for user in self.users.values():
            if isinstance(user, Customer) and user.email == email and user.password == password:
                login_user = user
                break

        if login_user:
            self.current_user = login_user
            messagebox.showinfo("Login Success", f"Welcome, {login_user.username}!")
            self.customer_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    def customer_register_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Customer Registration", font=("Helvetica", 22, "bold"))
        label.pack(pady=15)

        row = 0
        entry_labels = ["Username", "Email", "Password", "Contact Number"]
        self.reg_entries = {}
        for lbl_text in entry_labels:
            label = tk.Label(self.root, text=f"{lbl_text}:", font=("Helvetica", 14))
            label.pack()
            ent = tk.Entry(self.root, font=("Helvetica", 14))
            if lbl_text == "Password":
                ent.config(show="*")
            ent.pack(pady=2)
            self.reg_entries[lbl_text] = ent
            row += 1

        register_btn = tk.Button(self.root, text="Register", font=("Helvetica", 14), command=self.customer_register)
        register_btn.pack(pady=10)

        back_btn = tk.Button(self.root, text="Back", font=("Helvetica", 12), command=self.customer_login_screen)
        back_btn.pack(pady=10)

    def customer_register(self):
        username = self.reg_entries["Username"].get().strip()
        email = self.reg_entries["Email"].get().strip()
        password = self.reg_entries["Password"].get().strip()
        contact = self.reg_entries["Contact Number"].get().strip()

        if not (username and email and password and contact):
            messagebox.showerror("Invalid Input", "All fields are required.")
            return

        # Check email uniqueness
        for user in self.users.values():
            if user.email.lower() == email.lower():
                messagebox.showerror("Duplicate Email", "A user with this email already exists.")
                return

        userID = self.generate_user_id()
        new_customer = Customer(userID, username, email, password, contact)
        self.users[userID] = new_customer
        save_data(self.users, USERS_FILE)
        messagebox.showinfo("Success", "Registration successful. You can now log in.")
        self.customer_login_screen()

    def customer_dashboard(self):
        self.clear_screen()
        label = tk.Label(self.root, text=f"Welcome, {self.current_user.username}", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        view_tickets_button = tk.Button(self.root, text="View and Purchase Tickets", font=("Helvetica", 14), width=30, command=self.ticket_purchase_screen)
        view_tickets_button.pack(pady=10)

        view_history_button = tk.Button(self.root, text="View Purchase History", font=("Helvetica", 14), width=30, command=self.purchase_history_screen)
        view_history_button.pack(pady=10)

        logout_button = tk.Button(self.root, text="Logout", font=("Helvetica", 12), command=self.logout)
        logout_button.pack(pady=20)

    def ticket_purchase_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Available Events", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        if not self.events:
            no_events_label = tk.Label(self.root, text="No events available at the moment.", font=("Helvetica", 14))
            no_events_label.pack()
            back_button = tk.Button(self.root, text="Back", command=self.customer_dashboard)
            back_button.pack(pady=10)
            return

        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.events_listbox = tk.Listbox(frame, font=("Helvetica", 14), height=8)
        self.events_listbox.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        self.events_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.events_listbox.yview)

        for event in self.events.values():
            self.events_listbox.insert(tk.END, f"{event.name} | {event.date} | {event.location} | {event.eventType}")

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        select_button = tk.Button(button_frame, text="Select Event", font=("Helvetica", 14), command=self.select_event_to_purchase)
        select_button.pack(side="left", padx=10)

        back_button = tk.Button(button_frame, text="Back", font=("Helvetica", 12), command=self.customer_dashboard)
        back_button.pack(side="left", padx=10)

    def select_event_to_purchase(self):
        selected = self.events_listbox.curselection()
        if not selected:
            messagebox.showerror("Select Event", "Please select an event.")
            return
        idx = selected[0]
        event_name = list(self.events.keys())[idx]
        self.current_event = self.events[event_name]
        self.show_tickets_for_event()

    def show_tickets_for_event(self):
        self.clear_screen()
        label = tk.Label(self.root, text=f"Tickets for {self.current_event.name}", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        # Tickets selection frame
        tickets_frame = tk.Frame(self.root)
        tickets_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Treeview for tickets
        self.tickets_tree = ttk.Treeview(tickets_frame, columns=("Type", "Price", "Seat", "Available"), show="headings", height=8)
        self.tickets_tree.heading("Type", text="Type")
        self.tickets_tree.heading("Price", text="Price ($)")
        self.tickets_tree.heading("Seat", text="Seat Number")
        self.tickets_tree.heading("Available", text="Available")
        self.tickets_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tickets_frame, orient="vertical", command=self.tickets_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tickets_tree.configure(yscrollcommand=scrollbar.set)

        # Insert available tickets with discounted price
        for ticket in self.current_event.getTicketList():
            if ticket.getisAvailable():
                disc_price = round(ticket.calculateDiscount(self.discounts),2)
                self.tickets_tree.insert("", "end", iid=ticket.ticketID, values=(ticket.getType(), f"{disc_price:.2f}", ticket.getSeatNumber(), "Yes"))

        buy_button = tk.Button(self.root, text="Buy Selected Ticket", font=("Helvetica", 14), command=self.purchase_selected_ticket)
        buy_button.pack(pady=8)

        back_button = tk.Button(self.root, text="Back to Events", font=("Helvetica", 12), command=self.ticket_purchase_screen)
        back_button.pack(pady=10)

    def purchase_selected_ticket(self):
        selected = self.tickets_tree.selection()
        if not selected:
            messagebox.showerror("Select Ticket", "Please select a ticket to purchase.")
            return
        ticket_id = selected[0]

        ticket = None
        for t in self.current_event.getTicketList():
            if t.getTicketID() == ticket_id:
                ticket = t
                break

        if ticket is None or not ticket.getisAvailable():
            messagebox.showerror("Unavailable", "Selected ticket is not available.")
            return

        # Proceed to payment screen
        self.payment_screen(ticket)

    def payment_screen(self, ticket):
        self.clear_screen()
        label = tk.Label(self.root, text="Payment", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        price_to_pay = ticket.calculateDiscount(self.discounts)
        price_label = tk.Label(self.root, text=f"Ticket Type: {ticket.getType()}", font=("Helvetica", 14))
        price_label.pack()
        price_label2 = tk.Label(self.root, text=f"Price after discount: ${price_to_pay:.2f}", font=("Helvetica", 14))
        price_label2.pack(pady=5)

        payment_type_label = tk.Label(self.root, text="Select Payment Method:", font=("Helvetica", 14))
        payment_type_label.pack(pady=10)

        self.payment_var = tk.StringVar()
        self.payment_var.set("Card")

        card_rb = tk.Radiobutton(self.root, text="Credit/Debit Card", variable=self.payment_var, value="Card", font=("Helvetica", 12), command=self.show_payment_fields)
        card_rb.pack()
        cash_rb = tk.Radiobutton(self.root, text="Cash", variable=self.payment_var, value="Cash", font=("Helvetica", 12), command=self.show_payment_fields)
        cash_rb.pack()

        # Frame for dynamic payment fields
        self.payment_fields_frame = tk.Frame(self.root)
        self.payment_fields_frame.pack(pady=10)

        self.show_payment_fields()  # Show card fields by default

        pay_btn = tk.Button(self.root, text="Confirm Payment", font=("Helvetica", 14), command=lambda: self.process_payment(ticket))
        pay_btn.pack(pady=15)

        back_btn = tk.Button(self.root, text="Back to Tickets", font=("Helvetica", 12), command=self.show_tickets_for_event)
        back_btn.pack(pady=10)

    def show_payment_fields(self):
        # Clear previous fields
        for widget in self.payment_fields_frame.winfo_children():
            widget.destroy()

        if self.payment_var.get() == "Card":
            # Card payment fields
            labels = ["Card Number (16 digits)", "Cardholder Name", "Expiry (MM/YY)", "CVV (3 digits)"]
            self.payment_entries = {}

            for l in labels:
                label = tk.Label(self.payment_fields_frame, text=l + ":", font=("Helvetica", 12))
                label.pack()
                entry = tk.Entry(self.payment_fields_frame, font=("Helvetica", 12))
                if "CVV" in l:
                    entry.config(show="*")
                entry.pack(pady=3)
                self.payment_entries[l] = entry

        else:
            # Cash payment field - cash received
            label = tk.Label(self.payment_fields_frame, text="Cash Received ($)", font=("Helvetica", 12))
            label.pack()
            entry = tk.Entry(self.payment_fields_frame, font=("Helvetica", 12))
            entry.pack(pady=3)
            self.payment_entries = {"Cash Received": entry}

    def process_payment(self, ticket):
        ptype = self.payment_var.get()
        amount = ticket.calculateDiscount(self.discounts)
        paymentDate = datetime.now()

        paymentID = self.generate_payment_id()

        if ptype == "Card":
            card_num = self.payment_entries["Card Number (16 digits)"].get().strip()
            holder_name = self.payment_entries["Cardholder Name"].get().strip()
            expiry = self.payment_entries["Expiry (MM/YY)"].get().strip()
            cvv = self.payment_entries["CVV (3 digits)"].get().strip()

            if not (card_num and holder_name and expiry and cvv):
                messagebox.showerror("Input Error", "All card fields are required.")
                return

            payment = CreditDebitCard(paymentID, amount, paymentDate, card_num, holder_name, expiry, cvv)
            if not payment.validateCard():
                messagebox.showerror("Payment Error", "Invalid card details.")
                return

        else:
            cash_received_str = self.payment_entries["Cash Received"].get().strip()
            try:
                cash_received = float(cash_received_str)
            except ValueError:
                messagebox.showerror("Input Error", "Cash received must be a number.")
                return

            if cash_received < amount:
                messagebox.showerror("Payment Error", "Insufficient cash received.")
                return

            payment = Cash(paymentID, amount, paymentDate, cash_received)
            if not payment.processPayment():
                messagebox.showerror("Payment Error", "Cash payment failed.")
                return

        # Process payment
        success = payment.processPayment()
        if not success:
            messagebox.showerror("Payment Failed", "Payment could not be processed.")
            return

        # Create booking and update data
        bookingID = self.generate_booking_id()
        booking = Booking(bookingID, self.current_user, ticket, paymentDate)
        booking.setPayment(payment)
        booking.confirmBooking()

        self.bookings[bookingID] = booking
        self.current_user.makeBooking(booking)
        ticket.setAvailable(False)

        save_data(self.bookings, BOOKINGS_FILE)
        save_data(self.users, USERS_FILE)

        messagebox.showinfo("Success", f"Booking confirmed!\nBooking ID: {bookingID}\nSeat Number: {ticket.getSeatNumber()}\nChange Given: ${getattr(payment, 'changeGiven', 0):.2f}")

        # Return to customer dashboard
        self.customer_dashboard()

    def purchase_history_screen(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Purchase History", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        bookings = self.current_user.viewPurchaseHistory()

        columns = ("Booking ID", "Event", "Ticket Type", "Seat Number", "Price", "Booking Date", "Status")
        tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, minwidth=50, width=100, stretch=False)

        tree.pack(padx=10, pady=10, fill="x")

        for b in bookings:
            event_name = "N/A"
            # try to find event from ticket
            for event in self.events.values():
                if b.ticket in event.ticketList:
                    event_name = event.name
                    break
            tree.insert("", "end", iid=b.bookingID, values=(
                b.bookingID, event_name, b.ticket.getType(), b.ticket.getSeatNumber(),
                f"${b.ticket.getPrice():.2f}", b.bookingDate.strftime("%Y-%m-%d %H:%M"), b.status
            ))

        back_btn = tk.Button(self.root, text="Back", font=("Helvetica", 12), command=self.customer_dashboard)
        back_btn.pack(pady=10)

    def logout(self):
        self.current_user = None
        self.current_event = None
        self.main_choice_screen()

    ###############
    # ID Generators
    ###############
    def generate_user_id(self):
        while True:
            uid = "CUST" + ''.join(random.choices(string.digits, k=4))
            if uid not in self.users:
                return uid

    def generate_booking_id(self):
        while True:
            bid = "BOOK" + ''.join(random.choices(string.digits, k=6))
            if bid not in self.bookings:
                return bid

    def generate_payment_id(self):
        # Simple random ID for payments
        return "PAY" + ''.join(random.choices(string.digits, k=6))

# Event add/edit dialog for admin events management
class EventDialog:
    def __init__(self, parent, title, event=None):
        top = self.top = tk.Toplevel(parent)
        top.title(title)
        self.parent = parent
        self.result = None

        tk.Label(top, text="Event Name:", font=("Helvetica", 12)).pack(pady=5)
        self.name_entry = tk.Entry(top, font=("Helvetica", 12))
        self.name_entry.pack()

        tk.Label(top, text="Location:", font=("Helvetica", 12)).pack(pady=5)
        self.location_entry = tk.Entry(top, font=("Helvetica", 12))
        self.location_entry.pack()

        tk.Label(top, text="Date (YYYY-MM-DD):", font=("Helvetica", 12)).pack(pady=5)
        self.date_entry = tk.Entry(top, font=("Helvetica", 12))
        self.date_entry.pack()

        tk.Label(top, text="Total Capacity:", font=("Helvetica", 12)).pack(pady=5)
        self.capacity_entry = tk.Entry(top, font=("Helvetica", 12))
        self.capacity_entry.pack()

        tk.Label(top, text="Event Type:", font=("Helvetica", 12)).pack(pady=5)
        self.event_type_entry = tk.Entry(top, font=("Helvetica", 12))
        self.event_type_entry.pack()

        button_frame = tk.Frame(top)
        button_frame.pack(pady=15)

        ok_btn = tk.Button(button_frame, text="OK", width=10, command=self.ok)
        ok_btn.pack(side="left", padx=5)
        cancel_btn = tk.Button(button_frame, text="Cancel", width=10, command=self.cancel)
        cancel_btn.pack(side="left")

        if event:
            self.name_entry.insert(0, event.getName())
            self.location_entry.insert(0, event.getLocation())
            self.date_entry.insert(0, event.getDate())
            self.capacity_entry.insert(0, event.getTotalCapacity())
            self.event_type_entry.insert(0, event.getEventType())

    def ok(self):
        name = self.name_entry.get().strip()
        location = self.location_entry.get().strip()
        date = self.date_entry.get().strip()
        capacity = self.capacity_entry.get().strip()
        eventType = self.event_type_entry.get().strip()

        if not (name and location and date and capacity and eventType):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        # Validate date format YYYY-MM-DD
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Input Error", "Date must be in format YYYY-MM-DD.")
            return

        self.result = (name, location, date, capacity, eventType)
        self.top.destroy()

    def cancel(self):
        self.top.destroy()

# User add/edit dialog for admin user management
class UserDialog:
    def __init__(self, parent, title, user=None):
        top = self.top = tk.Toplevel(parent)
        top.title(title)
        self.parent = parent
        self.result = None

        tk.Label(top, text="Username:", font=("Helvetica", 12)).pack(pady=5)
        self.username_entry = tk.Entry(top, font=("Helvetica", 12))
        self.username_entry.pack()

        tk.Label(top, text="Email:", font=("Helvetica", 12)).pack(pady=5)
        self.email_entry = tk.Entry(top, font=("Helvetica", 12))
        self.email_entry.pack()

        tk.Label(top, text="Password:", font=("Helvetica", 12)).pack(pady=5)
        self.password_entry = tk.Entry(top, font=("Helvetica", 12), show="*")
        self.password_entry.pack()

        tk.Label(top, text="Contact Number:", font=("Helvetica", 12)).pack(pady=5)
        self.contact_entry = tk.Entry(top, font=("Helvetica", 12))
        self.contact_entry.pack()

        button_frame = tk.Frame(top)
        button_frame.pack(pady=15)

        ok_btn = tk.Button(button_frame, text="OK", width=10, command=self.ok)
        ok_btn.pack(side="left", padx=5)
        cancel_btn = tk.Button(button_frame, text="Cancel", width=10, command=self.cancel)
        cancel_btn.pack(side="left")

        if user:
            self.username_entry.insert(0, user.username)
            self.email_entry.insert(0, user.email)
            self.password_entry.insert(0, user.password)
            self.contact_entry.insert(0, user.contactNumber)

    def ok(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        contact = self.contact_entry.get().strip()

        if not (username and email and password and contact):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        # Basic email validation (very minimal)
        if "@" not in email or "." not in email:
            messagebox.showerror("Input Error", "Invalid email address.")
            return

        self.result = (username, email, password, contact)
        self.top.destroy()

    def cancel(self):
        self.top.destroy()

# Generate initial data for testing and tickets for events with seat numbers
def generate_sample_data():
    # Check if data already exists
    if os.path.exists(USERS_FILE) and os.path.exists(EVENTS_FILE) and os.path.exists(BOOKINGS_FILE):
        return

    users = {}
    events = {}
    bookings = {}
    discounts = {"Single Pass": 0.10, "Group": 0.15, "Season": 0.25, "Weekend": 0.10}

    # Default admin
    admin = Admin("admin001", "admin", "admin@example.com", "1234", "0000000000")
    users[admin.userID] = admin

    # Sample Customer
    cust = Customer("cust001", "John Doe", "john@example.com", "password", "1234567890")
    users[cust.userID] = cust

    # Create sample events
    event1 = Event("Grand Prix Monaco", "Monaco", "2024-05-26", 100, "Formula 1")
    event2 = Event("Grand Prix Silverstone", "UK", "2024-07-14", 120, "Formula 1")

    # Generate tickets for event1
    seat_letters = ['A', 'B', 'C', 'D', 'E']
    ticket_id_counter = 1000
    for row_letter in seat_letters:
        for seat_num in range(1, 21):
            seat_str = f"{row_letter}{seat_num}"
            ticket_id = f"T{ticket_id_counter}"
            price = 150.0
            # Alternate ticket types for diversity
            if seat_num % 4 == 1:
                ticket = SinglePassTicket(ticket_id, price, seat_str, "2024-05-26")
            elif seat_num % 4 == 2:
                ticket = GroupTicket(ticket_id, price*0.95, seat_str, 4)
            elif seat_num % 4 == 3:
                ticket = SeasonTicket(ticket_id, price*0.90, seat_str, "2024 Season")
            else:
                ticket = WeekendTicket(ticket_id, price*1.10, seat_str, "2024-05-25 to 2024-05-26")
            event1.addTicket(ticket)
            ticket_id_counter += 1

    # Similarly for event2
    for row_letter in seat_letters:
        for seat_num in range(1, 21):
            seat_str = f"{row_letter}{seat_num}"
            ticket_id = f"T{ticket_id_counter}"
            price = 200.0
            ticket = SinglePassTicket(ticket_id, price, seat_str, "2024-07-14")
            event2.addTicket(ticket)
            ticket_id_counter += 1

    events[event1.name] = event1
    events[event2.name] = event2

    save_data(users, USERS_FILE)
    save_data(events, EVENTS_FILE)
    save_data(bookings, BOOKINGS_FILE)
    save_data(discounts, DISCOUNTS_FILE)

    def show_tickets_for_event(self):
        self.clear_screen()
        label = tk.Label(self.root, text=f"Tickets for {self.current_event.name}", font=("Helvetica", 20, "bold"))
        label.pack(pady=15)

        # Tickets selection frame
        tickets_frame = tk.Frame(self.root)
        tickets_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Treeview for tickets
        self.tickets_tree = ttk.Treeview(tickets_frame, columns=("Type", "Price", "Seat", "Available"), show="headings",
                                         height=8)
        self.tickets_tree.heading("Type", text="Type")
        self.tickets_tree.heading("Price", text="Price ($)")
        self.tickets_tree.heading("Seat", text="Seat Number")
        self.tickets_tree.heading("Available", text="Available")
        self.tickets_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tickets_frame, orient="vertical", command=self.tickets_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tickets_tree.configure(yscrollcommand=scrollbar.set)

        # Insert available tickets with discounted price
        for ticket in self.current_event.getAvailableTickets():
            disc_price = round(ticket.calculateDiscount(self.discounts), 2)
            self.tickets_tree.insert("", "end", iid=ticket.ticketID,
                                     values=(ticket.getType(), f"{disc_price:.2f}", ticket.getSeatNumber(), "Yes"))

        # Update button for purchasing selected tickets
        buy_button = tk.Button(self.root, text="Buy Selected Ticket", font=("Helvetica", 14),
                               command=self.purchase_selected_ticket)
        buy_button.pack(pady=8)

        back_button = tk.Button(self.root, text="Back to Events", font=("Helvetica", 12),
                                command=self.ticket_purchase_screen)
        back_button.pack(pady=10)

    def purchase_selected_ticket(self):
        selected = self.tickets_tree.selection()
        if not selected:
            messagebox.showerror("Select Ticket", "Please select a ticket to purchase.")
            return

        for ticket_id in selected:
            ticket = None
            for t in self.current_event.getTicketList():
                if t.getTicketID() == ticket_id:
                    ticket = t
                    break

            if ticket is None:
                messagebox.showerror("Unavailable", "Selected ticket is not available.")
                return

            # Mark the ticket as unavailable
            ticket.setAvailable(False)

            # Proceed to payment screen for each selected ticket
            self.payment_screen(ticket)


if __name__ == "__main__":
    generate_sample_data()
    root = tk.Tk()
    app = GrandPrixExperienceApp(root)
    root.mainloop()



