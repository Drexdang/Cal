import streamlit as st

def calculate_recoverable_amount(loan_amount, duration, interest_rate, admin_charges):
    # Calculate interest
    interest = loan_amount * (interest_rate / 100) * (duration / 12)
    
    # Calculate total amount to be recovered
    total_recoverable = loan_amount + interest + admin_charges
    
    return total_recoverable

def calculate_monthly_installment(recoverable_amount, duration):
    # Calculate monthly installment
    monthly_installment = recoverable_amount / duration
    return monthly_installment

def main():
    st.title("Loan Calculator")

    # Input features
    name = st.text_input("Enter customer's name:")
    loan_amount = st.number_input("Enter loan amount:", min_value=0.0, step=0.01, value=100000.0)
    duration = st.number_input("Enter duration (in months):", min_value=1, step=1, value=12)
    interest_rate = st.number_input("Enter interest rate (in percentage):", min_value=0.0, step=0.01, value=7.0)
    admin_charges = st.number_input("Enter admin charges:", min_value=0.0, step=0.01, value=500.0)

    if st.button("Calculate"):
        # Calculate recoverable amount
        recoverable_amount = calculate_recoverable_amount(loan_amount, duration, interest_rate, admin_charges)

        # Calculate monthly installment
        monthly_installment = calculate_monthly_installment(recoverable_amount, duration)

        # Output
        st.write("\nCustomer's Name:", name)
        st.write("Loan Amount:", loan_amount)
        st.write("Duration (months):", duration)
        st.write("Interest Rate (%):", interest_rate)
        st.write("Admin Charges:", admin_charges)
        st.write("Recoverable Amount:", recoverable_amount)
        st.write("Monthly Installment:", monthly_installment)

if __name__ == "__main__":
    main()