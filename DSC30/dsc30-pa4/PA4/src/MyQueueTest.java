import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MyQueueTest {
    @Test
    void QueueTest1(){
        MyQueue<String> queue = new MyQueue<>();
        assertEquals(0, queue.size());
        assertEquals(true, queue.isEmpty());
        assertThrows(IllegalArgumentException.class, () -> {
            queue.enqueue(null);
        });
        queue.enqueue("Java");
        assertEquals("Java", queue.peek());
        queue.enqueue("Python");
        queue.enqueue("C#");
        queue.enqueue("Lua");
        assertEquals("[Java -> Python -> C# -> Lua]", queue.toString());
        assertEquals("Java", queue.peek());
        assertEquals("Java", queue.dequeue());
        assertEquals("[Python -> C# -> Lua]", queue.toString());
    }

    @Test
    void QueueTest2(){
        MyQueue<Integer> queue = new MyQueue<>();
        queue.enqueue(72);
        queue.enqueue(35);
        assertEquals(72, queue.peek());
        queue.enqueue(96);
        queue.enqueue(48);
        assertEquals("[72 -> 35 -> 96 -> 48]", queue.toString());
        assertEquals(72, queue.dequeue());
        queue.enqueue(72);
        assertEquals(false, queue.isEmpty());
        assertEquals(4, queue.size());
        assertEquals("[35 -> 96 -> 48 -> 72]", queue.toString());
    }

    @Test
    void QueueTest3(){
        MyQueue<Character> queue = new MyQueue<>();
        queue.enqueue('A');
        assertEquals(false, queue.isEmpty());
        assertEquals(1, queue.size());
        assertEquals("[A]", queue.toString());
        assertEquals('A', queue.dequeue());
        assertEquals(0, queue.size());
        assertEquals(true, queue.isEmpty());
        assertEquals(null, queue.peek());
        assertEquals(null, queue.dequeue());
        assertEquals("[]", queue.toString());
    }
}
