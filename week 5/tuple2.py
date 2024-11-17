def likelihood_min_max():
    """
    Returns the minimum and maximum likelihood of falling from a tuple of likelihoods.
    """
    likelihoods = (50, 38, 27, 99, 4)  # Create the tuple with likelihood values
    min_val = min(likelihoods)  # Find the minimum value
    max_val = max(likelihoods)  # Find the maximum value
    return min_val, max_val  # Return both values as a tuple

def run_task2():
    """
    Calls the likelihood_min_max function and displays the minimum and maximum likelihoods.
    """
    min_likelihood, max_likelihood = likelihood_min_max()  # Call the first function
    print(f"Minimum likelihood of falling: {min_likelihood}%")
    print(f"Maximum likelihood of falling: {max_likelihood}%")

# Example of calling the main function
run_task2()