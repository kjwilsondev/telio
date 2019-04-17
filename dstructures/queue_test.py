#!python

from queue import Queue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Queue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Queue()
        assert q.length() == 0
        q.enqueue('A')
        assert q.length() == 1
        q.enqueue('B')
        assert q.length() == 2
        q.dequeue()
        assert q.length() == 1
        q.dequeue()
        assert q.length() == 0

    def test_enqueue(self):
        q = Queue()
        q.enqueue('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.enqueue('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = Queue()
        assert q.front() is None
        q.enqueue('A')
        assert q.front() == 'A'
        q.enqueue('B')
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = Queue(['A', 'B', 'C'])
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()

    def test_push_front(self):
        q = Queue()
        q.push_front('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.push_front('B')
        assert q.front() == 'B'
        assert q.length() == 2
        q.push_front('C')
        assert q.front() == 'C'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_push_back(self):
        q = Queue()
        q.push_back('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.push_back('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.push_back('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_pop_front(self):
        q = Queue(['A', 'B', 'C'])
        assert q.pop_front() == 'A'
        assert q.length() == 2
        assert q.pop_front() == 'B'
        assert q.length() == 1
        assert q.pop_front() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.pop_front()
    
    def test_pop_back(self):
        q = Queue(['A', 'B', 'C'])
        assert q.pop_back() == 'C'
        assert q.length() == 2
        assert q.pop_back() == 'B'
        assert q.length() == 1
        assert q.pop_back() == 'A'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.pop_back()


if __name__ == '__main__':
    unittest.main()