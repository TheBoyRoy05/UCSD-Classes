/*
 * NAME: Issac Roy
 * PID: A17787465
 */

/**
 * Round Robin style task allocator
 *
 * @author Issac Roy
 * @since 04/22/2024
 */
public class RoundRobin {

    /* constants */
    private static final String TASKS_COMPLETED = "All tasks are already completed.";
    private static final int DEFAULT_QUANTUM = 4;

    /* instance variables */
    private MyQueue<Task> waitlist, finished;
    private int quantum, burstTime, waitTime;

    /**
     * This constructor will set the quantum to the default quantum of 4
     * @param toRun tasks to run
     */
    public RoundRobin(Task[] toRun) {
        this(DEFAULT_QUANTUM, toRun);
    }

    /**
     * Constructor to initialize all instance variables
     * @param quantum amount of time each task is allocated
     * @param toRun tasks to run
     * @throws IllegalArgumentException if quantum < 1 or if toRun is null or empty
     */
    public RoundRobin(int quantum, Task[] toRun) throws IllegalArgumentException{
        if (quantum < 1) throw new IllegalArgumentException();
        if (toRun == null || toRun.length == 0) throw new IllegalArgumentException();

        waitlist = new MyQueue<>();
        finished = new MyQueue<>();
        burstTime = waitTime = 0;
        this.quantum = quantum;

        for (int i = 0; i < toRun.length; i++){
            waitlist.enqueue(toRun[i]);
        }
    }

    /**
     * Runs all the tasks until completion
     * @return String with info about the completed tasks
     */
    public String runAllTasks() {
        if (waitlist.isEmpty()) return TASKS_COMPLETED;

        while (!waitlist.isEmpty()) {
            int size = waitlist.size();
            for (int i = 0; i < size; i++) {
                Task currTask = waitlist.dequeue();

                for (int j = 0; j < quantum; j++) {
                    burstTime++;
                    waitTime += waitlist.size();
                    currTask.runTask();
                    if (currTask.isFinished()) break;
                }

                if (currTask.isFinished()) finished.enqueue(currTask);
                else waitlist.enqueue(currTask);
            }
        }
        return "All tasks are run within " + burstTime + " units of burst time and "
                + waitTime + " units of wait time. The tasks are finished in this order:\\n"
                + finished.toString();
    }

    /**
     * Main method for testing.
     * @param args command-line arguments
     */
    public static void main(String[] args) {
        Task[] test1 = {new Task("A", 3), new Task("B", 4),
                        new Task("C", 4), new Task("D", 12),
                        new Task("E", 6), new Task("F", 3)};
        RoundRobin rr1 = new RoundRobin(3, test1);     // Quantum: 3, toRun: test1
        System.out.println(rr1.runAllTasks());   // Burst: 32, Wait: 86, Order: AFBCED
        System.out.println();
        System.out.println(rr1.runAllTasks());   // TASKS_COMPLETED
        System.out.println();

        Task[] test2 = {new Task("A", 9), new Task("B", 8),
                        new Task("C", 6), new Task("D", 4),
                        new Task("E", 4), new Task("F", 3)};
        RoundRobin rr2 = new RoundRobin(test2);  // Quantum: 4, toRun: test2
        System.out.println(rr2.runAllTasks());   // Burst: 34, Wait: 123, Order: DEFBCA
        System.out.println();
        System.out.println(rr2.runAllTasks());   // TASKS_COMPLETED
        System.out.println();

        Task[] test3 = {new Task("A", 7), new Task("B", 5),
                        new Task("C", 3), new Task("D", 1),
                        new Task("E", 2), new Task("F", 4),
                        new Task("G", 6), new Task("H", 8)};
        RoundRobin rr3 = new RoundRobin(3, test3);     // Quantum: 3, toRun: test3
        System.out.println(rr3.runAllTasks());   // Burst: 36, Wait: 148, Order: CDEBFGAH
        System.out.println();
        System.out.println(rr3.runAllTasks());   // TASKS_COMPLETED
        System.out.println();
    }
}
