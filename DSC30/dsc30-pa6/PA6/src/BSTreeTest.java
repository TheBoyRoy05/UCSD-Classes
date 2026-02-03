import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

class BSTreeTest {
    @Test
    void BSTreeTest1(){
        Integer[] data = new Integer[]{3, 5, 1, 2, 8, 0};
        BSTree<Integer> tree = new BSTree<>();

        for (int i = 0; i < data.length; i++) {
            assertEquals(true, tree.insert(data[i]));
        }
        assertEquals(3, tree.getRoot().getKey());
        assertEquals(1, tree.getRoot().getLeft().getKey());
        assertEquals(5, tree.getRoot().getRight().getKey());

        assertEquals(6, tree.getSize());
        assertEquals(true, tree.findKey(8));
        assertThrows(NullPointerException.class, () -> {
            tree.insert(null);
        });
        tree.insertData(1, Integer.valueOf(9));
        assertEquals(9, tree.findDataList(1).peek());
        assertEquals(2, tree.findHeight());
        assertEquals(false, tree.insert(8));

        Iterator<Integer> iter = tree.iterator();
        Arrays.sort(data);
        for (int i = 0; i < data.length; i++) {
            assertEquals(true, iter.hasNext());
            assertEquals(data[i], iter.next());
        }
        assertEquals(false, iter.hasNext());
    }

    @Test
    void BSTreeTest2(){
        Integer[] data = new Integer[]{1, 10, 2, 3, 4, 5, 6};
        BSTree<Integer> tree = new BSTree<>();
        for (int i = 0; i < data.length; i++) {
            assertEquals(true, tree.insert(data[i]));
        }
        assertEquals(1, tree.getRoot().getKey());
        assertEquals(10, tree.getRoot().getRight().getKey());

        assertEquals(7, tree.getSize());
        assertEquals(6, tree.findHeight());
        assertEquals(false, tree.findKey(8));
        assertThrows(NullPointerException.class, () -> {
            tree.findKey(null);
        });
        tree.insertData(6, Integer.valueOf(100));
        assertEquals(100, tree.findDataList(6).peek());

        assertThrows(NullPointerException.class, () -> {
            tree.findDataList(null);
        });
        assertThrows(IllegalArgumentException.class, () -> {
            tree.findDataList(100);
        });

        Iterator<Integer> iter = tree.iterator();
        Arrays.sort(data);
        for (int i = 0; i < data.length; i++) {
            assertEquals(true, iter.hasNext());
            assertEquals(data[i], iter.next());
        }
        assertEquals(false, iter.hasNext());

        assertEquals(true, tree.insert(8));
        assertEquals(7, tree.findHeight());

    }

    @Test
    void BSTreeTest3(){
        Integer[] data = new Integer[]{4, 2, 6, 1, 3, 5, 7};
        BSTree<Integer> tree = new BSTree<>();
        for (int i = 0; i < data.length; i++) {
            assertEquals(true, tree.insert(data[i]));
        }
        assertEquals(4, tree.getRoot().getKey());
        assertEquals(6, tree.getRoot().getRight().getKey());
        assertEquals(2, tree.getRoot().getLeft().getKey());

        assertEquals(7, tree.getSize());
        assertEquals(false, tree.findKey(8));

        assertThrows(NullPointerException.class, () -> {
            tree.insertData(null, Integer.valueOf(1));
        });
        assertThrows(NullPointerException.class, () -> {
            tree.insertData(2, null);
        });
        assertThrows(IllegalArgumentException.class, () -> {
            tree.insertData(10, Integer.valueOf(10));
        });

        tree.insertData(1, Integer.valueOf(2));
        assertEquals(2, tree.findDataList(1).peek());
        assertEquals(null, tree.findDataList(2).peek());
        assertEquals(2, tree.findHeight());

        Iterator<Integer> iter = tree.iterator();
        Arrays.sort(data);
        for (int i = 0; i < data.length; i++) {
            assertEquals(true, iter.hasNext());
            assertEquals(data[i], iter.next());
        }
        assertEquals(false, iter.hasNext());

        assertEquals(true, tree.insert(8));
        assertEquals(3, tree.findHeight());
    }

    @Test
    void intersectionTest1(){
        Integer[] data1 = new Integer[]{5, 1, 10, 0, 4, 7, 9};
        BSTree<Integer> tree1 = new BSTree<>();
        for (int i = 0; i < data1.length; i++) {
            assertEquals(true, tree1.insert(data1[i]));
        }

        Integer[] data2 = new Integer[]{10, 7, 20, 4, 9};
        BSTree<Integer> tree2 = new BSTree<>();
        for (int i = 0; i < data2.length; i++) {
            assertEquals(true, tree2.insert(data2[i]));
        }

        Iterator<Integer> iter1 = tree1.iterator();
        Iterator<Integer> iter2 = tree2.iterator();

        assertEquals("[4, 7, 9, 10]", tree1.intersection(iter1, iter2).toString());
    }

