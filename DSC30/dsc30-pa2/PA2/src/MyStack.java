import java.util.EmptyStackException;
import utilities.FullStackException;

/*
 * NAME: Issac Roy
 * PID: A17787465
 */

/**
 * Custom Stack implementation using arrays
 *
 * @author Issac Roy
 * @since 04/10/24
 */
public class MyStack {
    private String[] stack;
    private int top;
    private int capacity;

    private static final int DEFAULT_CAPACITY = 10;

    /**
    * Constructor that initializes a stack with the given initial capacity.
    * @throws IllegalArgumentException  if capacity is out of valid range (i.e. less than 1)
    * @param capacity       max number of elements that the stack can contain
    * */
    public MyStack(int capacity) throws IllegalArgumentException {
        if (capacity < 1) {
            throw new IllegalArgumentException();
        }
        this.capacity = capacity;
        this.top = 0;
        stack = new String[capacity];
    }

    /**
     * Default constructor that initializes capacity as 10
     * */
    public MyStack() {
        this.capacity = DEFAULT_CAPACITY;
        this.top = 0;
        stack = new String[capacity];
    }

    /**
     * Checks if the stack is empty
     * @return      true if empty, false otherwise
     * */
    public boolean isEmpty() {
        return top == 0;
    }

    /**
     * Clears all elements in the stack
     * */
    public void clear() {
        top = 0;
        stack = new String[capacity];
    }

    /**
     * Returns the number of elements currently stored in the stack
     * @return      the number of elements in the stack
     * */
    public int size() {
        return top;
    }

    /**
     * Returns the maximum number of elements the stack can store
     * @return      the maximum number of elements the stack can store
     * */
    public int capacity() {
        return capacity;
    }

    /**
     * Returns the top element of the stack
     * @throws EmptyStackException if the stack is empty
     * @return      the top element of the stack
     * */
    public String peek() throws EmptyStackException {
        if (top == 0) {
            throw new EmptyStackException();
        }
        return stack[top-1];
    }

    /**
     * Pushes the given element to the stack
     * @throws FullStackException if the stack reaches full capacity
     * @throws IllegalArgumentException if element is null
     * @param element   the element to be added
     * */
    public void push(String element) throws FullStackException, IllegalArgumentException{
        if (top >= capacity){
            throw new FullStackException("Your stack is full");
        }
        if (element == null){
            throw new IllegalArgumentException();
        }
        stack[top] = element;
        top++;
    }

    /**
     * Returns and removes the top element of the stack
     * @throws EmptyStackException if the stack is empty
     * @return      the top element of the stack
     * */
    public String pop() throws EmptyStackException{
        if (top == 0){
            throw new EmptyStackException();
        }
        top--;
        String popped = stack[top];
        stack[top] = null;
        return popped;
    }

    /**
     * Pushes all strings in the array elements to the stack.
     * @throws FullStackException once stack reaches full capacity.
     * @throws IllegalArgumentException if elements is null
     * @param elements      the elements to be added (they are added in order)
     * */
    public void multiPush(String[] elements) throws FullStackException, IllegalArgumentException {
        if (elements == null){
            throw new IllegalArgumentException();
        }
        for (int i = 0; i < elements.length; i++){
            push(elements[i]);
        }
    }

    /**
     * Pops up to the given amount of elements from the stack
     * @throws IllegalArgumentException if amount is not a positive number
     * @param amount        The number of elements to be popped
     * @return              String array that contains all popped elements
     * */
    public String[] multiPop(int amount) throws IllegalArgumentException {
        if (amount < 1){
            throw new IllegalArgumentException();
        }
        int removeAmount = Math.min(amount, top);
        String[] out = new String[removeAmount];
        for (int i = 0; i < removeAmount; i++){
            out[i] = pop();
        }
        return out;
    }
}
