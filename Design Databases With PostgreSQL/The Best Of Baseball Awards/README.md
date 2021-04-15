Set up PostgreSQL Locally

In this off-platform project, you will work on creating a database using PostgreSQL on your own computer. Before you get started, make sure you have gone through the necessary setup steps found in our article about setting up PostgreSQL locally. You will need to set up a PostgreSQL server as well as a client to connect to your server. As described in the article linked above, we recommend using Postbird for your client.
Download the Data and Instructions

Download the instructions, starting files, and solution code to the project. The instructions are listed below, but it may be useful to download the instructions so you can work on this project while offline.

There may be some files included in the project to help you get started. The instructions should explain how to use those files.

Finally, we have also included solution code to help guide you if you get stuck.
A Note on Running SQL Locally

Before we get started, it’s important to discuss how running SQL on your own machine is slightly different than running SQL on Codecademy’s website. Consider an exercise on Codecademy that has two steps. The first step asks you to create a table, and the second step asks you to add a row to that table. To pass the first step, you might write something like this and then click run:

CREATE TABLE students (
   name TEXT, 
   age INTEGER
);

Then to pass the second step, you would add on to your file and hit run again, like so:

CREATE TABLE students (
   name TEXT, 
   age INTEGER
);
 
INSERT INTO students (name, age) 
VALUES ('Zack Morris', 18);

Notice that technically you’ve now run the CREATE TABLE line twice — once the first time you hit the run button, and again when you hit the run button to pass the second checkpoint.

If you were running this code on your own computer, this would cause an error — the second time you run the CREATE TABLE line, you would see an error because the table was already created. When working on your own computer, it’s a better idea to run each new line separately, rather than adding a new line to the bottom of your file and running the entire file again.

If you were working through this example on your own computer, you should first run

CREATE TABLE students (
   name TEXT, 
   age INTEGER
);

and then run this line separately

INSERT INTO students (name, age) 
VALUES ('Zack Morris', 18);

That being said, sometimes you want to save your SQL statements in a single file for later use. For example, we have provided you with solution code in a .sql file. If you were to open your PostgreSQL client, and import that .sql file (usually done through the File menu of a client), you could run all of our solution code at once.
Project Instructions

Welcome! In this project, we will be looking at a massive baseball database containing information about players, teams, managers, salaries, and just about anything you might want to know about baseball. This dataset contains data from 2019 all the way back to 1871. Let’s see what interesting facts we can learn from this database!
Step 1 — Downloading The Data

In the files that you downloaded to begin this project, you will find a file called baseball_database.sql. In your PostgreSQL client, create a new database (we named ours baseball), and then open this .sql file. This should run all of the PostgreSQL commands to completely set up your tables and populate the tables with the data.

If you’re using Postbird, you can create a new database under the “Select database” menu, by choosing “Create Database”. Then you can then import the .sql file by selecting “Import .sql file” from the “File” menu.

Note that some learners have had trouble loading the data. If you’re having problems, this forum post has some helpful debugging tips.

This is a remarkable dataset that was put together by Sean Lahman, among others. This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. We ported Sean’s work to a PostgreSQL database to work for this project.
Step 2 — Investigate The Data

Now that we’ve got the data in a database, it’s time to take a look at what we’re working with. Note that there is a lot of data here — 29 tables to be exact. If you’re curious about any of the fields in any of these tables, you can consult the readme.txt file provided in the downloaded files. You can also find more detailed documentation on Sean Lahman’s site.

For now, let’s take a look at some of the most important tables. Take a look at the first few rows of the people, batting, pitching, and teams table. You can do this by writing some SQL queries or by using your client’s GUI to look at the table’s contents. (In Postbird, this is the “Content” tab). Make note of the fields there, and how they relate to each other. Start to think about how these tables connect. For example, how might you link a player’s name to the team they played on in a given year.
Part 3 - Handing Out Awards

Now that we’ve got a sense of what the data looks like, let’s use our querying skills to hold our own baseball awards show — The Best of Baseball. For each of these awards, write a query to find the award winner. If you get stuck on any of these queries, you can look at our solution in the solutions.sql file provided. We’ve also given you a hint on how you might start writing your queries for each of these awards.
Heaviest Hitters

This award goes to the team with the highest average weight of its batters on a given year.
Hint
We need to join three tables together — The table contains the weights of each player. We can link those players to the year and team they were batting for in the table. Finally, the table has a field, but we want the actual team name. We can link the table to the table to find the name of the team. We'll need to use the , , and to find the average weight of the players on these teams.
Shortest Sluggers

This award goes to the team with the smallest average height of its batters on a given year. This query should look very similar to the one you wrote to find the heaviest teams.
Hint
Once again we need to join the , , and tables. This time, use your aggregate functions on the column. Also make sure to use this time to get the shortest teams first.
Biggest Spenders

This award goes to the team with the largest total salary of all players in a given year.
Hint
You'll mostly be using the table for this one. Use , and to sum every player's salary for a given team on a given year. You'll want to group by both and . If you want to get the real name of the team rather than just the , you'll need to with the table.
Most Bang For Their Buck In 2010

This award goes to the team that had the smallest “cost per win” in 2010. Cost per win is determined by the total salary of the team divided by the number of wins in a given year. Note that we decided to look at just teams in 2010 because when we found this award looking across all years, we found that due to inflation, teams from the 1900s spent much less money per win. We thought that looking at all teams in just the year 2010 gave a more interesting statistic.
Hint
This should look very similar to your last query. You'll still need to join the and table. This time you want to divide the sum of the players salaries by the column from the table. Because of this, you'll also need to add to the clause. Finally, we added the function to the number we're reporting to make our output a little more readable.
Priciest Starter

This award goes to the pitcher who, in a given year, cost the most money per game in which they were the starting pitcher. Note that many pitchers only started a single game, so to be eligible for this award, you had to start at least 10 games.
Hint
You'll need to connect the table and the table. The column you're interested in the table is (for "games started"). When you join these two tables, you'll want to make sure the , , and all match — it is possible for one player to play on multiple teams in a given year. Make sure to use a clause to ensure the pitcher has started in at least 10 games. Finally, you may want to join with the table to get the player's full name.
Part 4 — Create Your Own Award

Come up with your own award and write a query to find the winner. We’d love to see your creativity! If you come up with a fun award, get in touch with us on Twitter (@Codecademy) to tell us your award name and winner. Use the hashtag #TheBestOfBaseballAwards to see what other people have found!

To get you started, here were some award names that we thought could be fun:

    Bean Machine: The pitcher most likely to hit a batter with a pitch
    Canadian Ace: The pitcher with the lowest ERA who played for a team whose stadium is in Canada
    Worst of the Best: The pitcher or batter inducted into the hall of fame with the worst career stats (you can decide what stat to look at)

