// Color palette used by all graphics
var colors = ["#1D507A", "#2F6999", "#66A0D1", "#8FC0E9", "#4682B4"];

//Save in memory 
var forecaster_data;

console.log("bonjour");
      
$.ajax({
    url: "/api/forecaster/",
    success: display_forecaster
});

// Upload the forecaster_data
d3.json('/api/forecaster', display_forecaster);

function display_forecaster(forecaster_data){
    var div = $()



}
/* TO DISPLAY IN CONSOLE
function display_nvd3_graph(result){
    console.log("Résultat de la requête :", result);
}

console.log("Au revoir");
*/

var ActualWeather = [{
    key : 'ActualWeather',
    values : forecaster_data['ActualWeather']
}]

nv.addGraph(function(){
    
})
