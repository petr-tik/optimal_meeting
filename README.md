#Optimal meeting

Following [this piece of advice](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html), I will write a full readme first and base my todo list on top of it. 

Do you want to see your friends in London go home in good time? 

Living in London is great if you enjoy ~~super expensive accommodation~~ many bars, meetups, events and culture spots this large, vibrant city has to offer. Organising a group of friends coming from offices in different parts of the city has required for someone to make the sacrifice and travel to and from the outing together. This web app will save you and your friends time by using your departure and final destination (usually office and home respectively) postcodes and calculate the area of London, where all of you can easily travel to and from. It takes each individual's transport mode into account, so people on bicycles can whiz on shiny cycle superhighways, while the more ~~spoiled~~ fashionable friends hail an uber/black cab/hackney carriage. 

The idea came to me, when I was organising one of the first monthly chess nights that I run, because I was trying to work out, how to make it easy for people to come after work and get home in good time after playing an awesome round of chess. Of course, chess nights have special requirements like big tables, a quiet area and some grub afterwards (potential additions in the future), but most groups of people meeting up, should enjoy the time benefits this brings.  

Features
--------

- Calculates an optimal meeting point for a group of people in London and suggests a place according to geographical and other requirements
- Includes walking, tube, bus, cycling, taxi and car directions

Installation
------------

No need to install anything, follow [this link](http://petr-tik.github.io/optimal_meeting/login), log into a meeting group with your group id or create a new group. 

The organiser creates a group setting the date, time, keyword requirements (_pub_, _italian restaurant_, _club_). and number of people in the group. A group id number is created, which the organiser can then share with the group. Using this number people can log in and input their data. Each user submits their departure and home postcodes (easiest to turn into coordinates) and their preferred travel mode on the day of travel. 

Once everyone registers, the organiser of the group will be notified and the optimal meeting area is calculated, where suitable locations according to interest are presented. The organiser chooses the place and exact direction are available to everyone. 

Contribute
----------

- Issue Tracker: https://github.com/petr-tik/optimal_meeting/issues
- Source Code: https://github.com/petr-tik/optimal_meeting/src

**please** add issues, fork and send me PRs! 

Support
-------

If you are having issues, please let me know.

License
-------

The project is licensed under the [WTFPL](https://en.wikipedia.org/wiki/WTFPL) license.
