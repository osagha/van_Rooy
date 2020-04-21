from DecisionProblem import DProblem, max_EU, info_proposition, entropy, info_prob

inits = {
    "default": {
        "prob": [1 / 3, 1 / 3, 1 / 3],
        "util": [
            [1.58, 0, 0],
            [0, 1.58, 0],
            [0, 0, 1.58]
        ]
    },
    "info-zeros": {
        "prob": [3 / 4, 3 / 16, 1 / 16],
        "util": [
            [info_proposition([0], [3 / 4, 3 / 16, 1 / 16]), 0, 0],
            [0, info_proposition([1], [3 / 4, 3 / 16, 1 / 16]), 0],
            [0, 0, info_proposition([2], [3 / 4, 3 / 16, 1 / 16])],
        ]
    },
    # "info-zeros":{
    #   "prob":[3/4, 1/4],
    #   "util":[
    #     [info([0], [3/4, 1/4]), 0],
    #     [0, info([1], [3/4, 1/4])]
    #   ]
    # },
    "info-penalty-col": {
        "prob": [3 / 4, 1 / 4],
        "util": [
            [info_proposition([0], [3 / 4, 1 / 4]), -info_proposition([1], [3 / 4, 1 / 4])],
            [-info_proposition([0], [3 / 4, 1 / 4]), info_proposition([1], [3 / 4, 1 / 4])]
        ]
    },
    "info-penalty-row": {
        "prob": [3 / 4, 1 / 4],
        "util": [
            [info_proposition([0], [3 / 4, 1 / 4]), -info_proposition([0], [3 / 4, 1 / 4])],
            [-info_proposition([1], [3 / 4, 1 / 4]), info_proposition([1], [3 / 4, 1 / 4])]
        ]
    },
    "entropy": {
        "prob": [3 / 4, 1 / 4],
        "util": [
            [entropy([[0]], [3 / 4, 1 / 4]), 0],
            [0, entropy([[1]], [3 / 4, 1 / 4])]
        ]
    }
}


def diagonal_constant_util(prob):
    utils = [[0 for _ in prob] for _ in prob]
    for i, x in enumerate(prob):
        utils[i][i] = 1
    return utils


def diagonal_info_util(prob):
    utils = [[0 for _ in prob] for _ in prob]
    for i, x in enumerate(prob):
        utils[i][i] = info_prob(prob[i])
    return utils


def diagonal_info_plus1_util(prob):
    utils = [[0 for _ in prob] for _ in prob]
    for i, x in enumerate(prob):
        utils[i][i] = info_prob(prob[i]) + 1
    return utils


def info_penalty_row_util(prob):
    utils = [[0 for _ in prob] for _ in prob]
    for i, x in enumerate(prob):
        for j, _ in enumerate(utils[i]):
            utils[i][j] = info_prob(prob[i]) if i == j else -info_prob(prob[i])
    return utils

def info_penalty_column_util(prob):
    utils = [[0 for _ in prob] for _ in prob]
    for i, x in enumerate(prob):
        for j, _ in enumerate(utils[i]):
            utils[i][j] = info_prob(prob[j]) if i == j else -info_prob(prob[j])
    return utils


