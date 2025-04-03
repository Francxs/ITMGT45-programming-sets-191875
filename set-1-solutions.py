def savings(gross_pay, tax_rate, expenses):
    """
    Calculate the money remaining for an employee after taxes and expenses.
    
    This implementation applies the tax rate to gross pay (rounding down),
    then subtracts expenses to determine remaining money.
    
    Args:
        gross_pay (int): Gross pay in centavos
        tax_rate (float): Tax rate as decimal between 0 and 1
        expenses (int): Expenses in centavos
        
    Returns:
        int: Remaining centavos after taxes and expenses
    """
    # Calculate after-tax pay (rounding down via integer division)
    after_tax = int(gross_pay * (1 - tax_rate))
    
    # Subtract expenses to get savings
    remaining = after_tax - expenses
    
    return remaining


def material_waste(total_material, material_units, num_jobs, job_consumption):
    """
    Calculate remaining material after jobs and format with units.
    
    Args:
        total_material (int): Total material available
        material_units (str): Units for material (e.g., "kg", "L")
        num_jobs (int): Number of jobs to run
        job_consumption (int): Material used per job
        
    Returns:
        str: Remaining material with units (e.g., "10kg")
    """
    # Calculate total material consumption
    total_consumption = num_jobs * job_consumption
    
    # Calculate remaining material
    remaining = total_material - total_consumption
    
    # Format with units as required
    return f"{remaining}{material_units}"


def interest(principal, rate, periods):
    """
    Calculate final value of an investment with simple interest.
    
    Uses the formula: final_value = principal + (principal * rate * periods)
    with the result rounded down.
    
    Args:
        principal (int): Initial investment in centavos
        rate (float): Interest rate per period as decimal
        periods (int): Number of time periods
        
    Returns:
        int: Final value of investment in centavos
    """
    # Calculate interest amount
    interest_amount = principal * rate * periods
    
    # Add interest to principal and round down
    final_value = int(principal + interest_amount)
    
    return final_value
