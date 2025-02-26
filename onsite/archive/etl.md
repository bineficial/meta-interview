ETL Question
Problem Statement
Your mission is to build an ETL process to populate a dashboard that shows the top movies viewed for a streaming movie service. We'll assume our streaming movie service is successful - we have millions of daily users.

Imagine we have a logging system in place that captures user playback events such as:
(userid, movieid, PLAYBACK_STARTED, movie_pos_in_secs, utc_timestamp)
(userid, movieid, PLAYBACK_STOPPED, movie_pos_in_secs, utc_timestamp)

Further, imagine our data infrastructure team has made our lives easier in Data Engineering by building for us an upstream table that pairs up playback start and stop events as playback segments:
playback_segments = (userid, movieid, pb_start_pos, pb_end_pos, pb_start_timestamp, pb_end_timestamp)

Each record represents one continuously played segment of a movie. A user may view many segments of the same movie over the course of a single day, and may rewind or fast-forward between viewing. So for a given (userid, movieid, date), there may be many possibly overlapping or disjoint playback_segments that start and/or end within that day.

During a weekly meeting, a Product Manager asks you to if could build a dashboard that shows the following:

By date - By movie category - Show the Top 10 most viewed movies (with rank numbers 1-10)"
How would you go about building an ETL pipeline to provide data for the dashboard?

Design a model that can capture Product Waterfalls
Examples:
User clicks on Composer, types out a message, attaches a photo, picks a location, hits submit
User installs the app, enters their phone number, picks a password, finds friends via contacts
Notification Jewel lights up, user clicks the jewel, user clicks a notification, user gives feedback (like/comment) on the item in the notification
The design should consider that there will be a variable number of levels