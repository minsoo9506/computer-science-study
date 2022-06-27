# https://leetcode.com/problems/reconstruct-itinerary

import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = collections.defaultdict(list)
        for a, b in sorted(tickets):
            ticket_dict[a].append(b)

        result = []

        def dfs(x):
            while ticket_dict[x]:
                dfs(ticket_dict[x].pop(0))
            result.append(x)

        dfs("JFK")

        return result[::-1]
