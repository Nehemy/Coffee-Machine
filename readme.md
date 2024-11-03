# Coffee Machine

This is a simple coffee machine program written in Python. It simulates a coffee machine where users can order coffee, insert coins, and receive change if needed. The machine can also generate a report showing available resources and accumulated money.

## Project Structure

- **coffeemachine.py**: Contains the main code for the coffee machine, including available resources, coffee menu, and logic for handling orders, payments, and reports.

## Features

1. **Order Coffee**: Users can choose between "espresso," "latte," and "cappuccino."
2. **Resource Management**: The machine checks if it has enough water, milk, and coffee for the selected drink before processing the order.
3. **Payment System**: Users are prompted to insert quarters, dimes, nickels, and pennies to pay for their coffee.
4. **Change Calculation**: If users pay more than the cost of the coffee, the program calculates and returns the change.
5. **Report Generation**: Displays remaining resources and total money earned by the machine.
6. **Power Off Option**: The machine can be turned off by entering "off" as the order.

## Usage

1. Run the program using Python:
   ```bash
   python coffeemachine.py

2. When prompted, enter your desired coffee type:

- **espresso**
- **latte**
- **cappuccino**

3. The machine will check resources and ask you to insert coins:

- **Quarters ($0.25 each)**
- **Dimes ($0.10 each)**
- **Nickels ($0.05 each)**
- **Pennies ($0.01 each)**

4. If there are enough resources and payment is sufficient, the coffee is dispensed, and change is returned if applicable.


5. To see the current resources and money earned, type "report" as the order. This will display:

- **Water remaining (in ml)**
- **Milk remaining (in ml)**
- **Coffee remaining (in g)**
- **Money accumulated in the machine**

6. To turn off the machine, type "off" as the order.