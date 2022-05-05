# python sample testing framework

Python-based automation framework for {HS} products

Instruction:
1. Clone the project from gitlab.
2. Install PyCharm
3. Import project
4. Run prepare_enviroment.bat file

Project structure
The project based on pytest testing framework. The framework has a libraries and classes which can test the Web UI,
 windows app and web REST API.
 Package base - in this package we have main class selenium_driver, base_page, base_api.
 
 Selenium_driver - In this calss implemented main seleium methods
 Base_page - In this class implemented comman method which can be used in all pages
 Base_api - In this class implemented the common methods for REST calls
 
The pages package - In this package add page classes for each page

Tests - Add test in test package

 