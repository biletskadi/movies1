1. Information about module's purpose
Module movies_map recieve from user:
1) a year of the movie
2) latitude
3) longitude
Based on recieved information module generates a map with 3 layers:
1) the first layer is point, which module recieve from user
2) the second layer is points of locations of 5 movies filmed nearby the point
3) the third layer is points of seven wonders of the ancient world

2. A description of the html file structure and the markup tags that were generated;
html file generates html page with map
it has three main parts:
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
    . . . 
    
</head>

<body>    
    
            <div class="folium-map" id="map_4a3cc13763d749839256537d6f678617" ></div>
        
</body>
and
<script>    
    
            var map_4a3cc13763d749839256537d6f678617 = L.map(
            
            . . .
            
</script>
Markup tags:
<!DOCTYPE> - defines the document type
<head> - defines information about the document
<body> - defines the document's body
<script> - defines a client-side script
<link> - defines the relationship between a document and an external resource (most used to link to style sheets)
<style> - defines style information for a document
<div> - defines a section in a document


3. Short conclusion about information, which map gives you:
You can discover which movie, where filmed near you and where are 7 wonders of the ancient world on the map

4. Startup example (year and location) of input and screenshot of generated map
Enter a year of the movie: 2009
Enter your latitude: 4.83993
Enter your longitude: 5.83902
Map is generating...
Please wait...