package TestNG;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.testng.Assert;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;


public class CrossBrowserTestng {

    WebDriver driver;

    @Parameters("browser")
    @Test(priority = 1)
    public void launchbrowser(String br) {


        if (br.equals("chrome")) {
            WebDriverManager.chromedriver().setup();

            driver = new ChromeDriver();
        }
           /* else if(br.equals("firefox"))
            {
               WebDriverManager.firefoxdriver();
                driver=new FirefoxDriver();
            }*/
        else if (br.equals("ie")) {
            WebDriverManager.iedriver();
            driver = new InternetExplorerDriver();
        }

        driver.get("http://newtours.demoaut.com/");

    }

    @Test(priority = 2)
    public void verifyTitle() {

        Assert.assertEquals(driver.getTitle(), "Welcome: Mercury Tours");


    }

    @Test(priority = 3)
    public void registration() {

        Assert.assertTrue(true);
        //write code for registratio process
    }

    @Test(priority = 4)
    public void closeBrowser() {

        driver.close();
    }

}



