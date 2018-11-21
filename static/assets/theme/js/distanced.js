	
		 var source, destination;
        var directionsDisplay;
        var directionsService = new google.maps.DirectionsService();
        google.maps.event.addDomListener(window, 'load', function () {
            new google.maps.places.SearchBox(document.getElementById('pkup_location'));
            new google.maps.places.SearchBox(document.getElementById('droff_location'));
            directionsDisplay = new google.maps.DirectionsRenderer({ 'draggable': true });
        });
		
		 function Getdirection()
		 {
			
          
            //*********DIRECTIONS AND ROUTE**********************//
            source = document.getElementById("pkup_location").value;
            destination = document.getElementById("droff_location").value;

            var request = {
                origin: source,
                destination: destination,
                travelMode: google.maps.TravelMode.DRIVING
            };
        

            //*********DISTANCE AND DURATION**********************//
            var service = new google.maps.DistanceMatrixService();
            service.getDistanceMatrix({
                origins: [source],
                destinations: [destination],
                travelMode: google.maps.TravelMode.DRIVING,
                unitSystem: google.maps.UnitSystem.METRIC,
                avoidHighways: false,
                avoidTolls: false
            }, function (response, status) {
                if (status == google.maps.DistanceMatrixStatus.OK && response.rows[0].elements[0].status != "ZERO_RESULTS") {
                    var distance = response.rows[0].elements[0].distance.text;
                    var duration = response.rows[0].elements[0].duration.text;
                   $('#totaldistanced').val(distance)
                   $('#totalduration').val(duration)
                   

                } else {
                    alert("Unable to find the distance via road.");
                }
            });
			
			
			}
		 
        function GetRoute() {
			$('.Route-intro').append('<button type="button" class="closeMap"><i class="fa fa-remove"></i></button>').addClass('openUp')
            var mumbai = new google.maps.LatLng(18.9750, 72.8258);
            var mapOptions = {
                zoom: 14,
                center: mumbai
            };
            map = new google.maps.Map(document.getElementById('dvMap'), mapOptions);
            directionsDisplay.setMap(map);
            directionsDisplay.setPanel(document.getElementById('dvPanel'));

            //*********DIRECTIONS AND ROUTE**********************//
            source = document.getElementById("pkup_location").value;
            destination = document.getElementById("droff_location").value;

            var request = {
                origin: source,
                destination: destination,
                travelMode: google.maps.TravelMode.DRIVING
            };
            directionsService.route(request, function (response, status) {
                if (status == google.maps.DirectionsStatus.OK) {
                    directionsDisplay.setDirections(response);
                }
            });

            //*********DISTANCE AND DURATION**********************//
            var service = new google.maps.DistanceMatrixService();
            service.getDistanceMatrix({
                origins: [source],
                destinations: [destination],
                travelMode: google.maps.TravelMode.DRIVING,
                unitSystem: google.maps.UnitSystem.METRIC,
                avoidHighways: false,
                avoidTolls: false
            }, function (response, status) {
                if (status == google.maps.DistanceMatrixStatus.OK && response.rows[0].elements[0].status != "ZERO_RESULTS") {
                    var distance = response.rows[0].elements[0].distance.text;
                    var duration = response.rows[0].elements[0].duration.text;
                    var dvDistance = document.getElementById("dvDistance");
                    dvDistance.innerHTML = "";
                    dvDistance.innerHTML += "<label>Distance:<b>" + distance + "</b></label>";
                    dvDistance.innerHTML += "<label>Duration:<b>" + duration + "</b></label>";
                    

                } else {
                    alert("Unable to find the distance via road.");
                }
            });
			
			$('#routeInfo').removeAttr('style');
			$('.closeMap').click(function(){
				$('.Route-intro').removeClass('openUp')
			})
        }
		
	