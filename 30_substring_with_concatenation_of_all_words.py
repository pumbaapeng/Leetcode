# key ideas
# 1) use |WL| scanning passes where WL is the (shared) word-length
# 2) maintain tables while scanning
#       a) required: #times a word is needed
#       c) found: #times a word is found in the current window
#       b) satisfied: # distinctive words such that found >= required
# pseudo algorith
#   for WL passes
#       for each pass: scan
#           for each stop
#               pop the str that "expires the window" while maintaining found and satisfied
#               if mismatch: clear found and satisfied
#               else: maintain found and satistied; if all satisfied, output
class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0: return []
        def reset(required):
            found = {k:0 for k in required}
            satisfied = 0
            return found, satisfied
        ret = []
        # init required
        required = {}
        for w in words:
            if not w in required: required[w] = 1
            else: required[w] += 1
        wl = len(words[0])
        for offset in xrange(wl):
            # init found and satisfied (make repeatable)
            found, satisfied = reset(required)
            for i_chunk in xrange((len(s) - offset) // wl):
                l = i_chunk * wl + offset
                # popped str
                l_pop = l - len(words) * wl
                popped_str = s[l_pop: (l_pop + wl)] if l_pop >= 0 else None
                if popped_str in required:
                    found[popped_str] -= 1
                    if found[popped_str] == required[popped_str] - 1:
                        satisfied -= 1
                # cur_str
                cur_str = s[l:l+wl]
                if cur_str in required:
                    found[cur_str] += 1
                    if found[cur_str] == required[cur_str]:
                        satisfied += 1
                        if satisfied == len(required):
                            ret.append(l_pop + wl)
        return ret
