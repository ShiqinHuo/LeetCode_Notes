class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return False
        visited = {}
        visited[0] = True
        stack = []
        stack.append(0)
        while stack:
            curr = stack.pop()
            # each key in a room, append in stack if not visited
            for i in rooms[curr]:
                if i not in visited:
                    visited[i] = True
                    stack.append(i)
        return len(visited) == len(rooms)