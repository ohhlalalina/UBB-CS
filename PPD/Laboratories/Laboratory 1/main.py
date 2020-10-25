import threading
import time
from Tree import Tree
from change import Change
import random
import sys

keep_running: bool = True
tree = Tree()


def make_changes(thread_id):
    while keep_running:
        leaf = tree.get_random_leaf()
        old_value = leaf.value.getValue()
        parent = leaf.get_parents_leaf()
        change = Change(leaf, parent, random.randint(-30, 50))
        change.execute()
        print("The leaf with previous value " + str(old_value) + " was changed in value " + str(leaf.value.getValue()))
        time.sleep(random.uniform(0.1, 0.5))
    print("Thread: {} finished running.".format(thread_id))


def check():
    while keep_running:
        time.sleep(5)
        tree.validate_nodes()


if __name__ == '__main__':
    quit = "q"
    threads = [threading.Thread(target=make_changes, args=(index,), daemon=True) for index in range(10)]
    for thread in threads:
        thread.start()
    validity = threading.Thread(target=check, args=(), daemon=True)
    validity.start()
    while True:
        try:
            x = input()
            print(x)
            if x == quit:
                keep_running = False
                break
        except KeyboardInterrupt:
            print('You pressed Ctrl+C!')
            keep_running = False
            break
    for thread in threads:
        thread.join()
    tree.__str__()
    validity.join()


    sys.exit(0)
