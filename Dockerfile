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
# Set volume for allure report files
VOLUME /allure_result
# Chrome browser and Allure dependency installation
# default-jre, default-jdk - for Allure, curl for downloading, rest of all - for Chrome browser
RUN apt-get update && apt-get install -y \
    default-jre \
    default-jdk \
    curl \
    software-properties-common \
    python3-launchpadlib \
    fonts-liberation \
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
    libvulkan1
# Chrome browser installation
RUN curl -LO  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb
# Check chrome version
RUN echo "Chrome: " && google-chrome --version
# Allure installation
RUN curl -o allure-commandline-2.23.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.23.0/allure-commandline-2.23.0.tgz
RUN tar -zxvf allure-commandline-2.23.0.tgz -C /opt/
RUN ln -s /opt/allure-2.23.0/bin/allure /usr/bin/allure
RUN rm -rf allure-commandline-2.23.0.tgz
# Copy and install requirements.txt
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy all project files in docker image
COPY . .
# Expose our port to the world
EXPOSE 9999
# Run tests and make Allure report
CMD ["sh", "-c", "pytest -s -v --alluredir=allure_result tests/ && allure serve --port 9999 allure_result"]
# Stub for debugging
#CMD ["tail", "-f", "/dev/null"]

