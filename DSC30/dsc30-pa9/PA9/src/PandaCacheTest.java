import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class PandaCacheTest {

    private PandaCache cache;

    @BeforeEach
    public void setUp() {
        cache = new PandaCache(3);
    }

    @Test
    public void testGetNonExistentPanda() {
        assertEquals(-1, cache.get(1), "Getting non-existent panda should return -1");
    }

    @Test
    public void testSetAndGetPanda() {
        cache.set(1, 101);
        assertEquals(101, cache.get(1), "Getting panda with ID 1 should return zone 101");
    }

    @Test
    public void testSetAndEvictPanda() {
        cache.set(1, 101);
        cache.set(2, 102);
        cache.set(3, 103);
        cache.set(4, 104);  // This should evict the first panda (ID 1)

        assertEquals(-1, cache.get(1), "Panda with ID 1 should be evicted");
        assertEquals(102, cache.get(2), "Getting panda with ID 2 should return zone 102");
        assertEquals(103, cache.get(3), "Getting panda with ID 3 should return zone 103");
        assertEquals(104, cache.get(4), "Getting panda with ID 4 should return zone 104");
    }

    @Test
    public void testSetAndAccessPanda() {
        cache.set(1, 101);
        cache.set(2, 102);
        cache.set(3, 103);

        // Access panda with ID 1 to move it to the end of the list
        assertEquals(101, cache.get(1), "Getting panda with ID 1 should return zone 101");

        cache.set(4, 104);  // This should evict the panda with ID 2, since ID 1 was recently accessed

        assertEquals(101, cache.get(1), "Getting panda with ID 1 should return zone 101");
        assertEquals(-1, cache.get(2), "Panda with ID 2 should be evicted");
        assertEquals(103, cache.get(3), "Getting panda with ID 3 should return zone 103");
        assertEquals(104, cache.get(4), "Getting panda with ID 4 should return zone 104");
    }

    @Test
    public void testSetUpdateExistingPanda() {
        cache.set(1, 101);
        cache.set(1, 102);  // Update the zone of panda with ID 1

        assertEquals(102, cache.get(1), "Getting panda with ID 1 should return updated zone 102");
    }

    @Test
    public void writeUpTest(){
        cache.set(123, 1);
        cache.set(456, 2);
        cache.set(789, 1);

        assertEquals(1, cache.get(123));
        cache.set(999, 3);
        assertEquals(-1, cache.get(456));
    }
}
