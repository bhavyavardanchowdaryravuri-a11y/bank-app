import streamlit as st

# Bank Application Class
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✅ Transaction successful. Withdrawn ₹{amount}"
        else:
            return "❌ Insufficient balance"

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposited ₹{amount}"

    def update_mob_num(self, new_num):
        self.mobile_number = new_num
        return f"📱 Updated Mobile: {self.mobile_number}"

    def check_balance(self):
        return f"💰 Balance: ₹{self.balance}"


# Streamlit UI
st.title("🏦 Bank Application")

# Initialize session state
if "account" not in st.session_state:
    st.session_state.account = None

# Create Account Section
st.header("Create Account")

name = st.text_input("Name")
account_number = st.text_input("Account Number")
age = st.number_input("Age", min_value=1)
mobile_number = st.text_input("Mobile Number")
balance = st.number_input("Initial Balance", min_value=0)

if st.button("Create Account"):
    st.session_state.account = BankApplication(
        name, account_number, age, mobile_number, balance
    )
    st.success("Account Created Successfully!")

# If account exists → show operations
if st.session_state.account:
    st.header("Bank Operations")

    option = st.selectbox(
        "Choose Operation",
        ["Deposit", "Withdraw", "Check Balance", "Update Mobile"]
    )

    acc = st.session_state.account

    if option == "Deposit":
        amount = st.number_input("Enter deposit amount", min_value=0)
        if st.button("Deposit"):
            st.success(acc.deposit(amount))

    elif option == "Withdraw":
        amount = st.number_input("Enter withdraw amount", min_value=0)
        if st.button("Withdraw"):
            st.success(acc.withdraw(amount))

    elif option == "Check Balance":
        if st.button("Check"):
            st.info(acc.check_balance())

    elif option == "Update Mobile":
        new_num = st.text_input("Enter new mobile number")
        if st.button("Update"):
            st.success(acc.update_mob_num(new_num))