    @Test
    void intersectionTest2(){
        Integer[] data1 = new Integer[]{5, 1, 10, 0, 4, 7, 9};
        BSTree<Integer> tree1 = new BSTree<>();
        for (int i = 0; i < data1.length; i++) {
            assertEquals(true, tree1.insert(data1[i]));
        }

        BSTree<Integer> tree2 = new BSTree<>();

        Iterator<Integer> iter1 = tree1.iterator();
        Iterator<Integer> iter2 = tree2.iterator();

        assertEquals("[]", tree1.intersection(iter1, iter2).toString());
    }

    @Test
    void levelMaxTest1(){
        Integer[] data1 = new Integer[]{4, 2, 5, 1, 3};
        BSTree<Integer> tree1 = new BSTree<>();
        for (int i = 0; i < data1.length; i++) {
            assertEquals(true, tree1.insert(data1[i]));
        }

        assertEquals(4, tree1.levelMax(0));
        assertEquals(5, tree1.levelMax(1));
        assertEquals(3, tree1.levelMax(2));
        assertEquals(null, tree1.levelMax(3));
    }
    private BSTree<Integer> bst;
    @BeforeEach
    public void setUp () {
        bst = new BSTree<>();
    }

    @Test
    public void testInsertAndGetSize () {
        assertTrue(bst.insert(5));
        assertTrue(bst.insert(3));
        assertTrue(bst.insert(7));
        assertEquals(3, bst.getSize());

        assertFalse(bst.insert(5)); // Duplicate insertion
        assertEquals(3, bst.getSize());
    }

    @Test
    public void testFindKey () {
        bst.insert(5);
        bst.insert(3);
        bst.insert(7);

        assertTrue(bst.findKey(5));
        assertTrue(bst.findKey(3));
        assertTrue(bst.findKey(7));
        assertFalse(bst.findKey(4));
    }

    @Test
    public void testInsertDataAndFindDataList () {
        bst.insert(5);
        bst.insertData(5, 10);
        bst.insertData(5, 15);

        LinkedList<Integer> dataList = bst.findDataList(5);
        assertEquals(2, dataList.size());
        assertTrue(dataList.contains(10));
        assertTrue(dataList.contains(15));

        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            bst.insertData(3, 10); // Key 3 not in the BST
        });
        assertEquals("java.lang.IllegalArgumentException", exception.getClass().getName());
    }

    @Test
    public void testFindHeight () {
        assertEquals(-1, bst.findHeight()); // Empty tree

        bst.insert(5);
        assertEquals(0, bst.findHeight());

        bst.insert(3);
        bst.insert(7);
        assertEquals(1, bst.findHeight());

        bst.insert(2);
        bst.insert(1);
        assertEquals(3, bst.findHeight());
    }

    @Test
    public void testIterator () {
        bst.insert(5);
        bst.insert(3);
        bst.insert(7);
        bst.insert(2);
        bst.insert(4);
        bst.insert(6);
        bst.insert(8);

        Iterator<Integer> iterator = bst.iterator();
        int[] expectedOrder = {2, 3, 4, 5, 6, 7, 8};
        int index = 0;

        while (iterator.hasNext()) {
            assertEquals(expectedOrder[index++], iterator.next());
        }
        assertEquals(expectedOrder.length, index);

        Exception exception = assertThrows(NoSuchElementException.class, iterator::next);
        assertEquals("java.util.NoSuchElementException", exception.getClass().getName());
    }

    @Test
    public void testInsertNull () {
        assertThrows(NullPointerException.class, () -> {
            bst.insert(null);
        });
    }

    @Test
    public void testFindKeyNull () {
        assertThrows(NullPointerException.class, () -> {
            bst.findKey(null);
        });
    }

    @Test
    public void testInsertDataNullKey () {
        assertThrows(NullPointerException.class, () -> {
            bst.insertData(null, 10);
        });
    }

    @Test
    public void testInsertDataNullData () {
        bst.insert(5);
        assertThrows(NullPointerException.class, () -> {
            bst.insertData(5, null);
        });
    }

    @Test
    public void testFindDataListNullKey () {
        assertThrows(NullPointerException.class, () -> {
            bst.findDataList(null);
        });
    }

    @Test
    public void testFindDataListInvalidKey () {
        bst.insert(5);
        assertThrows(IllegalArgumentException.class, () -> {
            bst.findDataList(3);
        });
    }

    @Test
    public void testAdd100Elements() {
        // Add 100 elements
        for (int i = 0; i < 100; i++) {
            assertTrue(bst.insert(i));
        }
        assertEquals(100, bst.getSize());

        // Verify that all elements are present
        for (int i = 0; i < 100; i++) {
            assertTrue(bst.findKey(i));
        }
    }
}