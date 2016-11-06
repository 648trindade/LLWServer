#!/bin/bash

git commit -am '$1'

git push heroku master

heroku ps:scale web=1
