#include <stdio.h>
#include <sqlite3.h>

#define DB_NAME "risk.db"

int main(int argc, char *argv[]) {
	
	sqlite3* db;

	int resultCode = sqlite3_open(DB_NAME, &db);

	if(resultCode) {
		printf("Failed to open database: %s", sqlite3_errmsg(db));
		return 0;
	}

	printf("Database opened\n");
	sqlite3_close(db);	
	return 0;
}