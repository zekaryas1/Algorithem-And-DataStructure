import os


def diskusage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += diskusage(childpath)
    print ('{0:<7}'.format(total), path)
    return total

print(diskusage("D:\SOFTWARE ENGINEERING\YEAR2 EDUCATIONAL\ALL THE VIDEOS OF FIRST SEAMISTER\ALGORITHM"))