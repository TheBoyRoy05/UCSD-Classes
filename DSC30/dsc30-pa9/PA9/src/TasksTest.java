import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.*;

public class TasksTest {

    @Test
    public void testRaffleChecker_noDuplicates() {
        int[] entries = {1, 2, 3, 4, 5};
        assertFalse(Tasks.raffleChecker(entries));
    }

    @Test
    public void testRaffleChecker_withDuplicates() {
        int[] entries = {1, 2, 3, 4, 5, 3};
        assertTrue(Tasks.raffleChecker(entries));
    }

    @Test
    public void testRaffleChecker_emptyArray() {
        int[] entries = {};
        assertFalse(Tasks.raffleChecker(entries));
    }

    @Test
    public void testRaffleChecker_singleElement() {
        int[] entries = {1};
        assertFalse(Tasks.raffleChecker(entries));
    }

    @Test
    public void testMiddleNode_singleNode() {
        Tasks.Node head = new Tasks.Node("A");
        assertEquals("A", Tasks.middleNode(head));
    }

    @Test
    public void testMiddleNode_oddNumberOfNodes() {
        Tasks.Node head = new Tasks.Node("A");
        head.next = new Tasks.Node("B");
        head.next.next = new Tasks.Node("C");
        assertEquals("B", Tasks.middleNode(head));
    }

    @Test
    public void testCanConstruct_trueCase() {
        assertTrue(Tasks.canConstruct("hello world", "eolhlolwr d"));
    }

    @Test
    public void testCanConstruct_falseCase() {
        assertFalse(Tasks.canConstruct("hello world", "ehl lwlord"));
    }

    @Test
    public void testCanConstruct_emptyNewMessage() {
        assertTrue(Tasks.canConstruct("", "anystring"));
    }

    @Test
    public void testCanConstruct_emptyOldMessage() {
        assertFalse(Tasks.canConstruct("hello", ""));
    }

    @Test
    public void testFrequentCustomers_singleMostFrequent() {
        String[] buyers = {"Alice", "Bob", "Alice", "Alice", "Charlie"};
        String[] expected = {"Alice"};
        assertArrayEquals(expected, Tasks.frequentCustomers(buyers, 1));
    }

    @Test
    public void testFrequentCustomers_multipleMostFrequent() {
        String[] buyers = {"Alice", "Bob", "Alice", "Bob", "Charlie"};
        String[] expected = {"Alice", "Bob"};
        assertArrayEquals(expected, Tasks.frequentCustomers(buyers, 2));
    }
}
