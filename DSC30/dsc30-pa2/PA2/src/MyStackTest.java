import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import utilities.FullStackException;
import java.util.EmptyStackException;

import static org.junit.jupiter.api.Assertions.*;

class MyStackTest {
    @Test
    void stackTest1(){
        MyStack myStack = new MyStack();
        assertEquals(10, myStack.capacity());
        myStack.push("A");
        assertEquals(false, myStack.isEmpty());
        assertEquals("A", myStack.peek());
        assertEquals(1, myStack.size());
        assertEquals("A", myStack.pop());
        assertEquals(true, myStack.isEmpty());
    }

    @Test
    void stackTest2(){
        MyStack myStack = new MyStack();
        myStack.multiPush(new String[] {"A", "B", "C"});
        String[] popped = myStack.multiPop(2);
        assertNotNull(popped);
        assertEquals(2, popped.length);
        assertEquals("C", popped[0]);
        myStack.clear();
        assertEquals(0, myStack.size());
    }

    @Test
    void stackTest3(){
        MyStack myStack = new MyStack(5);
        assertEquals(5, myStack.capacity());
        myStack.push("1");
        assertEquals("1", myStack.peek());
        assertEquals(1, myStack.size());
        assertEquals("1", myStack.pop());
        assertEquals(true, myStack.isEmpty());
    }

    @Test
    void stackTest4(){
        MyStack myStack = new MyStack(5);
        myStack.multiPush(new String[] {"1", "2", "3"});
        String[] popped = myStack.multiPop(1);
        assertNotNull(popped);
        assertEquals(1, popped.length);
        assertEquals("3", popped[0]);
        myStack.clear();
        assertEquals(0, myStack.size());
    }

    @Test
    void stackTest5(){
        MyStack myStack = new MyStack(3);
        assertEquals(3, myStack.capacity());
        myStack.push("Yes");
        assertEquals("Yes", myStack.peek());
        assertEquals(1, myStack.size());
        assertEquals("Yes", myStack.pop());
        assertEquals(true, myStack.isEmpty());
    }

    @Test
    void stackTest6(){
        MyStack myStack = new MyStack(3);
        myStack.multiPush(new String[] {"Yes", "Maybe", "No"});
        String[] popped = myStack.multiPop(3);
        assertNotNull(popped);
        assertEquals(3, popped.length);
        assertEquals("No", popped[0]);
        assertEquals("Maybe", popped[1]);
        assertEquals("Yes", popped[2]);
        assertEquals(0, myStack.size());
    }

    @Test
    void badStackInit(){
        assertThrows(IllegalArgumentException.class, () -> {
            MyStack myStack = new MyStack(0);
        });
    }

    @Test
    void badStackPeek(){
        MyStack myStack = new MyStack();
        assertThrows(EmptyStackException.class, () -> {
            myStack.peek();
        });
    }

    @Test
    void badStackPush1(){
        MyStack myStack = new MyStack(1);
        myStack.push("JA");
        assertThrows(FullStackException.class, () -> {
            myStack.push("VA");
        });
    }

    @Test
    void badStackPush2(){
        MyStack myStack = new MyStack(1);
        assertThrows(IllegalArgumentException.class, () -> {
            myStack.push(null);
        });
    }

    @Test
    void badStackPop(){
        MyStack myStack = new MyStack();
        assertThrows(EmptyStackException.class, () -> {
            myStack.pop();
        });
    }

    @Test
    void badStackMultiPush1(){
        MyStack myStack = new MyStack(1);
        assertThrows(FullStackException.class, () -> {
            myStack.multiPush(new String[] {"J", "A", "V", "A"});
        });
    }

    @Test
    void badStackMultiPush2(){
        MyStack myStack = new MyStack();
        assertThrows(IllegalArgumentException.class, () -> {
            myStack.multiPush(null);
        });
    }

    @Test
    void badStackMultiPop(){
        MyStack myStack = new MyStack();
        myStack.multiPush(new String[] {"J", "A", "V", "A"});
        assertThrows(IllegalArgumentException.class, () -> {
            myStack.multiPop(0);
        });
    }
}