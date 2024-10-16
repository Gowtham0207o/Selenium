from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


chrome_driver_path = r'C:\\chromedriver\\chromedriver\\chromedriver.exe'  


service = Service(chrome_driver_path)


driver = webdriver.Chrome(service=service)

with open('result.txt', 'w') as log_file:


    def test_successful_login(username, password):
        driver.get('https://analysis.selfmade.one/login.php') 
        time.sleep(2)  

        username_input = driver.find_element(By.NAME, 'email_id')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.NAME, 'submit')

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()
        
        time.sleep(2)  # Wait for the response

        try:
            welcome_message = driver.find_element(By.ID, 'welcomeMessage')  # Replace with actual element ID
            assert welcome_message.is_displayed(), "Login failed: Welcome message not displayed."
            log_file.write("Scenario 1: Successful Login - Login successful.\n")
        except Exception as e:
            log_file.write("Scenario 1: Successful Login - " + str(e) + "\n")


    # Function to test incorrect credentials
    def test_incorrect_credentials(username, password):
        driver.get('https://analysis.selfmade.one/login.php')  # Replace with your server URL
        time.sleep(2)  # Wait for the page to load

        username_input = driver.find_element(By.NAME, 'email_id')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.NAME, 'submit')

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()
        
        time.sleep(2)  # Wait for the response

        try:
            error_message = driver.find_element(By.ID, 'errorMessage')  # Replace with actual error message element ID
            assert error_message.is_displayed(), "Error message not displayed."
            log_file.write("Scenario 2: Incorrect Credentials - Login failed as expected.\n")
        except Exception as e:
            log_file.write("Scenario 2: Incorrect Credentials - " + str(e) + "\n")


    # Function to test empty credentials
    def test_empty_credentials():
        driver.get('https://analysis.selfmade.one/login.php')  # Replace with your server URL
        time.sleep(2)  # Wait for the page to load

        username_input = driver.find_element(By.NAME, 'email_id')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.NAME, 'submit')

        username_input.clear()
        password_input.clear()
        login_button.click()
        
        time.sleep(2)  # Wait for the response

        try:
            error_message = driver.find_element(By.ID, 'errorMessage')  # Replace with actual error message element ID
            assert error_message.is_displayed(), "Error message not displayed."
            log_file.write("Scenario 3: Empty Credentials - Login failed as expected.\n")
        except Exception as e:
            log_file.write("Scenario 3: Empty Credentials - " + str(e) + "\n")


    # Function to test slow response scenario
    def test_slow_response(username, password):
        driver.get('https://analysis.selfmade.one/login.php')  # Replace with your server URL
        time.sleep(2)  # Wait for the page to load

        username_input = driver.find_element(By.NAME, 'email_id')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.NAME, 'submit')

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        start_time = time.time()  # Record the start time
        login_button.click()  # Click the login button

        time.sleep(5)  # Adjust based on expected response time

        response_time = time.time() - start_time
        log_file.write(f"Scenario 4: Defect - Slow Response - Response Time: {response_time:.2f} seconds\n")

        if response_time > 3:
            log_file.write("Scenario 4: Slow Response - Login response time is too slow.\n")
        else:
            log_file.write("Scenario 4: Slow Response - Login response time is within acceptable limits.\n")


    # Run Test Scenarios
    log_file.write("Running Scenario 1: Successful Login\n")
    test_successful_login("admin@mail.me", "password")  # Replace with actual valid credentials

    log_file.write("\nRunning Scenario 2: Incorrect Credentials\n")
    test_incorrect_credentials("invalidUsername", "invalidPassword")  # Replace with actual invalid credentials

    log_file.write("\nRunning Scenario 3: Empty Credentials\n")
    test_empty_credentials()  # Test empty credentials

    log_file.write("\nRunning Scenario 4: Defect - Slow Response\n")
    test_slow_response("admin@mail.me", "password")  # Replace with actual valid credentials

# Close the browser
driver.quit()
