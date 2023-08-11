def write_to_file(name, contact, req):
    with open("users.txt", "a") as wf:
        wf.write(f'{name} ----- {contact} ----- {req}\n')
