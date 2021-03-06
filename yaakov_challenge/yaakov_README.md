\***all credit to [Yaakov](https://github.com/ybressler/teaching/tree/main/classes)**\*

This module contains information + is a guide for how and when to use
classes in python.

# Challenge:
Say you are building a tool which allows recruiters more effectively
screen candidates for a given job. The recruiter gives you a "wish list"
of variables they'd like to screen for, but you (a wisened developer) anticipate
that this list of requirements is likely to change, quite rapidly at that. With
this in mind, you plan on building a solution which is maleable and easy to
change.

## Provided Data:
You recieve data for a given person's past and current experiences. Your program
must determine if this person fits the role, and to what extent.

Example input data:
```
record = {
    first_name: Ada,
    last_name: Lovelace,
    work_experience: [
        {
            company: University of Cambridge,
            start_date: 1840-01-01,
            end_date: 1848-01-01,
            title: Software Developer
        },
        {
            company: University of Cambridge,
            start_date: 1848-01-01,
            end_date: 1852-06-01,
            title: Senior Software Developer
        },
    ]

}
```
#### Some notes:
* Each person can have many work experiences
* A person cannot have concurrent jobs (each job they've had cannot
    exist while they've had another job).
    * If a start data precedes an end date, overwrite the start date to
        the end date.
    * Ex:
        * job 1 `end_date = '2015-01-15'`
        * job 2 `start_date = '2015-01-01'`
        * job 2 `start_date` becomes `'2015-01-15'`
* If an end date is not provided, assume that person still holds that job.


## Requirements:
Your recruiter would like the following attributes:
* N years experience total
    * N years experience in a senior role
        * You must create and execute a definition for this.
    * N years experience in a data role
        * You must create and execute a definition for this.
    * N years experience in a leadership role
* Current job title
* If the candidate is working > 1 year in their current role
* Average length of time a candidate has worked at a company

-----

## Extra notes:
* You must use classes and methods to execute everything.
* Data will be provided in the accompanied json `work_experience_challenge.json`