import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MyHashTableTest {

    private MyHashTable hashTable;

    @BeforeEach
    void setUp() {
        hashTable = new MyHashTable();
    }

    @Test
    void testDefaultConstructor() {
        assertEquals(19, hashTable.capacity());
        assertEquals(0, hashTable.size());
    }

    @Test
    void testConstructorWithCapacity() {
        MyHashTable customHashTable = new MyHashTable(23);
        assertEquals(23, customHashTable.capacity());
    }

    @Test
    void testConstructorWithCapacityThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> new MyHashTable(5));
    }

    @Test
    void testInsert() {
        assertTrue(hashTable.insert("Test"));
        assertEquals(1, hashTable.size());
    }

    @Test
    void testInsertDuplicate() {
        assertTrue(hashTable.insert("Test"));
        assertFalse(hashTable.insert("Test"));
    }

    @Test
    void testInsertNullThrowsException() {
        assertThrows(NullPointerException.class, () -> hashTable.insert(null));
    }

    @Test
    void testInsertMultipleElements() {
        assertTrue(hashTable.insert("Test1"));
        assertTrue(hashTable.insert("Test2"));
        assertTrue(hashTable.insert("Test3"));
        assertEquals(3, hashTable.size());
    }

    @Test
    void testDelete() {
        hashTable.insert("Test");
        assertTrue(hashTable.delete("Test"));
        assertEquals(0, hashTable.size());
    }

    @Test
    void testDeleteNonExistent() {
        assertFalse(hashTable.delete("Test"));
    }

    @Test
    void testDeleteNullThrowsException() {
        assertThrows(NullPointerException.class, () -> hashTable.delete(null));
    }

    @Test
    void testDeleteMultipleElements() {
        hashTable.insert("Test1");
        hashTable.insert("Test2");
        hashTable.insert("Test3");
        assertTrue(hashTable.delete("Test1"));
        assertTrue(hashTable.delete("Test2"));
        assertTrue(hashTable.delete("Test3"));
        assertEquals(0, hashTable.size());
    }

    @Test
    void testLookup() {
        hashTable.insert("Test");
        assertTrue(hashTable.lookup("Test"));
    }

    @Test
    void testLookupNonExistent() {
        assertFalse(hashTable.lookup("NonExistent"));
    }

    @Test
    void testLookupNullThrowsException() {
        assertThrows(NullPointerException.class, () -> hashTable.lookup(null));
    }

    @Test
    void testLookupMultipleElements() {
        hashTable.insert("Test1");
        hashTable.insert("Test2");
        hashTable.insert("Test3");
        assertTrue(hashTable.lookup("Test1"));
        assertTrue(hashTable.lookup("Test2"));
        assertTrue(hashTable.lookup("Test3"));
    }

    @Test
    void testReturnAll() {
        hashTable.insert("Test1");
        hashTable.insert("Test2");
        String[] allElements = hashTable.returnAll();
        assertEquals(2, allElements.length);
        assertArrayEquals(new String[]{"Test1", "Test2"}, allElements);
    }

    @Test
    void testReturnAllWithNoElements() {
        String[] allElements = hashTable.returnAll();
        assertEquals(0, allElements.length);
    }

    @Test
    void testReturnAllWithMultipleElements() {
        hashTable.insert("Test1");
        hashTable.insert("Test2");
        hashTable.insert("Test3");
        String[] allElements = hashTable.returnAll();
        assertEquals(3, allElements.length);
        assertArrayEquals(new String[]{"Test1", "Test2", "Test3"}, allElements);
    }

    @Test
    void testSize() {
        hashTable.insert("Test");
        assertEquals(1, hashTable.size());
        hashTable.insert("Test2");
        assertEquals(2, hashTable.size());
    }

    @Test
    void testSizeAfterDeletions() {
        hashTable.insert("Test");
        hashTable.insert("Test2");
        hashTable.delete("Test");
        assertEquals(1, hashTable.size());
        hashTable.delete("Test2");
        assertEquals(0, hashTable.size());
    }

    @Test
    void testCapacity() {
        assertEquals(19, hashTable.capacity());
    }

    @Test
    void testCapacityAfterInsertions() {
        MyHashTable smallHashTable = new MyHashTable(7);
        for (int i = 0; i < 10; i++) {
            smallHashTable.insert("Test" + i);
        }
        assertTrue(smallHashTable.capacity() > 7);
    }

    @Test
    void testGetStatsLog() {
        hashTable.insert("Test1");
        hashTable.insert("Test2");
        assertTrue(hashTable.getStatsLog().isEmpty());
    }

    @Test
    void testGetStatsLogInitiallyEmpty() {
        assertTrue(hashTable.getStatsLog().isEmpty());
    }

    @Test
    void testGetStatsLogAfterMultipleInsertions() {
        for (int i = 0; i < 100; i++) {
            hashTable.insert("Element" + i);
        }
        System.out.println(hashTable.getStatsLog());
        assertFalse(hashTable.getStatsLog().isEmpty());
    }

    @Test
    void testRehash() {
        MyHashTable smallHashTable = new MyHashTable(7);
        for (int i = 0; i < 10; i++) {
            smallHashTable.insert("Test" + i);
        }
        assertTrue(smallHashTable.capacity() > 7);
        assertTrue(smallHashTable.getStatsLog().contains("Before rehash"));
    }

    @Test
    void testRehashMultipleTimes() {
        MyHashTable smallHashTable = new MyHashTable(7);
        for (int i = 0; i < 50; i++) {
            smallHashTable.insert("Test" + i);
        }
        assertTrue(smallHashTable.capacity() > 14);
        assertTrue(smallHashTable.getStatsLog().contains("Before rehash"));
    }

    @Test
    void testInsert100Elements() {
        for (int i = 0; i < 100; i++) {
            assertTrue(hashTable.insert("Element " + i));
        }
        assertEquals(100, hashTable.size());
        for (int i = 0; i < 100; i++) {
            assertTrue(hashTable.lookup("Element " + i));
        }
        assertTrue(hashTable.capacity() > 19);
    }
}
