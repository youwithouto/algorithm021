import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        result = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    result.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            nextWord = word[:i] + c + word[i + 1:]
                            if nextWord in wordSet:
                                newLayer[nextWord] += [j + [nextWord]
                                                       for j in layer[word]]
            wordSet -= set(newLayer.keys())
            layer = newLayer
        return result
