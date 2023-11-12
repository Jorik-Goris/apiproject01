# API basisproject Jorik Goris (r0901062 CCS02)

Dit project bevat het basisproject van API Development.

## Documentation

Deze github repository bevat alle nodige bestanden om dit project op te zetten.

### .github/workflows/docker-build.yml
Dit bestand configureert onze github pipeline.

### README.md ##
Documentatie

### docker-compose.yml ##
Configureert onze docker containers, API en MySQL.

### dockerfile ##
Gebruikt files in /app om onze container image te builden.

### requirements.txt ##
Definieert dependencies.

## app/.env ##
Bevat environment variables, API key voor openweather API in dit geval.

## app/__init__.py ##
Zorgt ervoor dat bestanden als package worden gezien.

## app/crud.py ##
Bevat onze database CRUD acties.

## app/database.py ##
Configureert onze database URL, voor MySQL in dit geval.

## app/main.py ##
Bevat onze API zelf.

## app/models.py ##
Bevat onze database models.

## app/schemas.py  ##
Bevat Pydantic models.

Een github action pipeline zal gewijzigde bestanden in de main branch automatisch detecteren en de docker image rebuilden, waarna deze op dockerhub wordt gepushed.

Okteto cloud zal de docker-compose.yml file gaan gebruiken om de docker images te pullen en op te zetten.

Deze API bevat vijf endpoints; 3 GET endpoints, één POST en één DELETE endpoint. 

De eerste twee GET endpoints maken gebruik van de openweather API. Deze 'consumen' als het waar een andere API. 

Met de endpoints /weather/{city} en /forecast/{city} kan je het weer of de weersvoorspelling voor een bepaalde stand ophalen.

Deze endpoints zullen op hun beurt een GET request doen op de openweather API. 

De andere 3 endpoints dienen om zelf weerdata te posten, meerbepaald de stad, temperatuur, condities en of er op dat moment neerslag valt.

Deze data kan je in een JSON body posten, ophalen en verwijderen. De data wordt opgeslagen in een mysql database.

Om de API te gebruiken heb je een API key nodig, die geprogrammeerd staan in de main.py file.


## Github actions

Volgende Github action workfile gaat onze pipeline opzetten.
Deze pipeline gaat de huidige repository gebruiken om een docker image van te builden, en deze te pushen naar de docker hub. 
Om dit te doen maakt hij gebruik van een docker hub authentication token en de requirements.txt file om enkele dependencies te installeren.

![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/2cf8eaf6-483f-43a2-9a69-e889bb66b784)

## Expected result 

![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/04f56cad-d15c-4890-be24-873cf30e4f81)



## Resultaat Okteto Cloud
Verbind Okteto Cloud met je github repository.
Deploy daarna in je Dev environment, waarop Okteto de docker-compose.yml file gaat gebruiken om je docker containers op te zetten. Deze docker containers zijn gebuild door je github pipeline.

![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/89e80cd2-7e8c-45e8-ba68-084ba3d4008f)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/f6b57184-2885-4ba6-b02d-edf04945eb69)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/08964244-892a-42bf-afa1-96779b67cc9a)


## Resultaat Postman

Openweather API:

![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/e436c7dd-c348-4add-b312-b5951cf68f14)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/1ff1ba74-c7ea-4729-a506-b4cff2f5ff7b)

API:

## POST 
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/89bf3fd5-43cb-4ff1-92a4-d0da49ae3a80)

## GET 
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/e2b636f2-2139-40eb-9946-0aedc8da26a5)

## DELETE 
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/4708d573-1f2c-40c4-b6bc-50df492a94c9)


## FastAPI - Swagger UI
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/15b7e5a2-f8ab-46c0-a9f4-dea002fc0af9)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/672488dc-5bf5-4587-a187-c668e5984b8f)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/fed7f037-319c-4bdd-80cb-1a9a08afded7)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/0001d6d2-5190-44d2-b150-28a133e11f5f)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/1863a680-4603-4ac1-818b-cf67d5220fa2)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/71b4a57b-4e2a-4b11-8921-f8f9c9cf519d)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/07d1811c-e37b-4485-a480-f12e5316cf69)
![image](https://github.com/Jorik-Goris/apiproject01/assets/95848835/885864ed-f951-4390-9b88-03e1a495b55d)


