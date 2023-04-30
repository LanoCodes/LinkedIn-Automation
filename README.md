# LinkedIn Automation
This project is a further exploration of automation using selenium.


## Installation
1. Create a directory on your machine to house it. Something such as "LinkedInAutomation" should work
```commandline
mkdir LinkedInAutomation 
```
2. Look above and select "Code"
3. From here, copy HTTPS web URL
4. Return to your terminal and clone the repo.
```commandline
git clone https://github.com/LanoCodes/LinkedIn-Automation.git
```
5. Using your favorite IDE, open the LinkedInAutomation folder.
6. Navigate to main and run the program from there. You will need to make sure to have the following packages installed:
   1. selenium
   2. selenium.webdriver.chrome.service
   3. webdriver_manager.chrome
   4. selenium.webdriver.common.by
   5. selenium.webdriver.chrome.options
   6. time, os, random

## Usage
- Some prerequisites:
  - This project makes use of environment variables to help obscure the sensitive login information, so you will need to set your own for your LinkedIn username and password.
- As this is a more exploratory project, the functionality of the automation has been scoped to just saving the first job posting on LinkedIn that comes up when using the provided "url_linkedin".
- The URL provided is a job search configured to Atlanta area, within 25 miles, and only to jobs with LinkedIn's Easy Apply feature attached.
  - You can of course customize that search parameter to your liking, just be mindful to recapture that new URL before further runs of your code!