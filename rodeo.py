def rename_rodeo_columns(columns):
    new_columns = []
    for column in columns:
        new_column = ''
        for letter in column:
            if letter == ' ':
                new_column += '_'
            else:
                new_column += letter

        if new_column[-5:] == "_Data":
            new_column = new_column[:-5]
        new_columns += [new_column.lower()]
    return new_columns


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
