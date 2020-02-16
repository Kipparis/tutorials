#!python3

company = input('enter job: ')
with open('q.txt', 'r') as f:
    with open('companies/{}.txt'.format(company), 'w') as out:
        # content = f.read()
        # print(content)
        for i, row in enumerate(f):
            answer = input("{}) {}".format(i, row))
            
            out.write("{}. {}>>>{}\n\n".format(i, row, answer))
