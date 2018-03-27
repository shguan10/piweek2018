# Introduction

Snowflake is a upgrade for your fridge, turning any regular fridge into a smart fridge. It will perform automatic food inventory tracking to provide meal recommendations, suggest recipes, and keep track of expiration dates. On a small scale, users will find a improvement in their own culinary life as they’re assisted in achieving the full value of the food they buy to create tasty, delicious, and, best of all, easily-accessible meals. On a larger scale, however, Snowflake will help reduce food waste and amplify the environmental and health benefits of home cooking.

# Usage

A new user would register their pi to an id and set a password, and the user would mount the pi on their fridge. The pi would then keep track of the foods the user is putting in and taking out of their fridge, keeping track of all items in the fridge. If the user needs some recipes, they can access the Snowflake website, which will suggest for them recipes based on what items are already in their fridge. The website will also detect when foods are expired and alert the user.

# Behind the Scenes

When the pi is initialized, it registers a user and hashed password in a postresql user database on an external Amazon EC2 Python server. When the pi camera detects motion, it takes pictures and TensorFlow will be used to identify whether the object is a food or not. In addition, Snowflake will distinguish whether or not the object is being taken out or going into the fridge and modify the database accordingly. The database will also check the food item with a University of Kentucky dataset on food expiration dates, and list a proper expiration date. When the expiration date comes, the food will become greyed out and listed as expired on the Snowflake website, built on top of Angular.js and Bootstrap.

When the user requests recipes, the food inventory will be conglomerated and queried into a Edamame recipe API, returning recipes for the user on the Snowflake website.

# piweek2018
https://www.youtube.com/watch?v=k4J7xHBGMlw

# DEMO
https://www.youtube.com/watch?v=XCwv_y-jH1E&feature=youtu.be
