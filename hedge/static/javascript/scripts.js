// Generated by CoffeeScript 1.6.3
(function() {
  var showStats, updateStats;

  $(document).ready(function() {
    showStats();
    return updateStats();
  });

  showStats = function() {
    return $.getJSON('api/stats', function(data) {
      var stat, _i, _len, _ref;
      _ref = data.stats;
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        stat = _ref[_i];
        $("aside").append("" + stat.description + ":<swap class=value id=" + stat.id + "_value>" + stat.value + "</swap>");
        $("aside").append("<div class=meter><span id=" + stat.id + "_percent width=\"" + stat.percent + "%\"></span></div>");
      }
      return $("aside").append("<p>Updated: <span id=time>" + data.time + "</span>");
    });
  };

  updateStats = function() {
    $.getJSON('api/stats', function(data) {
      var stat, _i, _len, _ref;
      _ref = data.stats;
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        stat = _ref[_i];
        $("#" + stat.id + "_value").text(stat.value);
        $("#" + stat.id + "_percent").width("" + stat.percent + "%");
      }
      return $("#time").text(data.time);
    });
    return setTimeout(updateStats, 10000);
  };

}).call(this);
