import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class MyPriorityQueueTest {

    private MyPriorityQueue<Integer> priorityQueue;

    @BeforeEach
    public void setUp() {
        priorityQueue = new MyPriorityQueue<>(10);
    }

    @Test
    public void testConstructorAndIsEmpty() {
        assertTrue(priorityQueue.isEmpty());
    }

    @Test
    public void testOffer() {
        assertTrue(priorityQueue.offer(10));
        assertFalse(priorityQueue.isEmpty());
        assertThrows(NullPointerException.class, () -> priorityQueue.offer(null));
    }

    @Test
    public void testPoll() {
        assertNull(priorityQueue.poll());
        priorityQueue.offer(20);
        priorityQueue.offer(10);
        assertEquals(10, priorityQueue.poll());
        assertEquals(20, priorityQueue.poll());
        assertNull(priorityQueue.poll());
    }

    @Test
    public void testClear() {
        priorityQueue.offer(10);
        priorityQueue.offer(20);
        assertFalse(priorityQueue.isEmpty());
        priorityQueue.clear();
        assertTrue(priorityQueue.isEmpty());
    }

    @Test
    public void testPeek() {
        assertNull(priorityQueue.peek());
        priorityQueue.offer(20);
        priorityQueue.offer(10);
        assertEquals(10, priorityQueue.peek());
        assertFalse(priorityQueue.isEmpty());
    }

    @Test
    public void testBulkInsertAndRemove() {
        int numElements = 100;
        for (int j = 3; j < numElements; j++) {
            for (int i = 0; i < j; i++) {
                priorityQueue.offer(i);
            }
            assertFalse(priorityQueue.isEmpty());
            for (int i = 0; i < j; i++) {
                assertEquals(i, priorityQueue.poll());
            }
            assertTrue(priorityQueue.isEmpty());
        }
    }
}