
# API basisproject Jorik Goris (r0901062 CCS02)

Dit project bevat het basisproject van API Development.


## Documentation

Deze github repository bevat alle nodige bestanden om dit project op te zetten.

Een github action pipeline zal gewijzigde bestanden in de main branch automatisch detecteren en de docker image rebuilden, waarna deze op dockerhub wordt gepushed.

Okteto cloud zal de docker-compose.yml file gaan gebruiken om de docker images te pullen en op te zetten.

Deze API bevat vijf endpoints; 3 GET endpoints, één POST en één DELETE endpoint. 

De eerste twee GET endpoints maken gebruik van de openweather API. Deze 'consumen' als het waar een andere API. 

Met de endpoints /weather/{city} en /forecast/{city} kan je het weer of de weersvoorspelling voor een bepaalde stand ophalen.

Deze endpoints zullen op hun beurt een GET request doen op de openweather API. 

De andere 3 endpoints dienen om zelf weerdata te posten, meerbepaald de stad, temperatuur, condities en of er op dat moment neerslag valt.

Deze data kan je in een JSON body posten, ophalen en verwijderen. De data wordt opgeslagen in een mysql database.

Om de API te gebruiken heb je een API key nodig, die geprogrammeerd staan in de main.py file.




## Resultaat Okteto Cloud
Verbind Okteto Cloud met je github repository.
Deploy daarna in je Dev environment, waarop Okteto de docker-compose.yml file gaat gebruiken om je docker containers op te zetten. Deze docker containers zijn gebuild door je github pipeline.

#insert fotos#


## Resultaat Postman

Openweather API:

#insert fotos#


API:

#insert fotos#


## FastAPI - Swagger UI
