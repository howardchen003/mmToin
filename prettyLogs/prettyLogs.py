#the goal is to make something that tabs at { and untabs at }. Has to look if next is {}
#also add \r after no more }

with open("old.txt") as f_old, open("new.txt", "w") as f_new:
    for line in f_old:
        f_new.write(line)
        if 'identifier' in line:
            f_new.write("extra stuff\n")