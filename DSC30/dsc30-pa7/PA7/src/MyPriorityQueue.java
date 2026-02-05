/*
 * Name: Issac Roy
 * PID:  A17787465
 */

import java.util.NoSuchElementException;

/**
 * Priority Queue Implementation using dHeap.
 *
 * @author Issac Roy
 * @since 05/21/2024
 *
 * @param <T> the type of elements held in this collection
 */

public class MyPriorityQueue<T extends Comparable<? super T>> {

    private dHeap<T> pQueue;
    private static final int DEFAULT_D = 4;

    /**
     * Constructor that creates a new priority queue
     *
     * @param initialSize the given size
     */
    public MyPriorityQueue(int initialSize) {
        pQueue = new dHeap<>(DEFAULT_D, initialSize, false);
    }

    /**
     * Inserts an element into the Priority Queue. The element received cannot be
     * null.
     *
     * @param element Element to be inserted.
     * @throws NullPointerException if the element received is null.
     * @return returns true
     */
    public boolean offer(T element) throws NullPointerException {
        if (element == null) throw new NullPointerException();
        pQueue.add(element);
        return true;
    }

    /**
     * Retrieve and remove the head of this Priority Queue (smallest element), or null if the
     * queue is empty.
     *
     * @return The head of the queue (smallest element), or null if queue is empty.
     */
    public T poll() {
        T data = null;
        try { data = pQueue.remove(); }
        catch (NoSuchElementException e) {}
        return data;
    }

    /**
     * Clears the contents of the queue
     */
    public void clear() {
        pQueue.clear();
    }

    /**
     * Retrieves, but does not remove, the head of this queue, or returns null if
     * this queue is empty.
     *
     * @return the head of the queue, null if the queue is empty
     */
    public T peek() {
        T data = null;
        try { data = pQueue.element(); }
        catch (NoSuchElementException e) {}
        return data;
    }

    /**
     * Returns true if the queue is empty, false otherwise
     * @return true if the queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return pQueue.size() == 0;
    }

}
