#!/usr/bin/env python3
import argparse

def calculate(num1, operation, num2):
    """
    Perform calculation based on the specified operation.
    
    Args:
        num1 (float): First number
        operation (str): Operation to perform (add, sub, mul, div)
        num2 (float): Second number
        
    Returns:
        float: Result of the calculation
        
    Raises:
        ValueError: If operation is invalid or division by zero is attempted
    """
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":
        return num1 * num2
    elif operation == "div":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="A simple command-line calculator that performs basic arithmetic operations."
    )
    
    # Add required arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operation", type=str, choices=["add", "sub", "mul", "div"], 
                        help="Operation to perform (add, sub, mul, div)")
    parser.add_argument("num2", type=float, help="Second number")
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Perform calculation
        result = calculate(args.num1, args.operation, args.num2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()