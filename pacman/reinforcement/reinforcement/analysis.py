# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    """
    Noise refers to how often an agent ends up in an unintended successor state,
    when they perform an action.
    So we make Noise as 0 assuming agent always takes intended successor state.
    Considering ideal case where discount is 1 and noise is 0. Since we need to change only one value
    changed noise value to 0.
    """
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise


def question3a():
    # q: Prefer the close exit (+1), risking the cliff (-10)
    # Ideally kept noise as 0 to maximize the output. started at 0.1 discount factor.
    # Two steps to reach +1 exit. East East and North.
    # Works for discount factor 0.1 and living reward 0.8.
    # Also Works for discount factor 0.2 and living reward 0.4.
    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = 0.8
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3b():
    # Prefer the close exit (+1), but avoiding the cliff (-10)
    # Assuming there is no living reward, Movement is assumed certain.
    # works for discount 0.1/0.2/0.3 and noise 0.1/0.2/0.3 and reward 0

    answerDiscount = 0.3
    answerNoise = 0.1
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3c():
    # Prefer the distant exit (+10), risking the cliff (-10)
    #  works for following values.
    # 0.9/0.8/0.7/0.6/0.5/0.4 0 0
    # 0.9/0.8/0.7/0.6/0.5/0.4 0 0.1-0.9

    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0.9
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3d():
    # Prefer the distant exit (+10), avoiding the cliff (-10)
    #  works for following values
    # 0.1-0.9 0.1 0.1-0.9
    # I choose 0.9 discount factor as the higher the discount factor,
    # the farther our rewards will propagate through time.
    # 0.1 as lesser noise is preferrable and 0.9 as more reward is preferrable.
    # True that more living reward might make agent lazy and less greedy, we can choose 0.1 as well.
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = 0.9
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3e():
    #  Avoid both exits and the cliff (so an episode should never terminate)
    # works for following values
    # 0.7-1/0.1 0.6-1 0.1-1
    # 0/1 0/1 0/1
    answerDiscount = 1
    answerNoise = 1
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question6():
    # Tried different variations for epsilon(0-1) and learning rate(0-1)..could not land at correct output.
    # Not exactly sure why.. but recalling epsilon-greedy concepts,
    # assume that too less or too high epsilon does not serve the purpose. If high epsilon, though we learn we keep
    # making bad decisions. If epsilon is too low, we don't explore much we don't learn much.
    # so better way is to reduce epsilon over time and decreasing randomness leading to optimal learning.
    # answerEpsilon = 'Not Possible'
    # answerLearningRate = 'Not Possible'
    # return answerEpsilon, answerLearningRate
    return 'NOT POSSIBLE'


if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis

    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
