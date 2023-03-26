#include <stdio.h>
#include <sqlite3.h>

#define DB_NAME "risk.db"

int main(int argc, char *argv[]) {
	
	int result;
	char* error;
	char insert[100];
	sqlite3* db;

	if(argc < 3) {
		printf("Missing arguments:\n");
		printf("\t./risk [user_id] [rating]\n");
		return 0;
	}

	result = sqlite3_open(DB_NAME, &db);

	if(result != SQLITE_OK) {
		printf("Failed to open database, %d: %s\n", result, sqlite3_errmsg(db));
		return 0;
	}
	printf("Database opened\n");

	sprintf(insert, "INSERT OR REPLACE INTO USERS VALUES(%s, %s);", argv[1], argv[2]);
	result = sqlite3_exec(db, insert, NULL, NULL, NULL);
	if(result != SQLITE_OK) {
		printf("Failed to insert record, %d: %s\n", result, sqlite3_errmsg(db));
		return 0;
	}
	printf("Record inserted\n");

	sqlite3_close(db);	
	return 0;
}