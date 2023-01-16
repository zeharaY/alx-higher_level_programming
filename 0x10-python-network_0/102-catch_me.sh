#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that gets  a message containing You got me!
curl -sL -X PUT -H "Origin: BestSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
