# Restaurant API

## Requirements
- python
- mongodb

Establishes a local server that allows for requesting what restaurants are open at a given time. It does this by querying results from a mongodb collection.

The original dataset was transformed to make filtering easier:
- The weekdays have been mapped to numbers and put in an array
- The time ranges have been converted to a standardized military format
