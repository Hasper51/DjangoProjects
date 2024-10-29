
//YouTube Channel: @kaeattatech
//https://www.youtube.com/@kaeattatech


function getWeather(location, apiKey){

    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=imperial`;

    fetch(apiUrl)
        .then(response => {
            if(!response.ok){
                //This is what will happen if the response didn't go well.
                //It will throw this error.
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            const weatherDescription = data.weather[0].description;
            //The Math.floor could be used to round the temperature number if needed.
            //It can be helpful if you choose to also display the degrees in Celsius.
            const temperatureMin = data.main.temp_min;
            const temperatureMax = data.main.temp_max;
            const humidity = data.main.humidity;
            const windSpeed = data.wind.speed;
            const d = new Date();
            const feelsLike = data.main.feels_like;
            const newPressure = data.main.pressure;

            //Now it is time make it display onto the browser screen.
            //First I need to grab the id's of the elements that I want 
            //to display the weather information.
            const destination = document.getElementById('locationDestination');
            //I will keep doing that until that part is done.
            const displayDate = document.getElementById('theDate');
            const newTemp = document.getElementById('highTemp');
            const newTempL = document.getElementById('tempDegreesL');
            const feelsTemp = document.getElementById('feels');
            const dailyDescription = document.getElementById('condition');
            const theHumidity = document.getElementById('humidity');
            const theNewWind = document.getElementById('theWind');
            const pressureTemp = document.getElementById('pressureValue');
            
            //Now I will do the following to assign the weather info to the 
            //new variables that were created that store the id location of the divs and 
            //elements that I want the info to display to.

            destination.innerHTML = `${location}`;
            displayDate.innerHTML = `${d}`;
            newTemp.innerHTML = `${temperatureMax}`;
            newTempL.innerHTML = `${temperatureMin}`;
            feelsTemp.innerHTML = `${feelsLike}`;
            dailyDescription.innerHTML = `${weatherDescription}`;
            theHumidity.innerHTML = `${humidity}`;
            theNewWind.innerHTML = `${windSpeed}`;
            pressureTemp.innerHTML = `${newPressure}`;


            console.log(`Description: ${weatherDescription}`);
            console.log(`Today's date: ${d}: `);
            console.log(`Weather in ${location}: `);
            console.log(`Feels Like: ${feelsLike}`);
            console.log(`Min Temp: ${temperatureMin} F`);
            console.log(`Max Temp: ${temperatureMax} F`);
            console.log(`Humidity: ${humidity}%`);
            console.log(`Wind Speed: ${windSpeed} mph`);
            console.log(`Pressure: ${newPressure}`);

        })
        .catch(error =>{
            console.error('Error fetching weather data: ', error);

        })
}


//Below is going to be the promptForLocation() function.
function promptForLocation() {
    //I just assigned whatever the user enters into the prompt box to 
    //new variable called location. I will do something similar with the 
    //API key.
    const location = prompt('Enter a city name: ');
    const apiKey = prompt('Enter your API key: ');

    if(location){
        //Below is a function that I am about to create now.
        //So whatever the user enters in the prompts will be sent to this 
        //function below.
        getWeather(location, apiKey);
    }
}