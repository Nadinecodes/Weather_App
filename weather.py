import requests
import json

class Weather:
    def __init__(self, location=input("Please enter a location: ")):
        self.location=location

#Get weather api 
    def get_weather_api(self):
        base_url ="https://rapidapi.p.rapidapi.com/observations/summary/"#new%20york,%20us" 
        url=base_url + self.location
        headers = {
            'x-rapidapi-host': "aerisweather1.p.rapidapi.com",
            'x-rapidapi-key': "MY_API_KEY"
        }

        response =requests.request("GET", url, headers=headers)
        json_data=response.json()
        
#Get temperature    
        avg_temp=json_data["response"][0]["periods"][0]["summary"]["temp"]["avgF"]
        return("The current weather is {}".format(avg_temp)+'F')
        


if __name__ == '__main__':
    my_weather=Weather()
    print(my_weather.get_weather_api())

