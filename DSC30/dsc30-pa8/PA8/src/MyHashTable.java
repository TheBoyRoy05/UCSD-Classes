/*
 * Name: Issac Roy
 * PID: A17787465
 */

import java.util.LinkedList;

/**
 * Hash Table implementation
 * 
 * @author Issac Roy
 * @since 05/27/2024
 */

public class MyHashTable implements KeyedSet {

    /* instance variables */
    private int size; // number of elements stored
    private LinkedList<String>[] table; // data table
    private int numRehashes;
    private int numCollisions;
    private String stats;

    private static final int DEFAULT_CAPACITY = 19;
    private static final int MIN_CAPACITY = 7;

    /**
     * Default Constructor
     */
    public MyHashTable() {
        this(DEFAULT_CAPACITY);
    }

    /**
     * Constructor with capacity
     * @param capacity initial capacity of hash table
     * @throws IllegalArgumentException if capacity is less than 7
     */
    @SuppressWarnings("unchecked")
    public MyHashTable(int capacity) throws IllegalArgumentException{
        if (capacity < MIN_CAPACITY) throw new IllegalArgumentException();
        table = new LinkedList[capacity];
        numRehashes = 0;
        numCollisions = 0;
        stats = "";
    }

    /**
     * Inserts value in the hash table
     *
     * @param value value to insert
     * @return true if the value was inserted, false if it already exists
     * @throws NullPointerException if value is null
     */
    public boolean insert(String value) throws NullPointerException{
        if (value == null) throw new NullPointerException();
        if (getLoadFactor() > 1) rehash();
        int hashValue = hashString(value);

        if (table[hashValue] == null) table[hashValue] = new LinkedList<>();
        else if (table[hashValue].contains(value)) return false;

        if (!table[hashValue].isEmpty()) numCollisions++;
        table[hashValue].add(value);
        size++;
        return true;
    }

    /**
     * Deletes the specified value from the hash table
     *
     * @param value value to delete
     * @return true if value was deleted, false if it doesn't exist
     * @throws NullPointerException if value is null
     */
    public boolean delete(String value) throws NullPointerException{
        if (value == null) throw new NullPointerException();
        int hashValue = hashString(value);
        if (table[hashValue] == null || !table[hashValue].contains(value)) return false;
        table[hashValue].remove(value);
        size--;
        return true;
    }

    /**
     * Returns whether value exists in the table or not
     *
     * @param value value to look up
     * @return true if the value is in the hash table, false otherwise
     * @throws NullPointerException if value is null
     */
    public boolean lookup(String value) throws NullPointerException{
        if (value == null) throw new NullPointerException();
        int hashValue = hashString(value);
        return table[hashValue] != null && table[hashValue].contains(value);
    }

    /**
     * Returns an array of all elements stored in the hashtable
     * @return an array of all elements stored in the hashtable
     */
    public String[] returnAll() {
        int pos = 0;
        String[] out = new String[size];
        for (int i = 0; i < table.length; i++) {
            if (table[i] == null) continue;
            while (!table[i].isEmpty()) {
                out[pos] = table[i].remove();
                pos++;
            }
        }
        return out;
    }

    /**
     * Returns the number of elements currently stored in the hash table
     * @return the number of elements currently stored in the hash table
     */
    public int size() {
        return size;
    }

    /**
     * Returns the total capacity of the table
     * @return the total capacity of the table
     */
    public int capacity() {
        return table.length;
    }

    /**
     * Returns the statistics log of the hash table
     * @return the statistics log of the hash table
     */
    public String getStatsLog() {
        return stats;
    }

    /**
     * Utility function provided to help with debugging
     */
    public void printTable() {
        String s = "";
        for (int i = 0; i < table.length; i++) {
            s = s + i + ":";
            if (!table[i].isEmpty()) {
                for (String t : table[i])
                    s = s + " " + t + ",";
                // remove trailing comma
                s = s.substring(0, s.length() - 1);
            }
            s = s + "\n";
        }
        // remove trailing newline
        s = s.substring(0, s.length() - 1);
        System.out.println(s);
    }

    /**
     * Rehash the table by doubling its capacity and rehashing each element
     */
    @SuppressWarnings("unchecked")
    private void rehash() {
        numRehashes++;
        stats += "Before rehash # " + numRehashes + ": " +
                "load factor " + String.format("%.2f", getLoadFactor()) + ", " +
                numCollisions + "collision(s).\n";
        numCollisions = 0;

        LinkedList<String>[] oldTable = table;
        table = new LinkedList[oldTable.length+oldTable.length];
        for (int i = 0; i < oldTable.length; i++) {
            if (oldTable[i] == null) continue;
            while (!oldTable[i].isEmpty()) {
                String value = oldTable[i].remove();
                int hashValue = hashString(value);
                if (table[hashValue] == null) table[hashValue] = new LinkedList<>();
                else numCollisions++;
                table[hashValue].add(value);
            }
        }
    }

    /**
     * Hashes the given string using the Simplified CRC hash function
     *
     * @param value string to be hashed
     * @return the hash value of the given string
     */
    private int hashString(String value) {
        int hashValue = 0;
        for (int i = 0; i < value.length(); i++) {
            int left = hashValue << 5;
            int right = hashValue >>> 27;
            hashValue = (left | right) ^ value.charAt(i);
        }
        return Math.abs(hashValue % table.length);
    }

    /**
     * Returns the current load factor of the hash table
     * @return the current load factor of the hash table
     */
    private double getLoadFactor(){
        return (double) size / (double) table.length;
    }
}
