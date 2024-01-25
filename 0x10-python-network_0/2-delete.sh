#!/bin/bash
# process a rm request to an URL with curl and show the body of the response
curl -sX DELETE "$1"
