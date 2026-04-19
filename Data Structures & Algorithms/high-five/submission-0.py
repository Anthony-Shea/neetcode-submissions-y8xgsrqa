class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        K = 5
        all_scores = defaultdict(list)

        for item in items:
            student_id = item[0]
            score = item[1]
            heapq.heappush_max(all_scores[student_id], score)
        solution = []
        for student_id in sorted(all_scores.keys()):
            total = 0
            for i in range(K):
                total += heapq.heappop_max(all_scores[student_id])
            solution.append([student_id, total //K])
        return solution