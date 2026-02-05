/*('-1','Michael Jackson') Due to Type Affinity, the string '-1' is converted to -1 which can be inserted since -1 is an integer and there isn't another row with the key -1.*/
/*(2, 'Roger Waters') This will cause an error since there is already a row with the key 2.*/
/*(NULL, 'Roger Waters') This won't cause an error since NULL is a valid value for the primary key in SQLite.*/