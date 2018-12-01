import random
import os
import bruteforce as bruteforce
import bottomup as bottomup
import topdown as topdown
import utils as utils

def main():
    runExperiments()
    # runExperiments2()

#############################################
# EXPERIMENTS
# Generate random data.
# 1 - Fixed n, varried W:
def runExperiments():
    print("=> Running Experiments: Fixed n, varried W")
    nList=[5,10,14,15,20]
    start=10; end=1000; #range of numbers in weight and value arrays
    wList = [10,20,30,40,50,100,200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000]

    print("=======================================")
    # EXP with all 3 mthods:
    for n in nList:
        Weights = utils.generateData(n, start, end)
        Values = utils.generateData(n, start, end)
        print("All:n=",n)
        # for each n, run thru varied W in wList:
        for i in range(len(wList)):
            W = wList[i]
            bf_runtime = 0;bu_runtime = 0;td_runtime = 0
            for k in range(10):
                bf = bruteforce.knapsack_brute_force(Weights, Values, W);
                bu = bottomup.knapsack_bottom_up_dp(Weights, Values, W);
                td = topdown.knapsack_top_down_dp(Weights, Values, W);
                bf_runtime = bf_runtime + bf[1]
                bu_runtime = bu_runtime + bu[1]
                td_runtime = td_runtime + td[1]

            bf_runtime = bf_runtime/10
            bu_runtime = bu_runtime/10
            td_runtime = td_runtime/10

            # data[capacity, n, bruteforce time, bottom up time, topdown time]
            fileName = "experiments/all_n_varried_W.csv"
            data = [str(W), str(n), "%.3f"%bf_runtime, "%.3f"%bu_runtime, "%.3f"%td_runtime]
            writeToFile(fileName, data) # recording the time it takes.

    # EXP: w/  bottom up vs top down, can increase n since no bruteforce
    nList=[100,200,400,500]
    # for each n, run thru varied W in wList:
    for n in nList:
        Weights = utils.generateData(n, start, end)
        Values = utils.generateData(n, start, end)
        print("BUTD:n=",n)
        for i in range(len(wList)):
            W = wList[i]
            bf_runtime = 0;bu_runtime = 0;td_runtime = 0
            #run each method for 10 times and then take average
            for k in range(10):
                bu = bottomup.knapsack_bottom_up_dp(Weights, Values, W);
                td = topdown.knapsack_top_down_dp(Weights, Values, W);
                bu_runtime = bu_runtime + bu[1]
                td_runtime = td_runtime + td[1]

            bu_runtime = bu_runtime/10
            td_runtime = td_runtime/10

            # data[capacity, n, bruteforce time, bottom up time, topdown time]
            fileName = "experiments/dp_n_varried_W.csv"
            data = [str(W), str(n), "%.3f"%0.0, "%.3f"%bu_runtime, "%.3f"%td_runtime]
            writeToFile(fileName, data) # recording all data in csv.

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
