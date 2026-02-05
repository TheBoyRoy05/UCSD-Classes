/*
 * Name: Issac Roy
 * PID:  A177787465
 */

import java.util.*;

/**
 * Binary search tree implementation.
 * 
 * @author Issac Roy
 * @since  05/10/24
 */
public class BSTree<T extends Comparable<? super T>> implements Iterable {

    /* * * * * BST Instance Variables * * * * */

    private int nelems; // number of elements stored
    private BSTNode root; // reference to root node

    /* * * * * BST Node Inner Class * * * * */
    /**
     * Binary Search Tree Node Class
     */
    protected class BSTNode {

        T key;
        LinkedList<T> dataList;
        BSTNode left;
        BSTNode right;

        /**
         * A constructor that initializes the BSTNode instance variables.
         *
         * @param left     Left child
         * @param right    Right child
         * @param dataList Linked list of related info
         * @param key      Node's key
         */
        public BSTNode(BSTNode left, BSTNode right, LinkedList<T> dataList, T key) {
            this.left = left;
            this.right = right;
            this.dataList = dataList;
            this.key = key;
        }

        /**
         * A constructor that initializes BSTNode variables. Note: This constructor is
         * used when you want to add a key with no related information yet. In this
         * case, you must create an empty LinkedList for the node.
         *
         * @param left  Left child
         * @param right Right child
         * @param key   Node's key
         */
        public BSTNode(BSTNode left, BSTNode right, T key) {
            this.left = left;
            this.right = right;
            this.dataList = new LinkedList<>();
            this.key = key;
        }

        /**
         * Return the key
         *
         * @return The key
         */
        public T getKey() {
            return key;
        }

        /**
         * Return the left child of the node
         *
         * @return The left child of the node
         */
        public BSTNode getLeft() {
            return left;
        }

        /**
         * Return the right child of the node
         *
         * @return The right child of the node
         */
        public BSTNode getRight() {
            return right;
        }

        /**
         * Return the linked list of the node
         *
         * @return The linked list of the node
         */
        public LinkedList<T> getDataList() {
            return dataList;
        }

        /**
         * Setter for left child of the node
         *
         * @param newleft New left child
         */
        public void setLeft(BSTNode newleft) {
            left = newleft;
        }

        /**
         * Setter for right child of the node
         *
         * @param newright New right child
         */
        public void setRight(BSTNode newright) {
            right = newright;
        }

        /**
         * Setter for the linked list of the node
         *
         * @param newData New linked list
         */
        public void setDataList(LinkedList<T> newData) {
            dataList = newData;
        }

        /**
         * Append new data to the end of the existing linked list of the node
         *
         * @param data New data to be appended
         */
        public void addNewInfo(T data) {
            dataList.add(data);
        }

        /**
         * Remove 'data' from the linked list of the node and return true. If the linked
         * list does not contain the value 'data', return false.
         *
         * @param data Info to be removed
         * @return True if data was found, false otherwise
         */
        public boolean removeInfo(T data) {
            return dataList.remove(data);
        }
    }

    /* * * * * BST Methods * * * * */

    /**
     * 0-arg constructor that initializes root to null and nelems to 0
     */
    public BSTree() {
        root = null;
        nelems = 0;
    }

    /**
     * Return the root of BSTree. Returns null if the tree is empty
     *
     * @return The root of BSTree, null if the tree is empty
     */
    public BSTNode getRoot() {
        return root;
    }

    /**
     * Return the BST size
     *
     * @return The BST size
     */
    public int getSize() {
        return nelems;
    }

    /**
     * Helper method for recursion
     *
     * @param curr current node
     * @param key to look for
     * @param addKey whether curr or null should be return if key is found
     * @return curr if key is found and insert is false or if key is not found and insert is true,
     * false otherwise
     */
    private BSTNode recurse(BSTNode curr, T key, boolean addKey){
        int value = key.compareTo(curr.getKey());
        if (value < 0) {
            if (curr.getLeft() == null) return addKey ? curr : null;
            else return recurse(curr.getLeft(), key, addKey);
        } else if (value > 0) {
            if (curr.getRight() == null) return addKey ? curr : null;
            else return recurse(curr.getRight(), key, addKey);
        } else return addKey ? null : curr;
    }

    /**
     * Insert a key into BST
     *
     * @param key to be added
     * @return true if insertion is successful and false otherwise
     * @throws NullPointerException if key is null
     */
    public boolean insert(T key) throws NullPointerException{
        if (key == null) throw new NullPointerException();

        if (root == null) root = new BSTNode(null, null, key);
        else {
            BSTNode node = recurse(root, key, true);
            if (node == null) return false;
            if (key.compareTo(node.getKey()) < 0) {
                node.setLeft(new BSTNode(null, null, key));
            } else {
                node.setRight(new BSTNode(null, null, key));
            }
        }

        nelems++;
        return true;
    }

