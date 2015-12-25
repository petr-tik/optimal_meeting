#Optimal meeting

Following [this piece of advice](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html), I will write a full readmen first and base my todo list on top of it. 



Do you like to see friends and know you can go home conveniently and in good time? 

If you live in London, you not only benefit from ~~cheap accommodation~~ many places this large, vibrant city has to offer. Organising a group of friends coming from offices in different parts of the city has required for someone to make the sacrifice and travel to and from the outing together. This web app will save you and your friends time by using your departure and final destination (usually office and home respectively) postcodes and calculate the area of London, where you can easily travel to and from. It takes each individual's transport mode into account, so people on bicycles can whiz on cycle their shiny highways, while the more ~~spoiled~~ fashionable friends hail an uber/black cab/hackney. 

The idea came to me, when I was organising one of the first monthly chess nights that I run, because I was trying to work out, how to make it easy for people to come after work and get home in good time after playing an awesome round of chess. Of course, chess nights have special requirements like big tables, a quiet area and some grub afterwards (potential additions in the future), but most groups of people meeting up, should enjoy the time benefits this brings.  

Look how easy it is to use:


Features
--------

- Calculates an optimal meeting point for a group of people in London 
- Includes walking, tube, bus, cycling, taxi and car directions

Installation
------------

No need to install anything, follow [this link](http://petr-tik.github.io/optimal_meeting/login), log into a meeting group with your group id or create a new group. 

Share the group id with other people, so they can login and input their addresses. Once everyone registers, the organiser of the group will be notified 

Contribute
----------

- Issue Tracker: https://github.com/petr-tik/optimal_meeting/issues
- Source Code: https://github.com/petr-tik/optimal_meeting/src

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@google-groups.com

#License
-------

The project is licensed under the [WTFPL](https://en.wikipedia.org/wiki/WTFPL) license.


Input: different people's postcodes in London and preferred transport mode

Output: area where all those people can get to in least variable time

future improvements:
- taking home postcode and working out overall (from work to venue, from venue to home) trip duration
- front-end showing a map and an individual route for every user
- transport mode
