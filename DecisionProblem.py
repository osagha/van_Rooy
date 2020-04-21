import numpy as np

class DProblem:
  def __init__(self, init_dict):
    # self.prob: list of numbers 
    # prior probability of each world
    # worlds are the indices of self.prob
    self.prob = init_dict["prob"]
    # self.util: list of lists of numbers
    # actions are the indices
    # self.util[a][w] is the utility of a in w
    self.util = init_dict["util"]
    self.num_worlds = len(self.prob)
    self.num_actions = len(self.util)
    for action in self.util:
      assert len(action) == self.num_worlds

  def UV(self, q):
      """
      See definition on p. 391 of van Rooy (2004)
      UV(q)   :=  UV(learn q, choose later) - UV(learn q, choose a*)
                =  max_i EU(a_i, q) - EU(a_star, q)
      actually, a_star may not be uniquely defined, so we update the definition when a_star is a set:
                =  max_i EU(a_i, q) - 1/|a_star| sum_j (EU(a_star_j, q))
      """
      new_prob = condition(self.prob, q)
      best_actions, maximum = max_EU(self.prob, self.util)
      best_action_utils = [EU(new_prob, self.util[action_index]) for action_index in best_actions]
      uv_now = sum(best_action_utils) / len(best_action_utils)    # (use old winner, calculate new EU)
      new_a, uv_later = max_EU(new_prob, self.util)    # (compute new max_EU based on q)
      return uv_later - uv_now

  def UV_lift(self, q_prime, alts): # broken, ignore for now
  """p. 394 bottom"""
    prob = self.prob
    util = self.util
    new_prob = condition(prob, q_prime)
    probabilities = [ probability(q, new_prob) for q in alts ]
    print("probabilities", probabilities)
    # a_star is the old winner
    best_actions, maximum = max_EU(prob, util)
    best_action_utils = [ EU(new_prob, util[action_index]) for action_index in best_actions ]
    print("best_action_utils", best_action_utils)
    summands = []
    for q in alts:
      term = 0
      prob_cond_q = condition(prob, q)
      prob_cond_q_prime = condition(prob, q_prime)
      new_winner, new_maxEU = max_EU(prob_cond_q, util)
      old_maxEU = sum(best_action_utils)/len(best_action_utils)
      term = probability(q, prob_cond_q_prime) * (new_maxEU - old_maxEU)
      summands.append(term)
    # print("uv_later", uv_later)
    # print("uv_now", uv_now)
    return sum(summands)

  # def EUV_lift(self, alts_prime)
	
  def EUV(self, alts_prime, alts):
    prob = self.prob
    probabilities = [ probability(q, prob) for q in alts ]
    uvs = [ self.UV(q, alts) for q in alts_prime ]
    return sum([ a*b for (a,b) in zip(probabilities, uvs) ])

  def IV(self, alts, q):
    old_entropy = entropy(alts, self.prob)
    new_entropy = entropy(alts, self.learn(q))
    return old_entropy - new_entropy

  def EIV(self, alts_prime, alts):
    prob = self.prob
    probabilities = [ probability(q, prob) for q in alts ]
    ivs = [ IV(alts_prime, q) for q in alts  ]
    return sum([ a*b for (a,b) in zip(probabilities, ivs) ])



# maybe abs(IV) is relevance?
# which utility: maybe IV?
# off-diagonal utilities?
# check out Parikh
# reach out to van Rooy
# schedule meeting with Craige

"""
	Helper functions:
		entropy: entropy of a set of propositions
		probability: probability of a proposition
		EU: expected utility of an action
		max_EU: returns EU maximizer given a full decision problem
		normalize: rescale probabilities to sum to 1
"""

def condition(prob, proposition):
  # q is a list of indices
  new_prob = prob.copy()
  for w in range(len(prob)):
    if w not in proposition:
      new_prob[w] = 0
  return normalize(new_prob)

def probability(q, prob):
  true = prob.copy()
  for w in range(len(prob)):
    if w not in q:
      true[w] = 0
  return sum(true)

def info_proposition(q, p_dist):
    return -np.log2(probability(q, p_dist))

def info_prob(p):
    return -np.log2(p)

def entropy(alts, prob):
    probabilities = [ probability(q, prob) for q in alts ]
    log_probs = [ info_proposition(q, prob) for q in alts ]
    return sum([ a*b for (a,b) in zip(probabilities, log_probs) ])


def EU(prob, a_util):
  return sum([ a*b for (a,b) in zip(a_util, prob) ])
	
def max_EU(prob, util):
  expected_utils = []
  for util_at_a in util:
    expected_utils.append(EU(util_at_a, prob))
  print("expected_utils", expected_utils)
  maximum = max(expected_utils)
  best_actions = []
  for index, action_util in enumerate(expected_utils):
    if action_util == maximum:
      best_actions.append(index)
  return best_actions, maximum
	
def normalize(prob):
  denominator = sum(prob)
  return [ p/denominator for p in prob ]