    /**
     * Return true if the 'key' is found in the tree, false otherwise
     *
     * @param key To be searched
     * @return True if the 'key' is found, false otherwise
     * @throws NullPointerException If key is null
     */
    public boolean findKey(T key) throws NullPointerException{
        if (key == null) throw new NullPointerException();
        if (root == null) return false;
        return recurse(root, key, false) != null;
    }

    /**
     * Insert 'data' into the LinkedList of the node whose key is 'key'
     *
     * @param key  Target key
     * @param data To be added to key's LinkedList
     * @throws NullPointerException     If either key or data is null
     * @throws IllegalArgumentException If key is not found in the BST
     */
    public void insertData(T key, T data) throws NullPointerException, IllegalArgumentException{
        if (key == null || data == null) throw new NullPointerException();
        if (root == null) throw new IllegalArgumentException();
        BSTNode node = recurse(root, key, false);
        if (node == null) throw new IllegalArgumentException();

        node.addNewInfo(data);
    }

    /**
     * Return the LinkedList of the node with key value 'key'
     *
     * @param key Target key
     * @return LinkedList of the node whose key value is 'key'
     * @throws NullPointerException     If key is null
     * @throws IllegalArgumentException If key is not found in the BST
     */
    public LinkedList<T> findDataList(T key) throws NullPointerException, IllegalArgumentException{
        if (key == null) throw new NullPointerException();
        if (root == null) throw new IllegalArgumentException();
        BSTNode node = recurse(root, key, false);
        if (node == null) throw new IllegalArgumentException();

        return node.getDataList();
    }

    /**
     * Return the height of the tree
     *
     * @return The height of the tree, -1 if BST is empty
     */
    public int findHeight() {
        return findHeightHelper(root);
    }

    /**
     * Helper for the findHeight method
     *
     * @param root Root node
     * @return The height of the tree, -1 if BST is empty
     */
    private int findHeightHelper(BSTNode root) {
        if (root == null) return -1;
        int leftHeight = findHeightHelper(root.getLeft());
        int rightHeight = findHeightHelper(root.getRight());
        return 1 + Math.max(leftHeight, rightHeight);
    }

    /* * * * * BST Iterator * * * * */
    /**
     * Binary Search Tree Iterator Class
     */
    public class BSTree_Iterator implements Iterator<T> {
        public Stack<BSTNode> path;

        /**
         * Constructor for Binary Search Tree Iterator
         */
        public BSTree_Iterator() {
            path = new Stack<>();
            BSTNode curr = getRoot();
            while (curr != null){
                path.push(curr);
                curr = curr.getLeft();
            }
        }

        /**
         * Returns if the iterator has a next element or not
         *
         * @return true if the iterator has a next element, false otherwise
         */
        public boolean hasNext() {
            return !path.empty();
        }

        /**
         * Returns the next in-order element of the tree
         *
         * @return the next in-order element of the tree
         * @throws NoSuchElementException if there is no next element
         */
        public T next() throws NoSuchElementException{
            if (!hasNext()) throw new NoSuchElementException();
            BSTNode node = path.pop();
            BSTNode curr = node.getRight();
            while (curr != null){
                path.push(curr);
                curr = curr.getLeft();
            }
            return node.getKey();
        }
    }

    /**
     * Creates an iterator object
     *
     * @return Binary Search Tree Iterator
     */
    public Iterator<T> iterator() {
        return new BSTree_Iterator();
    }

    /* * * * * Extra Credit Methods * * * * */

    /**
     * Finds the intersection of two trees
     *
     * @param iter1 iterator for first tree
     * @param iter2 iterator for second tree
     * @return      arraylist containing all shared keys in order
     */
    public ArrayList<T> intersection(Iterator<T> iter1, Iterator<T> iter2) {
        ArrayList<T> arr1 = new ArrayList<>();
        ArrayList<T> arr2 = new ArrayList<>();
        while (iter1.hasNext()) arr1.add(iter1.next());
        while (iter2.hasNext()) arr2.add(iter2.next());

        ArrayList<T> out = new ArrayList<>();
        for (int i = 0; i < arr1.size(); i++) {
            if (arr2.contains(arr1.get(i))) out.add(arr1.get(i));
        }
        return out;
    }

    /**
     * Finds the largest key at any level
     *
     * @param level level to check for largest
     * @return      largest key at level
     */
    public T levelMax(int level) {
        BSTNode node = levelMaxHelper(root, level);
        return node == null ? null : node.getKey();
    }

    /**
     * Helper function for levelMax
     *
     * @param curr  current node
     * @param level level to check
     * @return      node with the greatest value at level
     */
    private BSTNode levelMaxHelper(BSTNode curr, int level){
        if (level == 0 || curr == null) return curr;
        else{
            BSTNode node = levelMaxHelper(curr.getRight(), level-1);
            if (node != null) return node;
            else return levelMaxHelper(curr.getLeft(), level-1);
        }
    }
}
