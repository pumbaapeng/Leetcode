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
                return lv + 1 
            for neighbor in adj[w]:
                if neighbor not in used:
                    q.append((neighbor, lv + 1)) 
                    used.add(neighbor)
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        adj = self.make_adj_list(beginWord, wordList)
        return self.bfs_label_distance(beginWord, endWord, adj)
