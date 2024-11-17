def steps():
    """
    Returns a list of tuples representing steps and their likelihood of falling.
    """
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]
    return likelihoods

def run_task3():
    """
    Categorizes steps as good or bad based on their likelihood of falling and displays the result.
    """
    likelihoods = steps()  # Retrieve the list of steps
    good_steps = []  # List to store good steps
    bad_steps = []   # List to store bad steps

    for step, likelihood in likelihoods:
        if likelihood >= 50:
            bad_steps.append((step, likelihood))  # Add to bad steps
        else:
            good_steps.append((step, likelihood))  # Add to good steps

    # Display the result
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

# Example of calling the main function
run_task3()
