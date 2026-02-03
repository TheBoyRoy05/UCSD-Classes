import org.junit.jupiter.api.Test;
import java.util.NoSuchElementException;
import static org.junit.jupiter.api.Assertions.*;

class CharQueueTest {
    @Test
    void queueTest1(){
        CharQueue charQueue = new CharQueue();
        charQueue.enqueue('J');
        charQueue.enqueue('A');
        charQueue.enqueue('V');
        charQueue.enqueue('A');
        charQueue.enqueue(' ');
        charQueue.enqueue('I');
        charQueue.enqueue('S');
        charQueue.enqueue(' ');
        CharQueue myQueue = new CharQueue(1);
        assertEquals(true, myQueue.isEmpty());
        myQueue.enqueue('C');
        myQueue.enqueue('O');
        myQueue.enqueue('O');
        myQueue.enqueue('L');
        assertEquals(false, charQueue.isEmpty());
        assertEquals(false, myQueue.isEmpty());
        assertEquals(8, charQueue.size());
        assertEquals(4, myQueue.size());
        assertEquals('J', charQueue.peek());
        assertEquals('J', charQueue.dequeue());
        charQueue.clear();
        assertEquals(true, charQueue.isEmpty());
        assertThrows(NoSuchElementException.class, () -> {
            charQueue.dequeue();
        });
    }

    @Test
    void queueTest2(){
        CharQueue charQueue = new CharQueue();
        assertEquals(true, charQueue.isEmpty());
        charQueue.enqueue('m');
        assertEquals('m', charQueue.peek());
        charQueue.enqueue('a');
        assertEquals(false, charQueue.isEmpty());
        assertEquals(2, charQueue.size());
        assertEquals('m', charQueue.peek());
        assertEquals('m', charQueue.dequeue());
        charQueue.clear();
        assertThrows(NoSuchElementException.class, () -> {
            charQueue.peek();
        });
    }

    @Test
    void queueTest3(){
        CharQueue charQueue = new CharQueue(3);
        charQueue.enqueue('A');
        charQueue.enqueue('B');
        charQueue.enqueue('C');
        assertEquals('A', charQueue.dequeue());
        assertEquals(2, charQueue.size());
        assertEquals('B', charQueue.dequeue());
        assertEquals('C', charQueue.peek());
        assertEquals(false, charQueue.isEmpty());
        charQueue.clear();
        assertEquals(true, charQueue.isEmpty());
        assertEquals(0, charQueue.size());
    }

    @Test
    void queueTest4(){
        CharQueue charQueue = new CharQueue(10);
        CharQueue charQueue1 = new CharQueue(10);
        charQueue.enqueue('A');
        assertEquals(true, charQueue.size() > charQueue1.size());
    }

    @Test
    void badInit(){
        assertThrows(IllegalArgumentException.class, () -> {
            CharQueue charQueue = new CharQueue(0);
        });
    }
}
