/*
 * Name: Issac Roy
 * PID: A17787465
 */

import java.util.*;

/**
 * Stack implementation with Linked List
 *
 * @author Issac Roy
 * @since 6/4/2024
 */

public class DonationStack {
    private class Node {
        public int data;
        public Node next;

        public Node(int data){
            this.data = data;
            next = null;
        }
    }

    private Node head;
    private Node max;

    public DonationStack() {
        head = null;
        max = null;
    }

    public void push(int val) {
        Node node = new Node(val);
        node.next = head;
        head = node;
        if (max == null || node.data > max.data) max = node;
    }

    public int peek() {
        return head.data;
    }

    public int pop() {
        int data = head.data;
        if (max.equals(head)) max = head.next;
        Node curr = max;
        while (curr != null && curr.next != null) {
            curr = curr.next;
            if (curr.data > max.data) max = curr;
        }
        head = head.next;
        return data;
    }

    public int max() {
        return max.data;
    }
}