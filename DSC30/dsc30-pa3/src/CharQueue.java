import java.util.NoSuchElementException;

/*
    Name: Issac Roy
    PID:  A17787465
 */

/**
 * Implementation of Queue that stores characters only
 *
 * @author Issac Roy
 * @since 4/16/2024
 */

public class CharQueue {
    /* instance variables, feel free to add more if you need */
    private char[] circularArray;
    private int length;
    private int front;
    private int rear;

    private static final int DEFAULT_CAPACITY = 5;
    /**
    * Creates a new queue with an initial capacity of 5
    */
    public CharQueue() {
        this(DEFAULT_CAPACITY);
    }

    /**
     * Creates a new queue with the specified capacity
     * @throws IllegalArgumentException if capacity is non-positive
     * @param capacity     initial capacity of queue
     */
    public CharQueue(int capacity) {
        if (capacity < 1) throw new IllegalArgumentException();
        this.front = 0;
        this.rear = 0;
        this.length = capacity;
        this.circularArray = new char[capacity];
    }

    /**
     * Checks if the queue is empty
     * @return true if the queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return front == rear;
    }

    /**
     * Returns the number of elements currently stored in the queue
     * @return the number of elements currently stored in the queue
     */
    public int size() {
        if (rear - front >= 0) return rear - front;
        else return rear + length - front;
    }

    /**
     * Clears all the elements in the queue
     */
    public void clear() {
        front = 0;
        rear = 0;
    }

    /**
     * Adds a new elem to the back of the queue
     * Double the capacity of the queue when adding the elem to a full queue
     * @param elem      Element to be added to the queue
     */
    public void enqueue(char elem) {
        circularArray[rear] = elem;
        rear = (rear+1)%length;
        if (rear == front){
            int newLength = length+length;
            char[] newArray = new char[newLength];
            for (int i = 0; i < length; i++){
                newArray[i] = circularArray[(front+i)%length];
            }
            circularArray = newArray;
            front = 0;
            rear = length;
            length = newLength;
        }
    }

    /**
     * Returns the element at the front of the queue
     * @throws NoSuchElementException if the queue is empty
     * @return the element at the front of the queue
     */
    public char peek() {
        if (isEmpty()) throw new NoSuchElementException();
        return circularArray[front];
    }

    /**
     * Returns and removes the element at the front of the queue
     * @throws NoSuchElementException if the queue is empty
     * @return the element at the front of the queue
     */
    public char dequeue() {
        if (isEmpty()) throw new NoSuchElementException();
        char out = circularArray[front];
        front++;
        return out;
    }
}
