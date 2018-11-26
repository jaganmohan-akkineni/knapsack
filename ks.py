import random
import bruteforce as bruteforce;
import bottomup as bottom_up;
import topdown as topdown


def main():
    print("Hello, world!")
    Weights = generateData(5, 1,10)#[4,5,9,1,2,3]
    Values = generateData(5, 10, 100)#[10,20,15,10,20,15]
    W = 10

    # brute force:
    bf = bruteforce.Knapsack_bf(Weights, Values, W);
    td = topdown.Knapsack_topdown(Weights, Values, W);
    bu = bottom_up.Knapsack_bottomup(Weights, Values, W);

# generating arrays of weights and values of random int of length n:
def generateData(n, start, end):
    print("Generating data of length: {}, start={}, end={} ".format(n,start,end))
    arr = [];
    for x in range(n):
        arr.append(random.randint(start,end))

    return arr




if __name__ == '__main__':
    main()
