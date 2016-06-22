import heapq


class PriorityQueue:
    def __init__(self, pq=None):
        if not pq:
            self.pq = []
        else:
            self.pq = pq
            heapq.heapify(self.pq)

    def del_min(self):
        return heapq.heappop(self.pq)

    def decrease_key(self, vtx_id, value):
        pos = self.get_pos(vtx_id)
        if not pos:
            return
        if self.pq[pos][0] < value:
            # invalid operation
            return
        self.pq[pos] = [value, vtx_id]
        self.perc_up(pos)

    def perc_up(self, pos):
        while pos > 0:
            if self.pq[pos//2][0] > self.pq[pos][0]:
                temp = self.pq[pos//2]
                self.pq[pos//2] = self.pq[pos]
                self.pq[pos] = temp
                pos //= 2
            else:
                break

    def increase_key(self):
        # todo
        pass

    def per_down(self):
        # todo
        pass

    def get_pos(self, vtx_id):
        if self.is_empty():
            return None
        from collections import deque
        q = deque()
        q.append(0)
        while q:
            pos = q.popleft()
            if self.pq[pos][1] == vtx_id:
                return pos
            if 2*pos+1 < len(self.pq):
                q.append(2*pos+1)
            if 2*pos+2 < len(self.pq):
                q.append(2*pos+2)
        return None

    def is_empty(self):
        if not self.pq:
            return True
        else:
            return False

    def has_vertex(self, vtx_id):
        pos = self.get_pos(vtx_id)
        if not pos:
            return False
        else:
            return True

    def get_heap(self):
        return self.pq


