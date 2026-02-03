/*
 * Name: Issac Roy
 * PID: A17787465
 */

import java.util.*;

/**
 * Cache Implementation
 *
 * @author Issac Roy
 * @since 6/4/2024
 */

public class PandaCache {
    private HashMap<Integer, Integer> map;
    private LinkedList<Integer> list;
    private int capacity;

    public PandaCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>(capacity);
        list = new LinkedList<>();
    }

    public int get(int pandaID) {
        if (map.containsKey(pandaID)){
            list.remove(list.indexOf(pandaID));
            list.add(pandaID);
            return map.get(pandaID);
        } else return -1;
    }

    public void set(int pandaID, int zoneNumber) {
        list.add(pandaID);
        map.put(pandaID, zoneNumber);
        capacity--;
        if (capacity < 0) {
            int ID = list.remove();
            map.remove(ID);
        }
    }
}