""" This file is a collection of plotting functions that will be repeatedly used in analysis

Created by: Amanda LeBel
Spring Rotation Project 2021
"""
import matplotlib.pyplot as plt



def iterations_x_accuracy(correct, correct_sem):
    """ This function plots the accuracy for increasing iterations of a stimulus seperately for each set size.

    args:

    correct (dict): The keys for this dict should be the setsize (range 2-7). The values should be lists with the average accuracy
        across iterations
    correct_sem (dict): same as correct but sem instead of mean.
    """
    plt.figure()
    ax = plt.subplot(111)

    for i in range(2, 7):
        plt.plot(list(range(1, 15)), all_set[i], label=str(i))
        plt.fill_between(list(range(1, 15)), [i-j for i, j in zip(correct)[i], correct_sem[i])], [i+j for i, j in zip(correct[i], correct_sem[i])], alpha=0.3)

    for y in range(30, 100, 10):
         plt.plot([0, 8, 14, 15], [y/100]*4, '--', lw=0.5, color='dimgray', alpha=0.3)

    plt.legend()
    plt.xlabel('iterations')
    plt.ylabel('p (corr)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
def setsize_x_accuracy(correct, correct_sem):
    """ This function plots the accuracy as a function of set size.

    args:

    correct (array): This should be an array of shape (7,) with each value the mean for that set size
    correct_sem (array): Same as correct but with sem
    """
    plt.figure()
    ax = plt.subplot(111)

    plt.plot(list(range(2, 7)), correct)
    plt.fill_between(list(range(2, 7)), [i-j for i, j in zip(correct, correct_sem)], [i+j for i, j in zip(correct, correct_sem)], alpha=0.3)

    for y in range(50, 100, 10):
         plt.plot([2, 3, 5, 6], [y/100]*4, '--', lw=0.5, color='dimgray', alpha=0.3)

    plt.xlabel('set size')
    plt.ylabel('p (corr)')
    plt.xticks([2, 3, 4, 5, 6])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
