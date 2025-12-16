#basically we made simple headers for our data for csv from json data

["id", "created_at", "job", "interview", "alternate_url"] as $h 
| $h , (.items[] | [.id, .created_at, .name, .has_test, .alternate_url]) 
| @csv
