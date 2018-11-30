import random
import os
import bruteforce as bruteforce
import bottomup as bottom_up
import topdown as topdown
import utils as utils

def main():
    runExperiments();

#############################################
# EXPERIMENTS
# Generate random data.
# 1 - Fixed n, varried W:
def runExperiments():
    print("======> Running Experiments...")
    #Generate randome int array for weights and values
    # array's len = 10, random int from [start, end], capacity W random
    n = 10; start=10; end=100;
    Weights = utils.generateData(n, start, end)
    Values = utils.generateData(n, start, end)

    print("=======================================")
    print("Weights={}, Values={}".format(Weights,Values))
    # run this 100 times:
    for i in range(10):

        W = random.randint(start,end)

        print("W={}".format(W))

        # Calling bruteforce:
        bf = bruteforce.knapsack_brute_force(Weights, Values, W);
        # print("BruteForce optimalSet={}, duration(ms)={}".format(bf[0], bf[1]))
        fileName = "experiments/"+str(n)+"n_varried_W.csv"

        # Calling bottom up:
        bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);
        # print("BruteForce optimalSet={}, duration(ms)={}".format(bf[0], bf[1]))
        fileName = "experiments/"+str(n)+"n_varried_W.csv"

        # Calling top down:
        # td = topdown.knapsack_top_down_dp(Weights, Values, W);
        # print("TopDown optimalSet={}, duration(ms)={}".format(bf[0], bf[1]))

        # data[capacity, n, bruteforce time, bottom up time, topdown time]
        data = [str(W), str(n), "%.3f" % bf[1], "%.3f" % bu[1], "%.3f" % 0.0]
        # data = [str(W), str(n), "%.3f" % bf[1], "%.3f" % bu[1], "%.3f" % td[1]]
        writeToFile(fileName, data) # recording the time it takes.



# Append or create a file:
# Save data to file, csv: W, n, time
# example: "experiments/10n_varried_W.txt" for n=10
def writeToFile(fileName, data):
    exists = os.path.isfile(fileName)
    if not exists:
        f = open(fileName, "w")
        f.write("Capacity,n,BruteForce,BottomUp,TopDown" + "\n") #create and write header
    else:
        f = open(fileName, "a")
    # just append data:
    f.write((",").join(data) + "\n")


#main
if __name__ == '__main__':
    main()
