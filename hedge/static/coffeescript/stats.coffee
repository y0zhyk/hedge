$(document).ready ->
  showStats()
  updateStats()

showStats = () ->
  $.getJSON 'api/stats', (data) ->
    for stat in data.stats
      $("aside").append "#{stat.description}:<swap class=value id=#{stat.id}_value></swap>"
      $("aside").append "<div class=meter><span id=#{stat.id}_percent></span></div>"
    $("aside").append "<p>Updated: <span id=time></span>"

updateStats = () ->
  $.getJSON 'api/stats', (data) ->
    for stat in data.stats
      $("##{stat.id}_value").text stat.value
      $("##{stat.id}_percent").width "#{stat.percent}%"
    $("#time").text data.time
  setTimeout updateStats, 10000