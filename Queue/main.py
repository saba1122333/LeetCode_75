# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# class RecentCounter:

#     def __init__(self):
#         self.times: list[int] = []

#     def ping(self, t: int) -> int:
#         while len(self.times) and self.times[0] < (t-3000):
#             self.times = self.times[1:]
#         return len(self.times)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".


# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = list(senate)
        while queue:
            sntr = queue.pop(0)
            i = 0
            while i < len(queue) and queue[i] == sntr:
                i += 1
            if i < len(queue):
                queue.pop(i)
                queue.append(sntr)
            else:
                return "Dire" if sntr == "D" else "Radiant"

