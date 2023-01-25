fetch('https://earthquake.usgs.gov/fdsnws/event/1/?format=geojson&minmagnitude=5.0&starttime=2022-12-15%27)
  .then(response => response.json())
  .then(data => {
    // Traitement des données récupérées à partir de l'API


    // Récupération de l'élément HTML dans lequel les données seront affichées
    const element = document.querySelector('#maDiv');

    // Pour chaque élément dans les données récupérées
    for (const item of data) {
      // Création d'un paragraphe HTML
      const paragraph = document.createElement('p');

      // Affectation de la valeur de l'élément à ce paragraphe
      paragraph.textContent = item;

      // Ajout du paragraphe à l'élément HTML
      element.appendChild(paragraph);
    }

  });