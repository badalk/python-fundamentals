###4 It pays to be lazy in generator pipeline

from stateful_generators import take
from stateful_generators_2 import distinct

def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)): ## the internal generator does not process the whole source list as take only prints the first 3 distinct items. and hence it pays to be lazy
        print (item)

if __name__ == "__main__":
    run_pipeline()


