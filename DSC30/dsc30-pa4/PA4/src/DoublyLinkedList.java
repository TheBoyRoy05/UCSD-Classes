/*
 * NAME: Issac Roy
 * PID: A17787465
 */

import java.util.AbstractList;

/**
 * Doubly linked list for generics
 *
 * @author Issac Roy
 * @since 04/22/2024
 */
public class DoublyLinkedList<T> extends AbstractList<T> {

    /* DLL instance variables */
    private int size;
    private Node head;
    private Node tail;

    /**
     * Node for chaining together to create a linked list
     */
    protected class Node {

        /* Node instance variables */
        T data;
        Node next;
        Node prev;

        /**
         * Constructor to create singleton Node
         *
         * @param element element to be stored in the Node
         */
        private Node(T element) {
            data = element;
        }

        /**
         * Constructor to create singleton link it between previous and next
         *
         * @param element  Element to add, can be null
         * @param nextNode successor Node, can be null
         * @param prevNode predecessor Node, can be null
         */
        private Node(T element, Node nextNode, Node prevNode) {
            data = element;
            next = nextNode;
            prev = prevNode;
        }

        /**
         * Set the element
         *
         * @param element new element
         */
        public void setElement(T element) {
            data = element;
        }

        /**
         * Accessor to get the Nodes Element
         *
         * @return the data
         */
        public T getElement() {
            return data;
        }

        /**
         * Set the next node in the list
         *
         * @param n new next node
         */
        public void setNext(Node n) {
            next = n;
        }

        /**
         * Get the next node in the list
         *
         * @return the successor node
         */
        public Node getNext() {
            return next;
        }

        /**
         * Set the previous node in the list
         *
         * @param p new previous node
         */
        public void setPrev(Node p) {
            prev = p;
        }


        /**
         * Accessor to get the prev Node in the list
         *
         * @return predecessor node
         */
        public Node getPrev() {
            return prev;
        }

        /**
         * Remove this node from the list.
         * Update previous and next nodes
         */
        public void remove() {
            prev.setNext(next);
            next.setPrev(prev);
        }
    }

