from datetime import *

def diffDate():
    now = datetime.date(datetime.now())
    d = date(2021, 12, 3)
    delta = now - d
    return delta.days

print(diffDate())