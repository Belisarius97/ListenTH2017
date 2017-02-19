# Where's the important stuff?

The most crucial file is probably TreeHacks/listen/templates/listen/index.html.

The second most important file is TreeHacks/listen/views.py.

# How do I add new songs?

After running the server (cd in the command line to TreeHacks/ and type "python3 manage.py runserver") go to http://127.0.0.1:8000/admin/ and log in with username administrator and password treehacks. Then click on Songs and add a new song!

TODO: move the skill level PNGs into buttons with transparent backgrounds and borders to make them big pressable buttons 
first need to figure out why button coloration and activation states aren't working visually
left in the css components of parallax in case you want to investigate it further (just wrap primary element groups in div class = parallax and nest another div class = parallax_group parallax_group_back, etc. go from back layer to front)

Group skill level image/buttons together and even out vertical sizing