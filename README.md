# StroyremAutomation

Правила работы с GIT
#Несколько маркеров
#Потоки 
#запуск тестов на проде и на stage


### Запуск тестов в Docker
- ```docker build -t stroyremautomation:0.0.1 .```
- ```docker run -p 9999:9999 stroyremautomation:0.0.1```  

После формирования отчета Allure он доступен на http://localhost:9999/  
Также отчет Allure можно скопировать из контейнера и сформировать на хосте: 
- `````$CONTAINER_ID = (docker ps -a -q | Select-Object -First 1)`````
- ```docker cp ${CONTAINER_ID}:/app/allure_result .```
- ```allure serve .\allure_result  ```

Для открытия bash контейнера используйте:
- ```docker ps```
- ```docker exec -it ИМЯ_ИЛИ_ID_КОНТЕЙНЕРА bash ```
- ```exit```

[![Allure-report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://victoretc.github.io/StroyremAutomation/)

