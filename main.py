import random
import os
import bruteforce as bruteforce
import bottomup as bottomup
import topdown as topdown
import utils as utils

def main():
    #runExperiments()
    runExperiments2()

#############################################
# EXPERIMENTS
# Generate random data.
# 1 - Fixed n, varried W:
def runExperiments():
    print("======> Running Experiments...")
    #Generate randome int array for weights and values
    # array's len = 10, random int from [start, end], capacity W random
    # TODO: create an array of n, then loop thru each n
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

        # Calling bottom up:
        bu = bottom_up.knapsack_bottom_up_dp(Weights, Values, W);

        # Calling top down:
        # td = topdown.knapsack_top_down_dp(Weights, Values, W);

        # data[capacity, n, bruteforce time, bottom up time, topdown time]
        fileName = "experiments/"+str(n)+"n_varried_W.csv"
        data = [str(W), str(n), "%.3f" % bf[1], "%.3f" % bu[1], "%.3f" % 0.0]
        # data = [str(W), str(n), "%.3f" % bf[1], "%.3f" % bu[1], "%.3f" % td[1]]
        writeToFile(fileName, data) # recording the time it takes.

#fixed W, varied n
def runExperiments2():
    Wlist = [50,100,500,1000]

    for i in range(len(Wlist)):
        for j in range(5, 21):
            start = 10
            end = 100
            Weights = utils.generateData(j, start, end)
            Values = utils.generateData(j, start, end)
            bf_runtime = 0
            bu_runtime = 0
            td_runtime = 0

            #run each method for 10 times and then take average
            for k in range(10):
                bf = bruteforce.knapsack_brute_force(Weights, Values, Wlist[i])
                bu = bottomup.knapsack_bottom_up_dp(Weights, Values, Wlist[i])
                td = topdown.knapsack_top_down_dp(Weights, Values, Wlist[i])

                bf_runtime = bf_runtime + bf[1]
                bu_runtime = bu_runtime + bu[1]
                td_runtime = td_runtime + td[1]

            bf_runtime = bf_runtime/10
            bu_runtime = bu_runtime/10
            td_runtime = td_runtime/10
            #fileName = "experiments/TDvsBU_"+str(Wlist[i])+"W_varried_n.csv"
            fileName = "experiments/ALL_W_varried_n.csv"

            # data[capacity, n, bruteforce time, bottom up time, topdown time]
            data = [str(Wlist[i]), str(j), "%.3f" % bf_runtime, "%.3f" % bu_runtime, "%.3f" % td_runtime]
            # data = [str(W), str(n), "%.3f" % bf[1], "%.3f" % bu[1], "%.3f" % td[1]]
            writeToFile(fileName, data) # recording the time it takes.




# Append or create a file:
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
