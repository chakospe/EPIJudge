from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections
from typing import Deque, Any

class QueueWithMax:
    def __init__(self) -> None:
        self._entries: Deque[Any] = collections.deque()
        self._candidates_for_max: Deque[Any] = collections.deque()

    def enqueue(self, x: int) -> None:
        self._entries.append(x)
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def dequeue(self) -> int:
        result = self._entries.popleft()
        if result == self._candidates_for_max[0]:
            self._candidates_for_max.popleft()
        return result

    def max(self) -> int:
        return self._candidates_for_max[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
