
from copy import deepcopy

class Solution:
    # def stoneGameII(self, piles: List[int]) -> int:
    def stoneGameII(self, piles):
        # idea is to traverse every possible situation in the game and find the most optimum solution
        # the optimum move for each player is determined by taking the difference between current player and the other player
        # this is a recursive problem

        num_players = 2

        def traverse(piles, seen_results, prefix_sum, ii, X, M, scores, turn):
            '''
            Args:
                piles (list[int]): list of piles of stones
                prefix_sum (list[int]): prefix sum of piles
                ii (int): current position
                X (int): number of piles to take
                M (int): value to calculate how many piles can be taken
                scores (list[int]): scores of players
                turn (int): 0 - for Alice, 1 for Bob
            '''
            # print(f'seen_results: {seen_results}')

            # if seen_results.get((turn, (max(ii, len(prefix_sum)-1), max(ii+X, len(prefix_sum)-1))), None) is not None:
            #     s = seen_results[(turn, (ii, ii+X))]
            #     return [s[ii] + scores[ii] for ii in range(num_players)]

            # print()
            # print(f'ii: {ii} X: {X} M: {M}')
            # print(f'prefix_sum: {prefix_sum}')
            # print(f'start: {ii} end: {ii+X}')
            # print(f'scores: {scores} turn: {turn}')

            # if seen_results.get((turn, M, ii+1, ), None) is not None:
            #     s = seen_results[(turn, M, ii+1)]
            #     return [s[jj] + scores[jj] for jj in range(num_players)]

            if seen_results.get((turn, M, ii, ii+X), None) is not None:
                s = seen_results[(turn, M, ii, ii+X)]
                return [s[jj] + scores[jj] for jj in range(num_players)]

            # print()
            # print(f'ii: {ii} X: {X} M: {M}')
            # print(f'prefix_sum: {prefix_sum}')
            # print(f'start: {ii} end: {ii+X}')
            # print(f'scores: {scores} turn: {turn}')

            if ii + X >= len(prefix_sum) - 1:
                # piles finished
                # print(f'prefix_sum.i: {prefix_sum[ii]} {prefix_sum[-1]}')
                # print('finished')
                # print(f'ii: {ii} X: {X} ii+X: {ii+X} n: {len(prefix_sum)}')
                scores[turn] += prefix_sum[-1] - prefix_sum[ii]
                # s = [0, 0]
                # s[turn] += prefix_sum[-1] - prefix_sum[ii]
                # seen_results[(turn, M, ii+1)] = deepcopy(s)
                # seen_results[(turn, M, ii, ii+X)] = deepcopy(s)
                return scores
            else:
                # print(f'prefix_sum.i: {prefix_sum[ii]} {prefix_sum[ii+X]}')
                possible_scores = []
                scored_values = []

                scores[turn] = scores[turn] + (prefix_sum[ii+X] - prefix_sum[ii])
                # print('values for x: ', list(range(1, 2*M+1)))
                # print(f'scores before: {scores}')
                next_turn = (turn+1)%num_players

                for x in range(1, 2*M + 1):
                    if ii + X + x >= len(prefix_sum):
                        break
                    # print(f'ii: {ii} X: {X} x: {x} ii+X+x: {ii+X+x}')
                    # print(f'ii+X: {ii+X} x: {x} max(x, M)')
                    # scored_value = traverse(piles, prefix_sum, ii + X, x, max(x, M), scores, next_turn)
                    # current_scores, scored_value = traverse(piles, prefix_sum, ii + X, x, max(x, M), deepcopy(scores), next_turn)
                    current_scores = traverse(piles, seen_results, prefix_sum, ii + X, x, max(x, M), deepcopy(scores), next_turn)
                    # print(f'scored_value: {scored_value}')
                    # scored_values.append(scored_value)
                    possible_scores.append(current_scores)

                # print('afterafter')
                # print(f'ii: {ii} X: {X} M: {M}')
                # print(f'prefix_sum: {prefix_sum}')
                # print(f'piles: {piles} taken piles: {piles[ii:ii+X]}')
                # print(f'start: {ii} end: {ii+X}')
                # print(f'scores: {scores} turn: {turn}')
                # print(f'scored_values: {scored_values}')
                # print(f'scores after: {scores}')
                # print(f'possible_scores: {possible_scores}')
                    
                idx_max = max(range(len(possible_scores)), key=lambda x: possible_scores[x][next_turn])
                # print(f'idx_max: {idx_max}')
                # seen_results[(turn, (ii, ii+X))] = [possible_scores[idx_max][ii] - scores[ii] for ii in range(num_players)]
                # seen_results[(turn, (ii, ii+X))][turn] += prefix_sum[ii+X] - prefix_sum[ii]
                # seen_results[(next_turn, M, ii+X+1)] = [possible_scores[idx_max][ii] - scores[ii] for ii in range(num_players)]
                seen_results[(next_turn, M, ii, ii+X)] = [possible_scores[idx_max][ii] - scores[ii] for ii in range(num_players)]

                return possible_scores[idx_max]

        prefix_sum = [0]
        seen_results = dict()  # player, (ii, ii+X)
        s = 0
        current_player = 0
        current_player = num_players - 1

        for x in piles:
            s += x
            prefix_sum.append(s)

        scores = traverse(piles, seen_results, prefix_sum, 0, 0, 1, [0, 0], current_player)
        # print(scores)
        # print(seen_results)

        return scores[0]

        # possible_scores = []

        # possible_scores.append(traverse(piles, prefix_sum, 0, 1, 1, [0, 0], current_player))
        # possible_scores.append(traverse(piles, prefix_sum, 0, 2, 1, [0, 0], current_player))

        # idx_max = max(range(len(possible_scores)), key=lambda x: possible_scores[x][current_player])
        # print(possible_scores)
        # return possible_scores[idx_max][current_player]
        


if __name__ == "__main__":
    piles = [2,7,9,4,4]
    Output = 10

    piles = [1,2,3,4,5,100]
    Output = 104
    
    # piles = [1,1,1]
    Output = 2

    piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729,7084,8407]
    Output = 98008

    # piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729]
    # Output = 93650

    # piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511]
    # Output = 76946

    # piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065]
    # Output = 84319

    # piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063]
    # Output = 87735

    # piles = [1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7063]
    # Output = 16

    piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 7000]
    Output = 6


    sol = Solution()
    print(sol.stoneGameII(piles))
