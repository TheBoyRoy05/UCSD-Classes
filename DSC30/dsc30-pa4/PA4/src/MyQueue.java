/*
 * NAME: Issac Roy
 * PID: A17787465
 */

/**
 * Queue implementation using doubly linked lists
 *
 * @author Issac Roy
 * @since 04/22/2024
 */
public class MyQueue<T> {
    
    private DoublyLinkedList<T> list;

    private static final int TO_STRING_PADDING = 11;
    /**
     * Initialize the instance variables of this queue.
     */
    public MyQueue() {
        list = new DoublyLinkedList<T>();
    }

    /**
     * Return true if a queue is empty, false otherwise
     * @return true if a queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return list.isEmpty();
    }

    /**
     * Return the number of elements currently stored in a queue
     * @return the number of elements stored in a queue
     */
    public int size() {
        return list.size();
    }

    /**
     * Add the given data to the back of the queue
     * @param data data to be queued
     * @throws IllegalArgumentException if data is null
     */
    public void enqueue(T data) throws IllegalArgumentException{
        if (data == null) throw new IllegalArgumentException();
        list.add(data);
    }

    /**
     * Returns and removes the element at the front of the queue or null if the queue is empty
     * @return the element at the front of the queue or null if the queue is empty
     */
    public T dequeue() {
        if (list.isEmpty()) return null;
        else return list.remove(0);
    }

    /**
     * Returns the element at the front of the queue or null if the queue is empty
     * @return the element at the front of the queue or null if the queue is empty
     */
    public T peek() {
        if (list.isEmpty()) return null;
        else return list.get(0);
    }

    /**
     * Returns a String representation of the queue
     * @return a String representation of the queue
     */
    @Override
    public String toString(){
        String str = list.toString();
        if (list.isEmpty()) return "[]";
        else return "[" + str.substring(TO_STRING_PADDING, str.length()-TO_STRING_PADDING) + "]";
    }
}
