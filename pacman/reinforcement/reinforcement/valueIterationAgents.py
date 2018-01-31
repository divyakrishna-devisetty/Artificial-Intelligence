# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        for _ in range(self.iterations):
            temp_values = util.Counter()

            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    continue

                actions = self.mdp.getPossibleActions(state)
                value = [self.getQValue(state, action) for action in actions]
                temp_values[state] = max(value) if value else 0

            self.values = temp_values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        # Q*(s,a) = sum over next states(T(s,a,s')[R(s,a,s')+gammaV*(s')])
        # for each of next states (s') for current state s and action a we calculate Q values
        # V*(s')--> value of next state, T(s,a,s') --> transition probability
        #  R(s,a,s') --> reward we achieve by taking that action and going to s'
        # gamma is discount factor

        q_value = 0
        # Iterate through all possible outcomes for a given state and action
        for next_state, transition_prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, next_state)
            future_reward = self.discount * self.values[next_state]
            q_value += transition_prob * (reward + future_reward)

        return q_value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        # pi*(state) = argmax over actions (Q*(state,action))
        # Choosing the best action for given state computed from q-values
        if self.mdp.isTerminal(state):
            return None
        policy = util.Counter()
        for action in self.mdp.getPossibleActions(state):
            policy[action] = self.computeQValueFromValues(state, action)

        return policy.argMax()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
