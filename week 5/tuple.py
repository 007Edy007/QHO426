def likelihood():
    """
    Returns the step with the smallest likelihood of falling from a tuple of likelihoods.
    """
    likelihoods = (50, 38, 27, 99, 4)  # Create the tuple with likelihood values
    return min(likelihoods)  # Return the smallest value in the tuple

def run_task1():
    """
    Calls the likelihood function and displays the minimum likelihood of falling.
    """
    min_likelihood = likelihood()  # Call the likelihood function
    print(f"Minimum likelihood of falling: {min_likelihood}%")  # Display the result
run_task1()