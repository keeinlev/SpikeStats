# SpikeStats

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Features](#features)
    * [Grid Layout](#stat-button-grid)
    * [Assigning a Stat to a Player](#assigning-a-stat-to-a-player)
        + [Developer's Notes](#devnotes1)
    * [Game Flow](#game-flow)
        + [Developer's Notes](#devnotes2)
    * [End of Game CSV File Generation](#end-of-game-csv-file-generation)
    * [Check Stats Button](#check-stats-button)

# Introduction

<p>SpikeStats is a Python program I wrote in high school using the TkInter GUI library and 
CSV library that heavily facilitated the process of jotting stats for our school volleyball
team.</p>

![appScreenshot](/screenshots/entiress.png/)

<p>The creation of this project stemmed from when I had volunteered as a stat-taker and
general assistant for the Sr. Girls Volleyball Team at my high school.
I myself am a volleyball player, having played both competitively and in school for three years,
and I had known the importance of keeping stats in order to understand the team's and individual
players' strengths and weaknesses. Taking stats was one of the most emphasized commands
given by my rep coach and I have stood by his data-oriented approach to the sport to
this day.</p>

<p>Throughout my two seasons playing under said coach, we were writing stats down on these
printed out tables with each player's name on the left and empty boxes for different
types of stats in the remaining space of the sheet. Every hit, every dig, every ace
and more was jotted down beside a player's name. We must have carried maybe twenty of these
sheets with us at all times.</p>

<p>Now you can imagine that this was not an efficient nor easy task, as volleyball is a fast-paced
sport. One look too long at the sheet to find a player's name could result in missing
the next play, and then you would be sitting there asking everyone else what just happened:
more time wasted, more time for the next play to be missed.</p>

<p>I hadn't come up with the ephiphany of writing an application for this task until my senior
year of high school, halfway through first semester, when I had just finished learning
File I/O for Python in my ICS 4U class.</p>

<p>This was around the time that our own Sr Boys' Volleyball Team had lost in the semifinals 
after one of our most successful years in our high school careers. I was heartbroken from
the defeat at the hands of our longtime rivals, Georgetown District HS, and I had been looking
for anything I could do that was even remotely related to volleyball to cope with the end 
of my season.</p>

<p>Luckily, the Sr. Girls' season was starting, and I took the opportunity to help the coach
with something that I knew would be beneficial for the team: taking stats.</p>

<p>For a few games, I had stuck to the original method that I knew: pen and paper. After games,
I'd be at my computer punching each stat into an Excel Spreadsheet. Horrible, I know. However,
it quickly dawned on me that I could do more; I could extend my learning from the classroom
into something real, something tangible that would not just be some assignment that I write
and never look at again afterwards. I had learned GUI and TkInter in Grade 11, and now I had
the knowledge to use more complicated data structures and automated file writing to bring my 
vision of an interactive stat-taking application to reality.</p>

<p>For three months or so, I walked into the gym or drove to away games every week with my
laptop in hand and sat on the bench with the team as I entered in stats. After every set,
it was as simple as pressing a button to generate a completely fresh CSV file containing all
the recorded events of the game, which the coach would later be converted to an Excel file for
further analysis (she was a Data Management and Calculus teacher).</p>

<p>This was my first real taste at what it was like to create something based off a need for
a more streamlined process. It reminds me to this day to be ambitious and that my skills
can be applicable in so many ways. Have a look at the features and inner functions of this
program below.</p>


# Features
## Stat Button Grid
<p>Upon running the application, the user in encountered with a large grid full of buttons,
most of which display the label of a relevant volleyball stat.</p>

![gridScreenshot](/screenshots/buttongrid.png/)

<p>The grid is mostly organized by actions that the player can make. For example, the first
column includes "Hit", "Kill" and "Error", all stats relevant to the action of attacking
across the net. The next column is reserved for serve-related stats. The third and fourth
columns are all for defensive stats, with the exception of "Blocked", which was added in a
later version as a miscellaneous attacking stat. The layout of the grid was designed so that
the user can develop a solid familarity with the region of each stat group, potentially
decreasing the amount of time needed to record a stat.</p>

<p>The right side of the screen also includes "Opponent Error" and "Opponent Point", stats
that aid in keeping track of points that are not specifically related to one player, so that
the end tallies will correspond to the correct number of points.</p>

<p>An undo button is available to the very right side of the screen, in case the same stat
is clicked twice, or if the wrong stat was clicked.</p>


## Assigning a Stat to a Player
<p>In order to record a stat for a given player, the user must enter their jersey number into
the appointed text box, then press "Enter".</p>

![defaultJerseyScreenshot](/screenshots/defaultjersey.png/)<br>
![enterPlayerScreenshot](/screenshots/validjersey.png/)

<p>Players' jersey numbers and full names will be echoed to a label which appears in the blank
space of the screen. Numbers and names are pulled directly from the local roster.txt file,
which must be written on its own to match the team information.</p>

![rosterScreenshot](/screenshots/rostertxt.png/)

<p>When recording a stat while a player is selected, the change will be echoed to a text label
above the "Block Errors" and "Blocked" buttons. Observe that the default value of the label
is "No changes made yet".</p>

![defaultStatScreenshot](/screenshots/defaultchange.png/)
![changeStatScreenshot](/screenshots/addstat.png/)

<p>Trying to press "Enter" while an invalid jersey number is inputted will result in an error
message in both the player name text label and the changes made text label.</p>

![enterErrorScreenshot](/screenshots/errorsjersey.png/)

<p>To avoid incorrect addition of stats, pressing "Enter" after entering a valid jersey number
is <b>required</b>. The user will be prompted to press "Enter" if they attempt to click a
stat button after only typing in a new jersey number into the text box and not pressing "Enter".</p>

![invalidJerseyScreenshot](/screenshots/invalidjersey.png/)


### <a id = "devnotes1"></a>Developer's Notes
<p>While writing this feature, I knew that the user would probably be more accustomed to the 
players' names, but I felt like entire names would take too long to write out, and some players
shared the same first or last names, so this was not a viable approach. I chose to use jersey
numbers as identifiers since each player has a unique number. Also, the number would always be
on the player's back, whereas last names were not included on school uniforms. Since players
literally wear their numbers, it's easy for the user to remember who performed the play they
just witnessed. I found this to be the optimal method of associating players to their data.</p>


## Game Flow
<p>Generates a small colored bar graph illustrating the point distribution over time between
both teams </p>

![gameFlowScreenshot](/screenshots/flow.png/)

### <a id = "devnotes2"></a>Developer's Notes
<p>A feature that was implemented much later after the initial version of the application.
Gives a general idea of how the momentum of the game changes over time and highlights the
points at which a team may struggle to score at an attempt to locate trends. This was never
fully implemented so the data does not export into the CSV file, but rather stays local
to the session only while the application is running.</p>


## End of Game CSV File Generation
<p>Creates a new .csv file in the local directory displaying all stats recorded in the session.</p>

![csvOpenedScreenshot](/screenshots/openedcsv.png/)

<p>This feature takes all the data from the structure created to store the stats and writes
the new .csv file line by line. The file will be formatted with all names and 
jersey numbers of players in the first column and all stat categories as headers.</p>

<p><b>It is crucial that the user fills in the "VS Team" text box and clicks "Confirm" before
attempting to create a .csv file for the recorded game, as the title of the resulting file
will depend on the input of this text box. <b></p>

![defaultVSScreenshot](/screenshots/beforevsteam.png/)
![confirmVSScreenshot](/screenshots/aftervsteam.png/)

<p>Titles will be in the form of "YYYY-MM-DD vs. OpposingTeam"</p>

![csvInFolderScreenshot](/screenshots/generatedcsv.png/)


## Check Stats Button
<p>Logs the main data structure containing all stats to the console, helpful for making sure
the correct changes were made without having to create the final .csv file.</p>

![checkStatsScreenshot](/screenshots/checkstats.png/)
