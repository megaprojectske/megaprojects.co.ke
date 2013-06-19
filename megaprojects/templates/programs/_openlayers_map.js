OpenLayers.ImgPath = "{{ STATIC_URL }}openlayers/img/";

var options, layer, map;

function init() {
  options = {
    maxExtent: new OpenLayers.Bounds(-200000, -200000, 200000, 200000),
    zoom: 5,
    controls: []
  };

  layer = new OpenLayers.Layer.OSM(
    "MapQuest OSM Tiles",
    [
      "http://otile1.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png",
      "http://otile2.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png",
      "http://otile3.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png",
      "http://otile4.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png"
    ],
    {
      attribution: "Data, imagery and map information provided by <a href='http://www.mapquest.com/' target='_blank'>MapQuest</a>, <a href='http://www.openstreetmap.org/' target='_blank'>Open Street Map</a> and contributors, <a href='http://creativecommons.org/licenses/by-sa/2.0/' target='_blank'>CC-BY-SA</a> <img style='margin-top: -6px;' src='http://developer.mapquest.com/content/osm/mq_logo.png'>",
      transitionEffect: "resize"
    }
  );

  map = new OpenLayers.Map("openlayers", options);
  map.addLayer(layer);
  map.addControl(new OpenLayers.Control.Navigation({'zoomWheelEnabled': false}));
  // map.addControl(new OpenLayers.Control.ZoomPanel());
  map.addControl(new OpenLayers.Control.Attribution());
  map.addControl(new OpenLayers.Control.ScaleLine());
  map.setCenter(
    new OpenLayers.LonLat(38, 0.5).transform(
      new OpenLayers.Projection("EPSG:4326"),
      map.getProjectionObject()
    )
  );
}

init();
