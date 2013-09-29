showStats = () ->
  $.getJSON 'api/stats', (data) ->
    for stat in data.stats
      $("aside").append "#{stat.description}:<swap class=value id=#{stat.id}_value>#{stat.value}</swap>"
      $("aside").append """<div class=meter><span id=#{stat.id}_percent/></div>"""
      $("##{stat.id}_percent").width "#{stat.percent}%"
    $("aside").append "<p>Updated: <span id=time>#{data.time}</span>"
    setTimeout updateStats, 10000

updateStats = () ->
  $.getJSON 'api/stats', (data) ->
    for stat in data.stats
      $("##{stat.id}_value").text stat.value
      $("##{stat.id}_percent").width "#{stat.percent}%"
    $("#time").text data.time
    setTimeout updateStats, 10000