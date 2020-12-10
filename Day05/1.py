import string

with open(r"input") as f:
    seats = set()
    lines = f.read().split('\n')
    for line in lines:
        row_ids = list(range(128))
        rows = line[0:7]
        for row in rows:
            if row == "F":
                row_ids = row_ids[:len(row_ids)//2]
            else:
                row_ids = row_ids[len(row_ids)//2:]
        row_result = row_ids[0]

        column_ids = list(range(8))
        columns = line[7:]
        for column in columns:
            if column == "L":
                column_ids = column_ids[:len(column_ids)//2]
            else:
                column_ids = column_ids[len(column_ids)//2:]
        column_result = column_ids[0]
        seats.add(row_result * 8 + column_result)
    # part 2
    total_seats = set()
    for i in range(128):
        for j in range(8):
            for k in range(8):
                total_seats.add(i*j + k)
    result = total_seats - seats
    print(result)