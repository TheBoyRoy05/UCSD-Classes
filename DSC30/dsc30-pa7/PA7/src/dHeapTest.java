import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.NoSuchElementException;

class dHeapTest {
    @Test
    void dHeapTest1(){
        dHeap<Integer> heap = new dHeap<>();
        assertEquals(0, heap.size());
        assertThrows(NoSuchElementException.class, () -> {
            heap.remove();
        });
        for (int i = 0; i < 10; i++) {
            heap.add(i);
        }
        assertEquals(10, heap.size());
        assertEquals(9, heap.element());
        assertEquals(10, heap.size());
        assertEquals(9, heap.remove());
        assertEquals(9, heap.size());
        heap.clear();
        assertEquals(0, heap.size());
        for (int i = 0; i < 10; i++) {
            heap.add(i);
        }
        for (int i = 0; i < 10; i++) {
            assertEquals(10-i-1, heap.remove());
        }
        assertEquals(0, heap.size());
    }

    @Test
    void dHeapTest2(){
        assertThrows(IllegalArgumentException.class, () -> {
            dHeap<Integer> heap = new dHeap<>(0, 1, true);
        });
        dHeap<Integer> heap = new dHeap<>(1);
        for (int i = 0; i < 20; i++) {
            heap.add(i);
            assertEquals(i, heap.element());
            assertEquals(i, heap.remove());
        }
        assertEquals(0, heap.size());
        assertThrows(NullPointerException.class, () -> {
            heap.add(null);
        });
        for (int i = 0; i < 5; i++) {
            heap.add(5);
        }
        heap.clear();
        assertEquals(0, heap.size());
    }

    @Test
    void dHeapTest3(){
        dHeap<Integer> heap = new dHeap<>(3, 10, true);
        assertThrows(NoSuchElementException.class, () -> {
            heap.element();
        });
        for (int i = 0; i < 100; i++) {
            heap.add(i);
        }
        assertEquals(100, heap.size());
        assertEquals(99, heap.element());
        assertEquals(99, heap.remove());
        for (int i = 0; i < 99; i++) {
            assertEquals(99-i-1, heap.remove());
        }
        heap.clear();
    }
    private dHeap<Integer> minHeap;
    private dHeap<Integer> maxHeap;

    @BeforeEach
    void setUp() {
        minHeap = new dHeap<>(2, 10, false);
        maxHeap = new dHeap<>(2, 10, true);
    }

    @Test
    void testInitialization() {
        assertEquals(0, minHeap.size());
        assertEquals(0, maxHeap.size());
    }

    @Test
    void testAddAndSize() {
        maxHeap.add(10);
        maxHeap.add(20);
        assertEquals(2, maxHeap.size());

        minHeap.add(10);
        minHeap.add(5);
        assertEquals(2, minHeap.size());
    }

    @Test
    void testElement() {
        maxHeap.add(10);
        assertEquals(10, maxHeap.element());

        minHeap.add(5);
        assertEquals(5, minHeap.element());
    }

    @Test
    void testRemove() {
        maxHeap.add(10);
        maxHeap.add(20);
        assertEquals(20, maxHeap.remove());
        assertEquals(10, maxHeap.remove());

        minHeap.add(10);
        minHeap.add(5);
        assertEquals(5, minHeap.remove());
        assertEquals(10, minHeap.remove());
    }

    @Test
    void testClear() {
        maxHeap.add(10);
        maxHeap.add(20);
        maxHeap.clear();
        assertEquals(0, maxHeap.size());

        minHeap.add(10);
        minHeap.add(5);
        minHeap.clear();
        assertEquals(0, minHeap.size());
    }

    @Test
    void testEmptyHeapExceptions() {
        assertThrows(NoSuchElementException.class, () -> maxHeap.remove());
        assertThrows(NoSuchElementException.class, () -> maxHeap.element());

        assertThrows(NoSuchElementException.class, () -> minHeap.remove());
        assertThrows(NoSuchElementException.class, () -> minHeap.element());
    }

    @Test
    void testNullElementException() {
        assertThrows(NullPointerException.class, () -> maxHeap.add(null));
        assertThrows(NullPointerException.class, () -> minHeap.add(null));
    }

    @Test
    void testIllegalD() {
        assertThrows(IllegalArgumentException.class, () -> new dHeap<>(0, 10, true));
        assertThrows(IllegalArgumentException.class, () -> new dHeap<>(-1, 10, false));
    }

    @Test
    void testResize() {
        dHeap<Integer> smallHeap = new dHeap<>(2, 1, true);
        smallHeap.add(10);
        smallHeap.add(20);
        assertEquals(2, smallHeap.size());
    }

    @Test
    void testMaxHeapProperty() {
        maxHeap.add(10);
        maxHeap.add(20);
        maxHeap.add(5);
        assertEquals(20, maxHeap.element());

        maxHeap.add(25);
        assertEquals(25, maxHeap.element());
    }

    @Test
    void testMinHeapProperty() {
        minHeap.add(10);
        minHeap.add(20);
        minHeap.add(5);
        assertEquals(5, minHeap.element());

        minHeap.add(1);
        assertEquals(1, minHeap.element());
    }
}
