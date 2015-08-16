import slate

with open('example.pdf') as f:
    doc = slate.PDF(f)
    print(doc)
