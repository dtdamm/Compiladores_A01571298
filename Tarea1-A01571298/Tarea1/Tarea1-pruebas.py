import importlib

tarea1 = importlib.import_module("Tarea1-docs")

Stack = tarea1.Stack
Queue = tarea1.Queue
Dict = tarea1.Dict

def test_stack_push_and_pop():
    """ Test adding and removing from stack to verify funtionality

    """
    s = Stack()
    for x in (1, 2, 3):
        s.push(x)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1

def test_stack_peek():
    """Verify returning viewing top of stack

    """
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert len(s) == 2

def test_stack_len_and_is_empty():
    """ Verify length fucntions correctly identify and track stacks length
    """
    s = Stack()
    assert s.is_empty()
    assert len(s) == 0
    s.push(1)
    s.push(2)
    assert not s.is_empty()
    assert len(s) == 2
    s.pop()
    s.pop()
    assert s.is_empty()
    assert len(s) == 0

def test_stack_pop_empty():
    """Verify stck cant pop when empty
    """
    s = Stack()
    try:
        s.pop()
        raise AssertionError("pop on empty stack should raise IndexError")
    except IndexError:
        pass

def test_stack_peek_empty():
    """Verify peek returns error when stack empty
    """
    s = Stack()
    try:
        s.peek()
        raise AssertionError("peek on empty stack should raise IndexError")
    except IndexError:
        pass

def test_stack_push_after_empty():
    """Verify popping correctly removes top and modifies size

    """
    s = Stack()
    s.push(1)
    s.pop()
    s.push(2)
    assert s.peek() == 2
    assert len(s) == 1

def test_queue_enqueue_and_dequeue():
    """Verify multiple enqueues and dequeues correctly returning prevo=ioulsy added values

    """
    q = Queue()
    for x in (1, 2, 3):
        q.enqueue(x)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

def test_queue_peek():
    """verify peek fucntions leaves queue intact and simply returns top of stack

    """
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    assert len(q) == 2

def test_queue_len_and_is_empty():
    """Verify size obtaining functions, that they correclty return queue size when empty and containing 1+ Nodes

    """
    q = Queue()
    assert q.is_empty()
    assert len(q) == 0
    q.enqueue(1)
    q.enqueue(2)
    assert not q.is_empty()
    assert len(q) == 2
    q.dequeue()
    q.dequeue()
    assert q.is_empty()
    assert len(q) == 0

def test_queue_dequeue_empty():
    """Verify dequeue doesnt work on empty queue

    """
    q = Queue()
    try:
        q.dequeue()
        raise AssertionError("dequeue on empty queue should raise IndexError")
    except IndexError:
        pass

def test_queue_peek_empty():
    """Verify empty returns error when stack has no nodes

    """
    q = Queue()
    try:
        q.peek()
        raise AssertionError("peek on empty queue should raise IndexError")
    except IndexError:
        pass

def test_queue_enqueue_after_empty():
    """Verify both enqueue and dequeue remove items and emptry recognizes

    """
    q = Queue()
    q.enqueue(1)
    q.dequeue()
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()

def test_dict_insert_and_get():
    """Test inserting new elements and retreiving them with get

    """
    d = Dict()
    for i in range(-25, 26):
        d[i] = i * 10
    assert len(d) == 51
    assert d[-7] == -70
    assert d[0] == 0


def test_dict_update():
    """test udpdating a key, in it smapped value and state

    """
    d = Dict()
    d[-7] = -70
    d[-7] = "updated"
    assert d[-7] == "updated"
    assert len(d) == 1


def test_dict_delete():
    """Make sure delte fucntion leaves no trace of key removed and updates size

    """
    d = Dict()
    d[-7] = -70
    d[3] = 30
    del d[-7]
    assert -7 not in d
    assert len(d) == 1


def test_dict_reinsert_after_delete():
    """Verify after deletion, insert handles tombstone slot and safely reinserts element

    """
    d = Dict()
    d[-7] = -70
    del d[-7]
    d[-7] = "back"
    assert d[-7] == "back"
    assert len(d) == 1


def test_dict_collisions():
    """Test collisions are handled correctly (since -1 and -2 give same hash) by making sure -2 got a different spot and didnt overwrite -1

    """
    c = Dict()
    c[-1], c[-2] = "a", "b"
    assert c[-1] == "a"
    assert c[-2] == "b"
    del c[-1]
    assert c[-2] == "b"
    assert -1 not in c


def test_dict_invalid_keys():
    """Verifiy invalid keys of multiple types get rejected when doing consult

    """
    d = Dict()
    for bad in (True, 1.5, "1", None):
        try:
            d[bad] = 1
            raise AssertionError(f"{bad!r} should be rejected")
        except TypeError:
            pass
        assert bad not in d


def test_dict_missing_key():
    """When looking up key that doesnt exist, get correctly returns non-existent

    """
    d = Dict()
    for op in (d.get, d.delete):
        try:
            op(42)
            raise AssertionError("missing key should raise KeyError")
        except KeyError:
            pass


if __name__ == "__main__":
    test_stack_push_and_pop()
    test_stack_peek()
    test_stack_len_and_is_empty()
    test_stack_pop_empty()
    test_stack_peek_empty()
    test_stack_push_after_empty()
    test_queue_enqueue_and_dequeue()
    test_queue_peek()
    test_queue_len_and_is_empty()
    test_queue_dequeue_empty()
    test_queue_peek_empty()
    test_queue_enqueue_after_empty()
    test_dict_insert_and_get()
    test_dict_update()
    test_dict_delete()
    test_dict_reinsert_after_delete()
    test_dict_collisions()
    test_dict_invalid_keys()
    test_dict_missing_key()
    print("Implementations work")