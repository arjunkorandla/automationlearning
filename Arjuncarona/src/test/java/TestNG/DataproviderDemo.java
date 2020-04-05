package TestNG;


import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;


public class Dataprovier {
    WebDriver driver;

    @BeforClass
    void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
    }

    @Test(dataProvider = "users")
    void login(String uname, String pwd) {
        driver.get("http://newtours.demoaut.com/");
        driver.findElement(By.name("userName")).sendKeys(uname);
        driver.findElement(By.name("password")).sendKeys(pwd);
        driver.findElement(By.name("login")).click();
        driver.findElement(By.xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]")).click();

    }

    @DataProvider(name = "Users")
    Object[] loginDetails() {
        String data[][] = {{"mercury", "mercury"}, {"mer", "mer"}, {"mercury1", "mercury1"}};
        return data;
    }

    @AfterClass
    void close() {
        driver.close();
    }


}