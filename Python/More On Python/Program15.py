Code = input("Enter a color code")
ColorCodes = {
    'v': 'Violet',
    'i': 'Indigo',
    'b': 'Blue',
    'g': 'Green',
    'y': 'Yellow',
    'o': 'Orange',
    'r': 'Red'
}
if ColorCodes[Code]:
    print(Code)
else:
    print('Invalid option.')
