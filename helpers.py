# Convert processing code to function

def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats',  'authorStats ', 'challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    skiped_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    flatten_data = {}
    for idx, value in enumerate(data):
        flatten_data[idx] = {}
        for prop_idx, prop_value in value.items():
            if prop_idx in nested_values:
                if prop_idx in skiped_values:
                    pass
                else:
                    for nested_idx, nested_value in prop_value.items():
                        flatten_data[idx][prop_idx + '_' + nested_idx] = nested_value
            else:
                flatten_data[idx][prop_idx] = prop_value

    return flatten_data