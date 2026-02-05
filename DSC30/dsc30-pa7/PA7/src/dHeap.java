/*
 * Name: Issac Roy
 * PID:  A17787465
 */

import java.util.Arrays;
import java.util.NoSuchElementException;

/**
 * Title: dHeap Description: This program creates a Heap with d branching factor
 *
 * @author Issac Roy
 * @since 05/14/2024
 *
 * @param <T> the type of elements held in this collection
 */

public class dHeap<T extends Comparable<? super T>> implements HeapInterface<T> {

    private T[] heap;   // backing array
    private int d;      // branching factor
    private int nelems; // number of elements
    private boolean isMaxHeap; // indicates whether heap is max or min

    private int isMax;
    private static final int DEFAULT_SIZE = 10;

    /**
     * Initializes a binary max heap with capacity = 10
     */
    @SuppressWarnings("unchecked")
    public dHeap() {
        this(DEFAULT_SIZE);
    }

    /**
     * Initializes a binary max heap with a given initial capacity.
     *
     * @param heapSize The initial capacity of the heap.
     */
    @SuppressWarnings("unchecked")
    public dHeap(int heapSize) {
        this(2, heapSize, true);
    }

    /**
     * Initializes a d-ary heap (with a given value for d), with a given initial
     * capacity.
     *
     * @param d         The number of child nodes each node in the heap should have.
     * @param heapSize  The initial capacity of the heap.
     * @param isMaxHeap indicates whether the heap should be max or min
     * @throws IllegalArgumentException if d is less than one.
     */
    @SuppressWarnings("unchecked")
    public dHeap(int d, int heapSize, boolean isMaxHeap) throws IllegalArgumentException {
        if(d < 1) throw new IllegalArgumentException();
        this.d = d;
        heap = (T[]) new Comparable[heapSize];
        this.isMaxHeap = isMaxHeap;
        isMax = isMaxHeap ? 1 : -1;
        nelems = 0;
    }

    /**
     * Returns the size of the heap
     * @return the size of the heap
     */
    @Override
    public int size() {
        return nelems;
    }

    /**
     * Removes and returns the root element from the heap
     *
     * @return the root element from the heap
     * @throws NoSuchElementException if the heap is empty
     */
    @Override
    public T remove() throws NoSuchElementException {
        if (nelems == 0) throw new NoSuchElementException();
        T top = heap[0];
        heap[0] = heap[nelems-1];
        heap[nelems-1] = null;
        nelems--;
        if (nelems > 1) trickleDown(0);
        return top;
    }

    /**
     * Adds the given data to the heap
     *
     * @param item The element to add.
     * @throws NullPointerException if data is null
     */
    @Override
    public void add(T item) throws NullPointerException {
        if (item == null) throw new NullPointerException();
        if (heap.length == nelems) resize();
        heap[nelems] = item;
        bubbleUp(nelems);
        nelems++;
    }

    /**
     * Clear all elements in the heap
     */
    @SuppressWarnings("unchecked")
    @Override
    public void clear() {
        nelems = 0;
    }

    /**
     * Returns the root element from the heap
     *
     * @return the root element from the heap
     * @throws NoSuchElementException if the heap is empty
     */
    @Override
    public T element() throws NoSuchElementException {
        if (nelems == 0) throw new NoSuchElementException();
        return heap[0];
    }

    /**
     * Returns the index of the parent of the node at index
     * @param index index of child
     * @return index of parent, -1 if no parent
     */
    private int parent(int index) {
        return index == 0 ? -1 : (index - 1) / d;
    }

    /**
     * Bubble up the node at index to it's correct location to maintain the heap's structure
     * @param index of node to bubble up
     */
    private void bubbleUp(int index) {
        if (parent(index) < 0) return;
        if (heap[index].compareTo(heap[parent(index)]) == isMax){
            T temp = heap[index];
            heap[index] = heap[parent(index)];
            heap[parent(index)] = temp;
            bubbleUp(parent(index));
        }
    }

    /**
     * Trickle down the node at index to it's correct location to maintain the heap's structure
     * @param index of node to trickle down
     */
    private void trickleDown(int index) {
        int nextIdx = index;
        for (int i = Math.min(nelems, d*index+1); i <= Math.min(nelems, d*index+d); i++){
            if (heap[i] == null) break;
            if (heap[i].compareTo(heap[nextIdx]) == isMax) nextIdx = i;
        }
        if(nextIdx == index) return;
        T temp = heap[index];
        heap[index] = heap[nextIdx];
        heap[nextIdx] = temp;
        trickleDown(nextIdx);
    }

    /**
     * Doubles the size of the array before adding if it's full
     */
    @SuppressWarnings("unchecked")
    private void resize() {
        T[] newHeap = (T[]) new Comparable[nelems+nelems];
        for (int i = 0; i < nelems; i++) {
            newHeap[i] = heap[i];
        }
        heap = newHeap;
    }
}
