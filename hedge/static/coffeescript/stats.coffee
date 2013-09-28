$(document).ready ->
  showStats()
  updateStats()

showStats = () ->
  $.getJSON 'api/stats', (data) ->
    for stat in data.stats
      $('aside').append "#{stat.description}:<span align='right'>#{stat.value}</span>"
      $('aside').append "<div class='meter'><span id=#{stat.id}></span></div>"
    $('aside').append "<p>Updated: <span id='time'>#{data.time}</span>"

updateStats = () ->
  $.getJSON 'api/stats', (data) ->
    for stat in data.stats
      $("##{stat.id}").width "#{stat.percent}%"
    $("#time").text data.time
  setTimeout updateStats, 10000