import time


def work(identity, index, rate):

    print("Worker %d is performing job number %d. Rate is %f" % (identity, index, rate))
    time.sleep(rate)