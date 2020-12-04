def viewTable(headings,data):
    for heads in headings:
        print("%5s" % heads,end="\t")
    print()
    for rows in data:
        for cols in rows:
            print("%5s" % cols,end="\t")
        print()
