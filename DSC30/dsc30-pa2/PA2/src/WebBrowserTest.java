import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WebBrowserTest {

    @Test
    void browserTest1(){
        WebBrowser web = new WebBrowser();
        web.openNewPage("gradescope.com");
        assertEquals("gradescope.com", web.getCurrentPage());
        web.openNewPage("canvas.edu");
        assertEquals("canvas.edu", web.getCurrentPage());
        web.openNewPage("autograder.ucsd.edu");
        assertEquals("autograder.ucsd.edu", web.getCurrentPage());
        web.previousPage();
        assertEquals("canvas.edu", web.getCurrentPage());
        web.previousPage();
        assertEquals("gradescope.com", web.getCurrentPage());
        web.nextPage();
        assertEquals("canvas.edu", web.getCurrentPage());
        web.newTab();
        assertThrows(IllegalStateException.class, () -> {
            web.nextPage();
        });
        assertEquals(true, web.findLink("canvas.edu"));
        assertEquals("canvas.edu", web.getCurrentPage());
        String correctHistory = "[gradescope.com, canvas.edu, autograder.ucsd.edu, " +
                "canvas.edu, gradescope.com, canvas.edu, canvas.edu]";
        assertEquals(correctHistory, ""+web.getHistory());
        web.clearHistory();
    }

    @Test
    void browserTest2(){
        WebBrowser web = new WebBrowser();
        for (int i = 1; i < 10; i++){
            web.openNewPage("DSC"+i+"0.org");
        }
        assertEquals("DSC90.org", web.getCurrentPage());
        for (int i = 1; i < 9; i++){
            web.previousPage();
        }
        assertEquals("DSC10.org", web.getCurrentPage());
        web.nextPage();
        web.nextPage();
        assertEquals("DSC30.org", web.getCurrentPage());
        web.newTab();
        assertThrows(IllegalStateException.class, () -> {
            web.previousPage();
        });
        assertEquals(true, web.findLink("DSC20.org"));
        assertEquals("DSC20.org", web.getCurrentPage());
        web.clearHistory();
        assertEquals("[]", ""+web.getHistory());
    }

    @Test
    void browserTest3(){
        WebBrowser web = new WebBrowser();
        assertEquals(false, web.findLink("google.com"));
        assertEquals("google.com", web.getCurrentPage());
        web.openNewPage("");
        assertEquals("", web.getCurrentPage());
        web.previousPage();
        assertEquals("google.com", web.getCurrentPage());
        web.nextPage();
        assertEquals("", web.getCurrentPage());
        web.newTab();
        assertEquals("[, google.com, ]", ""+web.getHistory());
        web.clearHistory();
        web.openNewPage("bing.com");
        assertEquals("[bing.com]", ""+web.getHistory());
    }
}