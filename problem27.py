'''

Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.

'''

def flatten_dict(nested_dict, parent_key='', separator='.'):
    """
    Flattens a nested dictionary by concatenating keys with a separator.

    Args:
        nested_dict (dict): The dictionary to flatten.
        parent_key (str): The base key string for the current recursion level.
        separator (str): The string used to separate keys.

    Returns:
        dict: A flattened dictionary with concatenated keys.
    """
    flattened = {}
    for key, value in nested_dict.items():
        # Construct the new key
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        
        if isinstance(value, dict):
            # Recursively flatten the sub-dictionary
            flattened.update(flatten_dict(value, new_key, separator))
        else:
            # Assign the value to the new key in the flattened dictionary
            flattened[new_key] = value
    return flattened

# Example usage:
if __name__ == "__main__":
    nested = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    flattened = flatten_dict(nested)
    print(flattened)
    # Output:
    # {'key': 3, 'foo.a': 5, 'foo.bar.baz': 8}
