package grid1; 
import java.net.URL; 
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.firefox.FirefoxOptions; 
import org.openqa.selenium.remote.RemoteWebDriver; 
public class Grid2 { 
public static void main(String[] args) { 
try { 
 
URL gridURL = new URL("http://localhost:4444"); 
 
FirefoxOptions options = new FirefoxOptions(); 
 
WebDriver driver = new RemoteWebDriver(gridURL, options); 
 
driver.get("https://www.google.com"); 
 
System.out.println("Page Title: " + driver.getTitle()); 
 
driver.manage().window().maximize(); 
 
Thread.sleep(5000); 
 
driver.quit(); 
} catch (Exception e) { 
e.printStackTrace(); 
} 
} 
}