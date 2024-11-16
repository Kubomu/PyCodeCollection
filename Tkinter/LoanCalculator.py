# LoanCalculator.py

from tkinter import *  # Import all definitions from tkinter

class LoanCalculator:
    """
    A GUI-based loan calculator that computes monthly payment and total payment.

    Example:
        >>> calculator = LoanCalculator()
        >>> calculator.computePayment()
    """

    def __init__(self): 
        """
        Initialize the loan calculator GUI.
        """
        window = Tk()  # Create a window
        window.title("Loan Calculator")  # Set title

        Label(window, text="Annual Interest Rate:").grid(row=1, column=1, sticky=W)  
        Label(window, text="Number of Years:").grid(row=2, column=1, sticky=W) 
        Label(window, text="Loan Amount:").grid(row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment:").grid(row=4, column=1, sticky=W)
        Label(window, text="Total Payment:").grid(row=5, column=1, sticky=W)
        Label(window, text='Thank You For Using My Calculator!!', bg='blue').place(x=150, y=150)

        self.annualInterestRateVar = StringVar()                
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        self.monthlyPaymentVar = StringVar()
        lblMonthPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar() 
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        btComputePayment = Button(window, text='Compute Payment:', command=self.computePayment).grid(row=6, column=2, sticky=E)

        window.mainloop()  # Create an event loop

    def computePayment(self):
        """
        Compute the monthly payment and total payment based on user input.

        Example:
            >>> calculator = LoanCalculator()
            >>> calculator.loanAmountVar.set("200000")
            >>> calculator.annualInterestRateVar.set("6")
            >>> calculator.numberOfYearsVar.set("30")
            >>> calculator.computePayment()
        """
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get())
        )
        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        """
        Compute the monthly payment based on the formula:
        M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

        Args:
            loanAmount (float): The loan amount
            monthlyInterestRate (float): The monthly interest rate
            numberOfYears (int): The number of years

        Returns:
            float: The monthly payment

        Example:
            >>> calculator = LoanCalculator()
            >>> calculator.getMonthlyPayment(200000, 0.005, 30)
        """
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment


# Create GUI
LoanCalculator()