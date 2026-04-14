#Leetcode Question: 1103. Distribute Candies to People
#Interview Question: Given a certain number of candies and a certain number of people, distribute the candies in a specific way and return the final distribution.
def distributeCandies(candies, num_people):
        # Initialize result array with zeros for each person
        result = [0] * num_people
      
        # Track the current distribution round (also represents candies to give)
        distribution_round = 0

        current_person = 0
      
        # Continue distributing while there are candies remaining
        while candies > 0:
            # Calculate current person's index using modulo
            current_person = distribution_round % num_people
            print('current_person',current_person)
            # Give candies: either the required amount (distribution_round + 1) 
            # or all remaining candies, whichever is smaller
            candies_to_give = min(candies, distribution_round + 1)
            print('candies_to_give',candies_to_give)
            result[current_person] += candies_to_give
            print('result after giving',result)
            # Reduce the candy count by the amount given
            candies -= candies_to_give
            print('remaining candies',candies)
            # Move to next distribution round
            distribution_round += 1
            print('next distribution_round',distribution_round)
        print('final result',result)
        return result
distributeCandies(10,3)