#### Environment
python 3.6 or newer
#### Install Libs
```
pip install click
pip install ijson
```

#### How to run
- Mark **tokoin-simple-test/src** as root folder
- Put data files (json) in **tokoin-simple-test/data**
- Go to src directory
```shell script
$ cd src
```

- Show help
```shell script
$ python main.py -h
$ python main.py search -h
```

- Run with prompt command:
```sh
$ python main.py search
```
- Run with full command
```sh
$ python main.py search --search_type=<search_type> --term=<term> --value=<value>
$ python main.py searchable
```
    
### Example
- Search by prompt
```shell script
$ python main.py search
Select 1) Users or 2) Tickets or 3) Organizations: 1
Enter search term: _id
Enter search value []: 71
Searching users for "_id" with a value of "71"

_id                           				71
url                           				"http://initech.tokoin.io.com/api/v2/users/71.json"
external_id                   				"c972bb41-94aa-4f20-bc93-e63dbfe8d9ca"
name                          				"Prince Hinton"
alias                         				"Miss Dana"
created_at                    				"2016-04-18T11:05:43 -10:00"
active                        				true
verified                      				false
shared                        				false
locale                        				"zh-CN"
timezone                      				"Samoa"
last_login_at                 				"2013-05-01T01:18:48 -10:00"
email                         				"danahinton@flotonic.com"
phone                         				"9064-433-892"
signature                     				"Don't Worry Be Happy!"
organization_id               				121
tags                          				["Davenport", "Cherokee", "Summertown", "Clinton"]
suspended                     				false
role                          				"agent"
organization_name             				"Hotc\u00e2kes"
submitted_ticket_0            				"A Catastrophe in Micronesia"
submitted_ticket_1            				"A Drama in Wallis and Futuna Islands"
submitted_ticket_2            				"A Drama in Australia"
assignee_ticket_0             				"A Catastrophe in Sierra Leone"
```
- Search by full command
```shell script
$ python main.py search --search_type=1 --term=_id --value=71
```
- List of Searchable fields
```shell script
$ python main.py searchable

------------------------------------------
Search Users with
_id
url
external_id
name
alias
created_at
active
verified
shared
locale
timezone
last_login_at
email
phone
signature
organization_id
tags
suspended
role
------------------------------------------
Search Tickets with
_id
url
external_id
created_at
type
subject
description
priority
status
submitter_id
assignee_id
organization_id
tags
has_incidents
due_at
via
------------------------------------------
Search Organizations with
_id
url
external_id
name
domain_names
created_at
details
shared_tickets
tags
```

### Run Unittest
```shell script
$ cd src
$ python -m unittest discover -s ./ducle/tests/ -v
```