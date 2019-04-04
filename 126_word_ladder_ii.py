from collections import deque

class Solution:
    def cal_dist(self, w1, w2):
        assert(len(w1) == len(w2))
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        return diff

    def make_adj_list(self, beginWord, wordList):
        words = {w for w in wordList}
        words.add(beginWord)
        adj = {}

        for w in words:
            adj[w] = set()
            for i in range(len(w)):
                c = w[i]
                for j in range(ord('a'), ord('z')+1):
                    rep = chr(j)
                    repWord = w[:i] + rep + w[i+1: len(w)]
                    if rep != c and repWord in words:
                        adj[w].add(repWord)
        return adj

    def bfs_label_distance(self, beginWord, endWord, adj):
        q = deque()
        used = set()
        dist_map = {}
        q.append((beginWord, 0))
        used.add(beginWord)
        while len(q) != 0:
            w, lv = q.popleft()
            dist_map[w] = lv
            if w == endWord:
                return dist_map
            for neighbor in adj[w]:
                if neighbor not in used:
                    q.append((neighbor, lv + 1))
                    used.add(neighbor)
        return dist_map


    def dfs_enum_paths(self, beginWord, end_word, dist_map, adj):
        ret = []
        self.recur(beginWord, set(), [], end_word, ret, dist_map, adj)
        return ret

    def recur(self, cur_word, used, mem, end_word, ret, dist_map, adj):
        mem.append(cur_word)
        used.add(cur_word)
        if mem[-1] == end_word:
            ret.append(mem[:])
        else:
            for word in adj[cur_word]:
                if word in used or word not in dist_map or dist_map[word] != len(mem):
                    continue
                self.recur(word, used, mem, end_word, ret, dist_map, adj)
        used.remove(cur_word)
        mem.pop()
        return

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        adj = self.make_adj_list(beginWord, wordList)
        dist_map = self.bfs_label_distance(beginWord, endWord, adj)
        ret = self.dfs_enum_paths(beginWord, endWord, dist_map, adj)
        return ret

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
