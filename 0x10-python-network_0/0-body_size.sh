#!/bin/bash
# put a URL, process a request and shows the size of the body
curl -sI $1 | grep -i content-length | awk '{print $2}'
