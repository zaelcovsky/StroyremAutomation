# Using Debian 12.0 Slim official image
FROM python:3.11-slim-bookworm
# This flag is important to output python logs correctly in docker
ENV PYTHONUNBUFFERED=1
# Flag to optimize container size a bit by removing runtime python cache
ENV PYTHONDONTWRITEBYTECODE=1
# Flag to run needed webdriver with options
ENV DOCKERRUN=1

# Set working directore for our project
WORKDIR /app
# Chrome browser and Allure dependency installation
# default-jre, default-jdk - for Allure, curl for downloading, rest of all - for Chrome browser
RUN apt-get update && apt-get install -y \
    default-jre \
    default-jdk \
    curl \
    software-properties-common \
    python3-launchpadlib \
    fonts-liberation \
    jq \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json' \
    | jq -r '.channels.Stable.downloads|.chrome,.chromedriver|.[]|select(.platform=="linux64").url|"curl -LO \(.)"' \
    | bash \
    && unzip -d /usr/local/share 'chrome-linux64.zip' \
    && ln -s /usr/local/share/chrome-linux64/chrome /usr/bin/chrome \
    && unzip -d /usr/local/share 'chromedriver-linux64.zip' \
    && ln -s /usr/local/share/chromedriver-linux64/chromedriver /usr/bin/chromedriver \
    && rm 'chrome-linux64.zip' && rm 'chromedriver-linux64.zip'

# Check chrome version
RUN echo -e "Chrome: $(chrome --version) \nChromedriver: $(chromedriver --version) "

# Allure installation
RUN curl -o allure-commandline-2.23.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.23.0/allure-commandline-2.23.0.tgz \
    && tar -zxvf allure-commandline-2.23.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.23.0/bin/allure /usr/bin/allure \
    && rm -rf allure-commandline-2.23.0.tgz
# Copy and install requirements.txt
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy all project files in docker image
COPY . .
# Set volume for allure report files
# VOLUME /allure_result
# Expose our port to the world
EXPOSE 9999
# Run tests and make Allure report
CMD ["sh", "-c", "pytest -s -v --alluredir=allure_result tests/ && allure serve --port 9999 allure_result"]
# Stub for debugging
#CMD ["tail", "-f", "/dev/null"]
