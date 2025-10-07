class HeapItem:
    # custom heap solution
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __lt__(self, to_compare) -> bool:
        if self.count == to_compare.count:
            return self.word > to_compare.word  # for lexicographical order
        return self.count < to_compare.count


class Solution:
    # T: O(n*log(k)) # n words, k is size of heap
    # S: O(n) + O(n) => O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)
        heap = []

        for word, count in word_counts.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)

        res = []
        while k:
            cur = heapq.heappop(heap)
            res.append(cur.word)
            k -= 1

        return list(reversed(res))

        # Because heapq pops the smallest item first. (minHeap)
        # Your comparator defines “smaller” = lower count (or, on ties, lexicographically larger word)
        # So when you pop all k items you get them from worst → best: (count ↑, word ↓)
        # Reversing flips it to the required order: most frequent first, and for ties lexicographically smaller first.
