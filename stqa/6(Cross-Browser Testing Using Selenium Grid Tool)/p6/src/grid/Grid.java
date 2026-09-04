package grid; 
import java.net.URL; 
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.chrome.ChromeOptions; 
import org.openqa.selenium.firefox.FirefoxOptions; 
import org.openqa.selenium.edge.EdgeOptions; 
import org.openqa.selenium.remote.RemoteWebDriver; 
public class Grid { 
public static void main(String[] args) throws Exception { 
String[] browsers = {"chrome", "firefox", "edge"}; 
for (String browser : browsers) { 
WebDriver driver; 
if (browser.equals("chrome")) 
driver = new RemoteWebDriver( 
new URL("http://localhost:4444"), 
new ChromeOptions()); 
else if (browser.equals("firefox")) 
driver = new RemoteWebDriver( 
new URL("http://localhost:4444"), 
new FirefoxOptions()); 
else 
driver = new RemoteWebDriver( 
new URL("http://localhost:4444"), 
new EdgeOptions()); 
long start = System.currentTimeMillis(); 
driver.get("https://www.selenium.dev/"); 
System.out.println(browser + " : " + driver.getTitle()); 
long time = System.currentTimeMillis() - start; 
System.out.println("Time: " + time + " ms"); 
driver.quit(); 
} 
} 
}