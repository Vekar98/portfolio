function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
  }
  
  function getBedroomValue() {
    var uiBedrooms = document.getElementsByName("uiBedrooms");
    for(var i in uiBedrooms) {
      if(uiBedrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
  }

  function getGarage() {
    var uiGarage = document.getElementsByName("uiGarage");
    for(var i in uiGarage) {
      if(uiGarage[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
}

  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var floor_area = document.getElementById("uiFloorArea");
    var land_area = document.getElementById("uiLandArea");
    var build_year = document.getElementById("uiBuildYear");
    var bedrooms = getBedroomValue();
    var bathrooms = getBathValue();
    var garage = getGarage();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    // var url = "http://127.0.0.1:8000/predict_home_price";
    var url = "/api/predict_home_price";

  
    $.post(url, {
        floor_area: parseFloat(floor_area.value),
        land_area: parseFloat(land_area.value),
        build_year: parseFloat(build_year.value),
        bedrooms: bedrooms,
        bathrooms: bathrooms,
        garage: garage,
        location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " USD</h2>";
        console.log(status);
    });
  }

  function onPageLoad() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:8000/get_location_names";
    var url = "/api/get_location_names"; 
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;