import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class DonationStackTest {

    private DonationStack stack;

    @BeforeEach
    public void setUp() {
        stack = new DonationStack();
    }

    @Test
    public void testPushAndPeek() {
        stack.push(10);
        assertEquals(10, stack.peek());

        stack.push(20);
        assertEquals(20, stack.peek());

        stack.push(5);
        assertEquals(5, stack.peek());
    }

    @Test
    public void testPushAndMax() {
        stack.push(10);
        assertEquals(10, stack.max());

        stack.push(20);
        assertEquals(20, stack.max());

        stack.push(5);
        assertEquals(20, stack.max());

        stack.push(25);
        assertEquals(25, stack.max());
    }

    @Test
    public void testPop() {
        stack.push(10);
        stack.push(20);
        stack.push(5);

        assertEquals(5, stack.pop());
        assertEquals(20, stack.pop());
        assertEquals(10, stack.pop());
    }

    @Test
    public void testPopAndMax() {
        stack.push(10);
        stack.push(20);
        stack.push(5);

        assertEquals(5, stack.pop());
        assertEquals(20, stack.max());

        assertEquals(20, stack.pop());
        assertEquals(10, stack.max());

        assertEquals(10, stack.pop());
    }

    @Test
    public void testPushPopSequence() {
        stack.push(10);
        assertEquals(10, stack.peek());
        assertEquals(10, stack.max());

        stack.push(20);
        assertEquals(20, stack.peek());
        assertEquals(20, stack.max());

        stack.pop();
        assertEquals(10, stack.peek());
        assertEquals(10, stack.max());

        stack.push(15);
        assertEquals(15, stack.peek());
        assertEquals(15, stack.max());

        stack.push(5);
        assertEquals(5, stack.peek());
        assertEquals(15, stack.max());
    }

    @Test
    public void testMaxAfterPop() {
        stack.push(10);
        stack.push(20);
        stack.push(15);

        assertEquals(15, stack.pop());
        assertEquals(20, stack.max());

        assertEquals(20, stack.pop());
        assertEquals(10, stack.max());
    }

    @Test
    public void testEmptyStackOperations() {
        assertThrows(NullPointerException.class, () -> {
            stack.pop();
        });

        assertThrows(NullPointerException.class, () -> {
            stack.peek();
        });

        assertThrows(NullPointerException.class, () -> {
            stack.max();
        });
    }

    @Test
    public void testPushPopAndMaxSequence() {
        stack.push(5);
        stack.push(10);
        stack.push(5);
        stack.push(20);
        stack.push(15);
        assertEquals(20, stack.max());
        assertEquals(15, stack.pop());
        assertEquals(20, stack.pop());
        assertEquals(10, stack.max());
    }
}