$(document).ready(function () {
    startMonitoringStats()
});

function startMonitoringStats() {
    $.getJSON('api/stats', function (data) {
        $('#cpu').width(data.cpu + "%");
        $('#mem').width(data.mem + "%");
        $('#swap').width(data.swap + "%");
        $('#disk').width(data.disk + "%");
    });

    setTimeout(function () {
        startMonitoringStats()
    }, 10000);
}