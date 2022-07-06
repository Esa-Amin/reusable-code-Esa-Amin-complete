def rename_rodeo_columns(columns):
    # Replace this and the line below with your code...
    raise NotImplementedError


if __name__ == '__main__':
    # Create a list of exmple original column names
    original = [
        'Participant Count Data',
        'Rodeo Clown Count',
        'Hats Visible',
        'Cost Data',
    ]

    # Get the corrected column names
    corrected = rename_rodeo_columns(original)

    # Print a table to compare original and corrected names
    print('Original                  Corrected')
    print('--------                  ---------')
    for o, c in zip(original, corrected):
        print(f'{o:<25} {c:<25}')
