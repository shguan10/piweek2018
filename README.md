# Introduction

Snowflake is a upgrade for your fridge, turning any regular fridge into a smart fridge. It will perform automatic food inventory tracking to provide meal recommendations, suggest recipes, and keep track of expiration dates. On a small scale, users will find a improvement in their own culinary life as they’re assisted in achieving the full value of the food they buy to create tasty, delicious, and, best of all, easily-accessible meals. On a larger scale, however, Snowflake will help reduce food waste and amplify the environmental and health benefits of home cooking.

# Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=Re4hC_kxpIE
" target="_blank"><img src="http://img.youtube.com/vi/Re4hC_kxpIE/0.jpg" 
alt="Youtube demo" width="240" height="180" border="10" /></a>

*A demo of the project working. It's 5 minutes long.*

# Pitch
<a href="http://www.youtube.com/watch?feature=player_embedded&v=k4J7xHBGMlw
" target="_blank"><img src="http://img.youtube.com/vi/k4J7xHBGMlw/0.jpg" 
alt="Youtube demo" width="240" height="180" border="10" /></a>

*The original pitch for the idea, recorded for an internship with Capax Global. It's 3 minutes long.*


# Usage

A new user would register their pi to an id and set a password, and the user would mount the pi on their fridge. The pi would then keep track of the foods the user is putting in and taking out of their fridge, keeping track of all items in the fridge. If the user needs some recipes, they can access the Snowflake website, which will suggest for them recipes based on what items are already in their fridge. The website will also detect when foods are expired and alert the user.

# Behind the Scenes

When the pi is initialized, it registers a user and hashed password in a postresql user database on an external Amazon EC2 Python server. When the pi camera detects motion, it takes pictures and TensorFlow will be used to identify whether the object is a food or not. In addition, Snowflake will distinguish whether or not the object is being taken out or going into the fridge and modify the database accordingly. The database will also check the food item with a University of Kentucky dataset on food expiration dates, and list a proper expiration date. When the expiration date comes, the food will become greyed out and listed as expired on the Snowflake website, built on top of Angular.js and Bootstrap.

When the user requests recipes, the food inventory will be conglomerated and queried into a Edamame recipe API, returning recipes for the user on the Snowflake website.

## Team
+ [shguan10](https://github.com/shguan10/)
+ [17zhangw](https://github.com/17zhangw/)
+ [unbrace3](https://github.com/unbrace3/)

## Acknowledgements
We would like to acknowledge the following:
* Hackberry Pi Week officers and sponsers. Hackberry Pi Week is the 7-day hackathon in which we completed this project.
