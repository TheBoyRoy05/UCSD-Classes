/*
 * Name: Issac Roy
 * PID: A17787465
 */

import java.util.*;

/**
 * PA9 Part 2
 *
 * @author Issac Roy
 * @since 06/03/2024
 */

public class Tasks {

    /**
     * Checks for duplicate customer IDs in O(n) time
     * @param entries customer IDs
     * @return true if there are duplicates, false otherwise
     */
    public static boolean raffleChecker(int[] entries) {
        if (entries.length == 0) return false;
        int min = entries[0];
        int max = entries[0];
        for (int i = 0; i < entries.length; i++) {
            if (entries[i] > max) max = entries[i];
            if (entries[i] < min) min = entries[i];
        }
        int[] counts = new int[max-min+1];
        for (int i = 0; i < entries.length; i++) {
            if (counts[entries[i] - min] > 0) return true;
            else counts[entries[i] - min]++;
        }
        return false;
    }

    // List Node class provided for reference
    public static class Node {
        Node next;
        String name;
        public Node(String name) {
            this.name = name;
        }
    }

    /**
     * Returns the name of the middle node of linked list using one loop
     * @param head of the linked list
     * @return the name of the middle node
     */
    public static String middleNode(Node head) {
        Node curr = head;
        Node mid = head;
        int count = 0;
        while (curr != null){
            curr = curr.next;
            count++;
            if (count%2 == 0) mid = mid.next;
        }
        return mid.name;
    }

    /**
     * Determines if new message can be constructed with the letters from old message
     * @param newMessage message to be constructed
     * @param oldMessage message with letters to check
     * @return true if new message can be constructed, false otherwise
     */
    public static boolean canConstruct(String newMessage, String oldMessage) {
        int[] chars = new int[128];
        for (int i = 0; i < oldMessage.length(); i++) {
            chars[(int) oldMessage.charAt(i)]++;
        }
        for (int i = 0; i < newMessage.length(); i++) {
            if (chars[(int) newMessage.charAt(i)] == 0) return false;
            else chars[(int) newMessage.charAt(i)]--;
        }
        return true;
    }

    /**
     * Finds the k most occurring elements in buyers
     * @param buyers array to get elements from
     * @param k number of most occurring elements desired
     * @return string array of k most occurring elements in buyers
     */
    public static String[] frequentCustomers(String[] buyers, int k) {
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();
        for (int i = 0; i < buyers.length; i++) {
            if (map.containsKey(buyers[i])) map.put(buyers[i], map.get(buyers[i])+1);
            else map.put(buyers[i], 1);
        }

        PriorityQueue<Map.Entry<String, Integer>> queue = new PriorityQueue<>(
                (a, b) -> b.getValue() - a.getValue());
        queue.addAll(map.entrySet());

        String[] result = new String[k];
        for (int i = 0; i < k; i++) {
            result[i] = queue.poll().getKey();
        }

        return result;
    }
}
