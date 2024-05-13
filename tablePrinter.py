tableData = [['appes', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)

    for column in range(len(table)):
        for word in table[column]:
            if len(word) > colWidths[column]:
                colWidths[column] = len(word)

    for row in range(len(table[0])):
        for column in range(len(table)):
            print(table[column][row].rjust(colWidths[column]), end=' ')
        print()

printTable(tableData)