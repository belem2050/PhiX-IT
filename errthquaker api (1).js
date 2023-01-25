fetch('https://earthquake.usgs.gov/fdsnws/event/1/?format=geojson&minmagnitude=5.0&starttime=2022-12-15%27)
  .then(response => response.json())
  .then(data => {
    // Traitement des données récupérées à partir de l'API
    
  });