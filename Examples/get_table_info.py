from slides_configuration import *

table = slides_api.get_shape("test.pptx", 2, 4) #implies that shape #4 on slide #2 is a table

for ri, row in enumerate(table.rows):
    for ci, cell in enumerate(row.cells):
        print(f"row {ri + 1}")
        print(f"col {ci + 1}")
        print(cell.text)
        print()
