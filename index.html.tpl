<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <meta name="googlebot" content="noindex, nofollow">










  <script type="text/javascript" src="/js/lib/dummy.js"></script>








    <link rel="stylesheet" type="text/css" href="/css/result-light.css">




  <style type="text/css">

  </style>

  <title>Visitors per country</title>


</head>

<body>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
       <div id="regions_div" style="width: 900px; height: 500px;"></div>






<script type='text/javascript'>//<![CDATA[
      //https://developers.google.com/chart/interactive/docs/gallery/geomap
      google.charts.load('current', {'packages':['geochart']});
      google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = google.visualization.arrayToDataTable([
          ['Country', 'Visitors'],
          {% for country in countries %}
            ["{{country[0]}}", {{country[1]}} ],
          {% endfor %}
        ]);

        var options = {};
        //http://www.rapidtables.com/web/color/RGB_Color.htm
        // silver to red
        options['colors'] = ["#FFA07A", "#FF0000" ];

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
      }
//]]>

</script>

</body>

</html>
