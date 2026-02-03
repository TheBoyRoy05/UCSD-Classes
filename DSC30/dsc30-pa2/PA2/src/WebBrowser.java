import java.util.ArrayList;
import utilities.FullStackException;

/*
 * NAME: Issac Roy
 * PID: A17787465
 */

/**
 * Web Browser class which stores links to pages you've visited and allows you to move back and
 * forth between visited pages.
 *
 * @author Issac Roy
 * @since 04/12/24
 */
public class WebBrowser {

    private String currentPage;
    private ArrayList<String> history;
    private MyStack prev;
    private MyStack next;

    private static final String DEFAULT_PAGE = "google.com";
    private static final int STACK_CAPACITY = 100;

    /**
     * Constructor that initializes all the variables
     */
    public WebBrowser() {
        currentPage = DEFAULT_PAGE;
        history = new ArrayList<String>();
        prev = new MyStack(STACK_CAPACITY);
        next = new MyStack(STACK_CAPACITY);
    }

    /**
     * Gets the current page
     * @return the current page
     */
    public String getCurrentPage() {
        return currentPage;
    }

    /**
     * Opens a new page
     * @param newLink   link to the new page
     */
    public void openNewPage(String newLink) {
        prev.push(currentPage);
        currentPage = newLink;
        history.add(newLink);
    }

    /**
     * Set the current page to the previous page.
     * @throws IllegalStateException if there's no previous page
     */
    public void previousPage() throws IllegalStateException{
        if (prev.isEmpty()) throw new IllegalStateException();
        next.push(currentPage);
        currentPage = prev.pop();
        history.add(currentPage);
    }

    /**
     * Set the current page to the next page.
     * @throws IllegalStateException if there's no next page
     */
    public void nextPage() {
        if (next.isEmpty()) throw new IllegalStateException();
        prev.push(currentPage);
        currentPage = next.pop();
        history.add(currentPage);
    }

    /**
     * Opens a new tab, clearing the previous and next stacks
     */
    public void newTab() {
        prev.clear();
        next.clear();
        currentPage = DEFAULT_PAGE;
    }

    /**
     * Gets the history
     * @return the history
     */
    public ArrayList getHistory() {
        return history;
    }

    /**
     * Clears the history
     */
    public void clearHistory() {
        history.clear();
    }

    /**
     * Search history for link and open a new page if it exists
     * @return          true if link exists, false otherwise
     * @param link      The link to search for
     */
    public boolean findLink(String link) {
        if (history.contains(link)) {
            openNewPage(link);
            return true;
        }else{
            return false;
        }
    }
}
