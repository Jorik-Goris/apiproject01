# API basisproject Jorik Goris (r0901062 CCS02)

Dit project bevat het basisproject van API Development.
foto's: 

## Documentation

Deze github repository bevat alle nodige bestanden om dit project op te zetten.

##################files################

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


## Resultaat Okteto Cloud
Verbind Okteto Cloud met je github repository.
Deploy daarna in je Dev environment, waarop Okteto de docker-compose.yml file gaat gebruiken om je docker containers op te zetten. Deze docker containers zijn gebuild door je github pipeline.

https://user-images.githubusercontent.com/95848835/282313650-c7057ae9-7261-4418-b942-2be89b033a00.png
https://user-images.githubusercontent.com/95848835/282313651-c4ff7f1c-82ff-4eb9-a939-399e65856b0b.png
https://user-images.githubusercontent.com/95848835/282313652-60c978b8-7fec-4eaa-b55a-ae8ea6ba1aca.png
https://user-images.githubusercontent.com/95848835/282313663-53a0ce77-a694-44ac-bf12-bfcff2735839.png


## Resultaat Postman

Openweather API:

https://user-images.githubusercontent.com/95848835/282313653-cd70e2c5-b183-4210-b657-70e7146829b1.png
https://user-images.githubusercontent.com/95848835/282313653-cd70e2c5-b183-4210-b657-70e7146829b1.png
https://user-images.githubusercontent.com/95848835/282313654-b9abcdbf-2e04-45dc-bb9e-c7de51a408e4.png
https://user-images.githubusercontent.com/95848835/282313657-7a9648b7-7052-4489-aeed-1e13af8a3534.png


API:

https://user-images.githubusercontent.com/95848835/282313658-e5c5d702-c7de-47a3-85b6-6321625dec5b.png
https://user-images.githubusercontent.com/95848835/282313660-357314bb-62ec-4d77-b636-da5620f29157.png
https://user-images.githubusercontent.com/95848835/282313661-b4865df6-5430-46a3-95b2-8b879b9fa945.png

## FastAPI - Swagger UI
https://user-images.githubusercontent.com/95848835/282313664-9a68f253-ca1a-4534-a6fc-fdb2d342d66e.png
https://user-images.githubusercontent.com/95848835/282313665-767af8bb-afe9-45bd-a17d-3a26564f2700.png
https://user-images.githubusercontent.com/95848835/282313666-31f410be-7b07-4420-adf2-ba1edf92dbca.png
https://user-images.githubusercontent.com/95848835/282313668-893aeaf0-ab07-42c8-9e05-4209291ed8ea.png
https://user-images.githubusercontent.com/95848835/282313669-b9e48dc9-ffb6-4a61-9a19-1fbb851714b5.png
https://user-images.githubusercontent.com/95848835/282313670-37d3e1cc-cc37-435a-9ed6-4ae069667a32.png
