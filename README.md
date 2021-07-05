# Web Automation Service
This service looks to navigate through the Nate Tech Challenge website, using a
Selenium WebDriver framework. The service makes use of Selenium's Python client
library which instructs the browser driver (chrome or firefox) to interact with
the relevant browser through a secure connection.

# Setting up environment locally:

```
python3 -m venv nate
source nate/bin/activate
pip install -r requirements.txt
```

# Running web automation locally:

```
python web_automation.py -d chrome
```

When running on a non-mac operating system, the relevant driver executable is required.
E.g the chrome driver can be found here: https://chromedriver.chromium.org/

# Running with docker

The docker-compose.yml is configured to run three services. The first two are remote WebDriver
clients (chrome and firefox respectively). The third service is set to run the app's web_automation.py script, configured to use the remote WebDrivers when navigating the site.

```
docker compose build
docker compose up
```
