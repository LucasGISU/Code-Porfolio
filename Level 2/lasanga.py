EXPECTED_BAKE_TIME = 40


def bake_time_remaining(time):
    return EXPECTED_BAKE_TIME - time
    """Calculate the remaining baking time.
    :param time: int - minutes that lasagna has been in oven
    :return: int - number of minutes remaining until lasagna is done 
    
    This function takes two integers representing the number of minutes the recipe recommends to bake for and the time 
    already spent baking and calculates the number of minutes remaining to bake.
    """


def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2
    """Calculate preperation time based on number of layers
    :param number_of_layers: int - the number of layers in lasagna
    :return: int - total time spent preparing all layers of lasagna
    
    This function takes the number of layers in lasagna from user and calculates total time spent preparing  
    """


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    """Calculate elapsed cooking time
    :param number_of_layers: int - the number of layers in the lasagna
    :param elapsed_bake_time: int - time that has lasagna has already baked for
    :return: int - total time spent preparing and baking lasagna so far
    
    This function takes two integers for the number of lasagna layers and time spent baking so far and calculates the 
    total time spent on the lasagna so far
    """