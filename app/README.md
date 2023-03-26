
# Setup

First install sqlite3 and its developer libraries for creating and using the
database required by the application:

```
apt install sqlite3
apt install libsqlite3-dev
```

Then run the following command to setup the database:

```
sqlite3 risk.db < create.sql
```

The application can be created by executing the makefile:

```
make
```

And finally, it can be run with:

```
./risk
```