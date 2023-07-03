# Test Framework with Pytest and Page Object Model


Project Description: This project contains automation tests for a web application.


### Libraries

>pip install -r requirements.txt

### Running Tests
Make sure you have Chrome browser installed and running.
Run the tests using pytest by executing the following command terminal:

### Generating a report
> cd tests
> 
>pytest -sv --alluredir=allure_results
### *Viewing the report*
>allure serve C:\{path}\allure_results
___

### Project Structure
> pages/: *Contains page classes used for interacting with elements on web pages.*
> 
> tests/: *Contains test classes that perform various test scenarios.*
> 
> conftest.py: *File containing fixtures used in tests.*
> 
> requirements.txt: *File listing the dependencies.*



### Page Files
> base_page.py: *Base class for all pages, containing common methods and properties.*
> 
> forgot_password_page.py: *Forgot password page.*
> 
> login_page.py: *Login page.*
> 
> main_page.py: *Main page.*
> 
> registration_page.py: *Registration page.*

