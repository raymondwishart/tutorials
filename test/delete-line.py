with open('/home/rwishart/Python-scripts/known-hosts', 'r+') as f:
    t = f.read()
    to_delete = input('What should we delete? : ').strip()
    f.seek(0)
    for line in t.split('\n'):
        if line != to_delete:
            f.write(line + '\n')
    f.truncate()
