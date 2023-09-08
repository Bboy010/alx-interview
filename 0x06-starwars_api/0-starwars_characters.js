#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as a command-line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

// Define the API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Send a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    // Parse the response JSON
    const film = JSON.parse(body);

    // Extract the list of character URLs
    const characterUrls = film.characters;

    // Function to fetch and print character names
    const fetchCharacterNames = (urls, index = 0) => {
      if (index >= urls.length) {
        return; // All characters have been printed
      }

      // Send a GET request to the character URL
      request(urls[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character:', charError);
        } else if (charResponse.statusCode !== 200) {
          console.error('Request for character failed with status code:', charResponse.statusCode);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);

          // Fetch the next character
          fetchCharacterNames(urls, index + 1);
        }
      });
    };

    // Start fetching and printing character names
    fetchCharacterNames(characterUrls);
  }
});
