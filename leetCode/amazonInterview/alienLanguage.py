# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# this one took some conversations with Gemini to figure out and get right lol

def lexi_order(words):
        flattened_chars = [char for string in words for char in string]
        all_chars = set(flattened_chars)
        adj_map = { c: set() for c in all_chars }
        in_degree = { c: 0 for c in all_chars }

        for i in range(len(words)-1):
            word1 = words[i] 
            word2 = words[i+1]
            for j in range(len(word1)):
                if j >= len(word2):
                    return ""
                if word1[j] != word2[j]:
                    if word2[j] not in adj_map[word1[j]]:
                        in_degree[word2[j]]+=1
                    adj_map[word1[j]].add(word2[j])
                    break

        khan_queue = []
        for char in in_degree.keys():
            if in_degree[char] == 0:
                khan_queue.append(char)
        result = []
        while khan_queue:
            current = khan_queue.pop()
            result.append(current)
            for connection in adj_map[current]:
                in_degree[connection]-=1
                if in_degree[connection] == 0:
                    khan_queue.append(connection)
        if len(result) < len(all_chars):
            return ""
        return "".join(result)


# below is me talking with copilot lol
# what is the complexity of this approach?
# Time: O(C) where C is the total number of characters in all words, since we process each character a constant number of times
# really O(C)? even with khan's algorithm? 
# yeah, because each character is added to the queue and removed from the queue at most once, and we also process each edge in the adjacency map at most once
# ok so its O(C + E) where E is the number of edges in the graph, but E is at most C^2 in the worst case, so we can say O(C) for simplicity
# Space: O(C) for the adjacency map and in-degree map

print(lexi_order(["wrt","wrf","er","ett","rftt"]))
