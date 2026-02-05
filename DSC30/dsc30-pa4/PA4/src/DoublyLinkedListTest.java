import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DoublyLinkedListTest {

    @Test
    void LinkedListTest1(){
        DoublyLinkedList<String> list = new DoublyLinkedList<>();
        assertEquals(true, list.add("VA"));
        assertThrows(NullPointerException.class, () -> {
            list.add(null);
        });
        list.add(0, "JA");
        assertEquals(false, list.isEmpty());
        assertEquals(2, list.size());
        assertEquals("[(head) -> JA -> VA -> (tail)]", list.toString());
        list.clear();
        assertEquals(true, list.isEmpty());
        assertEquals(0, list.size());
        list.add("D");
        assertThrows(NullPointerException.class, () -> {
            list.add(0, null);
        });
        assertThrows(IndexOutOfBoundsException.class, () -> {
            list.add(2, "C");
        });
        list.add("A");
        list.add("C");
        list.add("B");
        assertEquals(true, list.contains("A"));
        assertEquals("A", list.get(1));
        assertEquals("[(head) -> D -> A -> C -> B -> (tail)]", list.toString());
        assertEquals("A", list.set(1, "S"));
        assertEquals("B", list.remove(list.size()-1));
        assertEquals(false, list.contains("A"));
        assertEquals("[(head) -> D -> S -> C -> (tail)]", list.toString());
        list.add(list.size(), "30");
        assertEquals("[(head) -> D -> S -> C -> 30 -> (tail)]", list.toString());
    }

    @Test
    void LinkedListTest2(){
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        assertEquals(true, list.isEmpty());
        assertEquals(0, list.size());
        assertEquals("[(head) -> (tail)]", list.toString());
        assertEquals(true, list.add(0));
        assertThrows(IndexOutOfBoundsException.class, () -> {
            list.set(1, 10);
        });
        assertEquals(false, list.contains(10));
        assertThrows(NullPointerException.class, () -> {
            list.set(0, null);
        });
        assertEquals(0, list.set(0, 10));
        assertEquals("[(head) -> 10 -> (tail)]", list.toString());
        assertThrows(IndexOutOfBoundsException.class, () -> {
            list.remove(1);
        });
        assertEquals(1, list.size());
        assertThrows(IndexOutOfBoundsException.class, () -> {
            list.get(1);
        });
        assertThrows(IndexOutOfBoundsException.class, () -> {
            list.get(-1);
        });
        assertEquals(10, list.get(0));
        list.clear();
        list.add(0);
        list.add(4);
        list.add(1, 2);
        assertThrows(IndexOutOfBoundsException.class, () -> {
            list.add(-1, -2);
        });
        assertEquals("[(head) -> 0 -> 2 -> 4 -> (tail)]", list.toString());
    }

    @Test
    void LinkedListTest3(){
        DoublyLinkedList<Character> list = new DoublyLinkedList<>();
        assertEquals(true, list.add('J'));
        assertEquals(true, list.add('A'));
        list.add(1, 'V');
        list.add(1, 'A');
        list.add(1, 'A');
        assertEquals("[(head) -> J -> A -> A -> V -> A -> (tail)]", list.toString());
        assertEquals(true, list.contains('J'));
        assertEquals(false, list.contains('D'));
        assertEquals(false, list.isEmpty());
        assertEquals('A', list.get(list.size()-1));
        assertEquals('A', list.remove(1));
        assertEquals(4, list.size());
        assertEquals('V', list.set(2, 'B'));
        assertEquals(4, list.size());
        assertEquals("[(head) -> J -> A -> B -> A -> (tail)]", list.toString());
        list.clear();
        assertEquals("[(head) -> (tail)]", list.toString());
    }

    @Test
    void swapHalvesTest1(){
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);
        list.add(7);
        list.add(8);
        assertEquals("[(head) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> (tail)]",
                list.toString());

        assertThrows(IllegalArgumentException.class, () -> {
            list.swapHalves(-1, 0, list.size()-1);
        });

        list.swapHalves(3, 0, list.size()-1);
        assertEquals("[(head) -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (tail)]",
                list.toString());
    }

    @Test
    void swapHalvesTest2(){
        DoublyLinkedList<String> list = new DoublyLinkedList<>();
        list.add("J");
        list.add("A");
        list.add("V");
        list.add("A");
        assertEquals("[(head) -> J -> A -> V -> A -> (tail)]", list.toString());

        assertThrows(IllegalArgumentException.class, () -> {
            list.swapHalves(3, 0, list.size()-1);
        });

        list.swapHalves(2, 0, list.size()-1);
        assertEquals("[(head) -> A -> V -> A -> J -> (tail)]", list.toString());
    }

    @Test
    void swapHalvesTest3(){
        DoublyLinkedList<Character> list = new DoublyLinkedList<>();
        list.add('P');
        list.add('Y');
        list.add('T');
        list.add('H');
        list.add('O');
        list.add('N');
        assertEquals("[(head) -> P -> Y -> T -> H -> O -> N -> (tail)]", list.toString());

        list.swapHalves(1, 0, list.size()-1);
        assertEquals("[(head) -> H -> O -> N -> P -> Y -> T -> (tail)]", list.toString());
    }

    @Test
    void swapHalvesTest4(){
        DoublyLinkedList<Character> list = new DoublyLinkedList<>();
        list.add('P');
        list.add('Y');
        list.add('T');
        list.add('H');
        list.add('O');
        list.add('N');
        assertEquals("[(head) -> P -> Y -> T -> H -> O -> N -> (tail)]", list.toString());

        list.swapHalves(0, 0, list.size()-1);
        assertEquals("[(head) -> P -> Y -> T -> H -> O -> N -> (tail)]", list.toString());
    }

    @Test
    void sliceTest1(){
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);
        list.add(7);
        list.add(8);
        list.add(9);
        assertEquals("[(head) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> (tail)]",
                list.toString());

        assertThrows(IllegalArgumentException.class, () -> {
            list.slice(-1, 8, 2);
        });
        assertThrows(IllegalArgumentException.class, () -> {
            list.slice(0, -1, 2);
        });
        assertThrows(IllegalArgumentException.class, () -> {
            list.slice(0, 8, 0);
        });

        list.slice(2, 8, 2);
        assertEquals(3, list.size());
        assertEquals("[(head) -> 3 -> 5 -> 7 -> (tail)]", list.toString());
    }

    @Test
    void sliceTest2(){
        DoublyLinkedList<Integer> list = new DoublyLinkedList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);
        assertEquals("[(head) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> (tail)]", list.toString());
        list.slice(10, 1, 1);
        assertEquals("[(head) -> (tail)]", list.toString());
    }

    @Test
    void sliceTest3(){
        DoublyLinkedList<Character> list = new DoublyLinkedList<>();
        list.add('J');
        list.add('B');
        list.add('A');
        list.add('C');
        list.add('V');
        list.add('D');
        list.add('A');
        assertEquals("[(head) -> J -> B -> A -> C -> V -> D -> A -> (tail)]",
                list.toString());
        list.slice(0, list.size(), 2);
        assertEquals("[(head) -> J -> A -> V -> A -> (tail)]", list.toString());
    }
}