def main():
    prob = [0.9, 0.09, 0.01]
    diagonal_constant = diagonal_constant_util(prob)
    diagonal_info = diagonal_info_util(prob)
    diagonal_info_plus1 = diagonal_info_plus1_util(prob)
    info_penalty_row = info_penalty_row_util(prob)
    info_penalty_column = info_penalty_column_util(prob)

    problem = DProblem({"prob": prob,
                        "util": diagonal_constant})
    print("Diagonal constant", problem.prob, problem.util)
    print("UV([0]) = ", problem.UV([0]))
    print("UV([1]) = ", problem.UV([1]))
    print("UV([2]) = ", problem.UV([2]))
    print("UV([0,1]) = ", problem.UV([0, 1]))
    print("UV([0,2]) = ", problem.UV([0, 2]))
    print("UV([1,2]) = ", problem.UV([1, 2]))
    print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    print("max_EU = ", max_EU(problem.prob, problem.util))
    print()

    problem = DProblem({"prob": prob,
                        "util": diagonal_info})
    print("Diagonal info", problem.prob, problem.util)
    print("UV([0]) = ", problem.UV([0]))
    print("UV([1]) = ", problem.UV([1]))
    print("UV([2]) = ", problem.UV([2]))
    print("UV([0,1]) = ", problem.UV([0, 1]))
    print("UV([0,2]) = ", problem.UV([0, 2]))
    print("UV([1,2]) = ", problem.UV([1, 2]))
    print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    print("max_EU = ", max_EU(problem.prob, problem.util))
    print()


    problem = DProblem({"prob": prob,
                        "util": diagonal_info_plus1})
    print("Diagonal info plus1", problem.prob, problem.util)
    print("UV([0]) = ", problem.UV([0]))
    print("UV([1]) = ", problem.UV([1]))
    print("UV([2]) = ", problem.UV([2]))
    print("UV([0,1]) = ", problem.UV([0, 1]))
    print("UV([0,2]) = ", problem.UV([0, 2]))
    print("UV([1,2]) = ", problem.UV([1, 2]))
    print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    print("max_EU = ", max_EU(problem.prob, problem.util))
    print()

    prob = [0.75, 0.25]
    diagonal_info_plus1 = diagonal_info_plus1_util(prob)
    problem = DProblem({"prob": prob,
                    "util": diagonal_info_plus1})
    print("Diagonal info plus1", problem.prob, problem.util)
    print("UV([0]) = ", problem.UV([0]))
    print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("UV([0,2]) = ", problem.UV([0, 2]))
    # print("UV([1,2]) = ", problem.UV([1, 2]))
    # print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    print("max_EU = ", max_EU(problem.prob, problem.util))
    print()


    prob = [0.4, 0.3, 0.3]
    diagonal_info_plus1 = diagonal_info_plus1_util(prob)
    problem = DProblem({"prob": prob,
                    "util": diagonal_info_plus1})
    print("Diagonal info plus1", problem.prob, problem.util)
    print("UV([0]) = ", problem.UV([0]))
    print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("UV([0,2]) = ", problem.UV([0, 2]))
    # print("UV([1,2]) = ", problem.UV([1, 2]))
    # print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    print("max_EU = ", max_EU(problem.prob, problem.util))
    print()

    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_column})
    # print("Info penalty column", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("UV([0,2]) = ", problem.UV([0, 2]))
    # print("UV([1,2]) = ", problem.UV([1, 2]))
    # print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()

    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("UV([0,2]) = ", problem.UV([0, 2]))
    # print("UV([1,2]) = ", problem.UV([1, 2]))
    # print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()


    # prob = [0.75, 0.25]
    # info_penalty_row = info_penalty_row_util(prob)
    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()

    # prob = [0.75, 0.20, 0.05]
    # info_penalty_row = info_penalty_row_util(prob)
    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("UV([0,2]) = ", problem.UV([0, 2]))
    # print("UV([1,2]) = ", problem.UV([1, 2]))
    # print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()


    # prob = [0.4, 0.3, 0.3]
    # info_penalty_row = info_penalty_row_util(prob)
    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("UV([0,2]) = ", problem.UV([0, 2]))
    # print("UV([1,2]) = ", problem.UV([1, 2]))
    # print("UV([1,2,3]) = ", problem.UV([0, 1, 2]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()

    # # When there are two alternatives and P_dist = {p, 1-p}, and util = info_penalty_row(P_dist), then
    # # max_EU    = p * -log_2(p) + (1-p) * log_2(p)
    # #           = log_2(p) * (1-2p)
    # prob = [0.9, 0.1]
    # info_penalty_row = info_penalty_row_util(prob)
    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()

    # prob = [0.99, 0.01]
    # info_penalty_row = info_penalty_row_util(prob)
    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()

    # prob = [0.51, 0.49]
    # info_penalty_row = info_penalty_row_util(prob)
    # problem = DProblem({"prob": prob,
    #                     "util": info_penalty_row})
    # print("Info penalty row", problem.prob, problem.util)
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([0,1]) = ", problem.UV([0, 1]))
    # print("max_EU = ", max_EU(problem.prob, problem.util))
    # print()

    # problem = DProblem(inits["default"])
    # print()
    # print("UV([0]) = ", problem.UV([0]))
    # print("UV([1]) = ", problem.UV([1]))
    # print("UV([2]) = ", problem.UV([2]))
    # print("UV([0,1]) = ", problem.UV([0,1]))
    # print("UV([1,2]) = ", problem.UV([1,2]))
    # print("UV([1,2,3]) = ", problem.UV([0,1,2]))

    # problem = DProblem(inits["info-zeros"])
    # print("max_EU", max_EU(problem.prob, problem.util))
    # print("UV([0,1])", problem.UV([0,1]))


if __name__ == "__main__":
    main()
