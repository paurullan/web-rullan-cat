%include header.tlp

<body>
Hi there.

<div id="location">
    You position is not known right now.
</div>

</body>

<script>
    function displayLocation(pos) {
        var lat = pos.coords.latitude;
        var lon = pos.coords.longitude;
        var div = document.getElementById("location");
        div.innerHTML = lat + ", " + lon;
    }
    navigator.geolocation.getCurrentPosition(displayLocation);
</script>

</html>