    /**
     * Creates a new, empty doubly-linked list.
     */
    public DoublyLinkedList() {
        head = new Node(null);
        tail = new Node(null);
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    /**
     * Add an element to the end of the list
     *
     * @param element data to be added
     * @return true if the element was added, false otherwise
     * @throws NullPointerException if data received is null
     */
    @Override
    public boolean add(T element) throws NullPointerException {
        // implementation of adding the new data
        if (element == null) throw new NullPointerException();
        Node newNode = new Node(element, tail, tail.prev);
        tail.prev.next = newNode;
        tail.prev = newNode;
        size++;
        return true;
    }


    /**
     * Adds an element to a certain index in the list, shifting exist elements
     * create room. Does not accept null values.
     *
     * @param index index to add the data at
     * @param element data to be added to the list
     * @throws IndexOutOfBoundsException index is outside the range [0, size]
     * @throws NullPointerException if data received is null
     */
    @Override
    public void add(int index, T element)
            throws IndexOutOfBoundsException, NullPointerException {
        if (element == null) throw new NullPointerException();
        if (index < 0 || index > size) throw new IndexOutOfBoundsException();
        Node curr = getNth(index);
        Node newNode = new Node(element, curr, curr.prev);
        curr.prev.next = newNode;
        curr.prev = newNode;
        size++;
    }

    /**
     * Clear the linked list
     */
    @Override
    public void clear() {
        head.next = tail;
        tail.prev = head;
        size = 0;
    }

    /**
     * Determine if the list contains the data element anywhere in the list.
     *
     * @param element the data to check is in the list or not
     * @return true if the list contains the element, false otherwise
     */
    @Override
    public boolean contains(Object element) {
        T data = (T) element;
        Node curr = head;
        for (int i = 0; i < size; i++){
            curr = curr.next;
            if (curr.data == data) return true;
        }
        return false;
    }

    /**
     * Retrieves the element stored with a given index on the list.
     *
     * @param index index to add the data at
     * @return the data at the given index
     * @throws IndexOutOfBoundsException index is outside the range [0, size-1]
     */
    @Override
    public T get(int index) throws IndexOutOfBoundsException {
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();
        return getNth(index).data;
    }

    /**
     * Helper method to get the Nth node in our list
     *
     * @param index index to add the data at
     * @return Node at the given index
     */
    private Node getNth(int index) {
        Node curr = head.next;
        for (int i = 0; i < index; i++){
            curr = curr.next;
        }
        return curr;
    }

    /**
     * Determine if the list empty
     *
     * @return true if the list contains no elements, false otherwise
     */
    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Remove the element from position index in the list
     *
     * @param index the index of the element to be removed
     * @return the data from the removed element
     * @throws IndexOutOfBoundsException if index is outside the range [0, size-1]
     */
    @Override
    public T remove(int index) throws IndexOutOfBoundsException {
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();

        Node curr = getNth(index);
        curr.remove();
        size--;
        return curr.data;
    }

    /**
     * Set the value of an element at a certain index in the list.
     *
     * @param index index of the element to replace
     * @param element element to be stored at the specified position
     * @return the previous data at the specified position
     * @throws IndexOutOfBoundsException index is outside the range [0, size-1]
     * @throws NullPointerException if data received is null
     */
    @Override
    public T set(int index, T element)
            throws IndexOutOfBoundsException, NullPointerException {
        if (element == null) throw new NullPointerException();
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();

        Node curr = getNth(index);
        T data = curr.data;
        curr.setElement(element);
        return data;
    }

    /**
     * Retrieves the amount of elements that are currently on the list.
     *
     * @return the size of the list
     */
    @Override
    public int size() {
        return size;
    }

    /**
     * String representation of this list in the form of:
     * "[(head) -> elem1 -> elem2 -> ... -> elemN -> (tail)]"
     *
     * @return string representation of this list
     */
    @Override
    public String toString() {
        Node curr = head;
        String out = "[(head) -> ";
        for (int i = 0; i < size; i++){
            curr = curr.next;
            out += curr.data + " -> ";
        }
        out += "(tail)]";
        return out;
    }

    /* ==================== EXTRA CREDIT ==================== */

    /**
     * Mimic Python list slicing, modify list in place
     *
     * @param start index to start slicing
     * @param end index to end slicing
     * @param step includes every step amount of elements from the start
     * @throws IllegalArgumentException if start < 0, end < 0, or step < 1
     */
    public void slice(int start, int end, int step) throws IllegalArgumentException{
        if (start < 0 || end < 0 || step < 1) throw new IllegalArgumentException();

        if (start >= size || start > end){
            head.next = tail;
            tail.prev = head;
            size = 0;
            return;
        }

        Node curr = getNth(start);
        Node prev = curr;
        head.next = curr;
        curr.prev = head;

        int listSize = size;
        size = 1;

        for (int i = 0; i < Math.min(listSize, end)-start; i++){
            if (i%step == 0 && i != 0){
                prev.next = curr;
                curr.prev = prev;
                prev = curr;
                size++;
            }
            curr = curr.next;
        }

        prev.next = tail;
        tail.prev = prev;
    }

    /**
     * Recursively swaps halves of list for n recursive layers
     *
     * @param n number of iterations
     * @param start index to begin swapping
     * @param end index to end swapping
     * @throws IllegalArgumentException n is less than 0
     * @throws IllegalArgumentException list can't be recursively split into equal halves n times
     */
    public void swapHalves(int n, int start, int end) throws IllegalArgumentException{
        if (size % Math.pow(2, n) != 0 || n < 0) throw new IllegalArgumentException();
        if (n == 0) return;

        int middle = (start + end)/2;
        Node firstNode = getNth(start);
        Node lastNode = getNth(end);
        Node middleNode = getNth(middle);

        firstNode.prev.next = middleNode.next;
        middleNode.next.prev = firstNode.prev;

        middleNode.next = lastNode.next;
        lastNode.next.prev = middleNode;

        lastNode.next = firstNode;
        firstNode.prev = lastNode;

        swapHalves(n-1, start, middle);
        swapHalves(n-1, middle+1, end);
    }
}
