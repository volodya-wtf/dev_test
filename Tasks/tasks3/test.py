import sys

sys.path.insert(0, "..")

from tasks1.test import Database, original_example
from tasks2.test import get_new_filenames

## tasks2
new_names, duplicate_error = get_new_filenames("/usr/bin")

for name in new_names:
    print(f"{name:80}{new_names[name]}")

print(duplicate_error)


## tasks1
db = Database()
db.populate_db(original_example)

print(db.get_repair_for_customer("89002001020"))
print(db.get_repair_for_customer("89808564559"))