class Customer:
    def __init__(self, customer_id=None, customer_name=None, email=None, phone_number=None):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__email = email
        self.__phone_number = phone_number

    # Getters and Setters
    def getCustomerID(self):
        return self.__customer_id

    def getCustomerName(self):
        return self.__customer_name

    def setCustomerName(self, customer_name):
        self.__customer_name = customer_name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPhoneNumber(self):
        return self.__phone_number

    def setPhoneNumber(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return f"Customer ID: {self.__customer_id}\nCustomer Name: {self.__customer_name}, Email: {self.__email}, Phone Number: {self.__phone_number}\n"

