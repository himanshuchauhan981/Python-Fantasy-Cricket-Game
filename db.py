import _sqlite3
from _sqlite3 import Error
import pandas as pd


class DbFiles:
    conn = None
    cur = None
    db_File = r'/home/himanshuchauhan/Desktop/Python-Fantasy-Cricket-Game/game-DB.db'

    def create_connection(self):
        try:
            self.conn = _sqlite3.connect(self.db_File)
            self.cur = self.conn.cursor()
        except Error as e:
            print(e)

    def create_teams_table(self):
        command = 'create table teams(name CHAR(20) not null, players CHAR(20) not null, value INTEGER not null)'
        self.cur.execute(command)

    def create_players_table(self):
        command = 'create table players(Name CHAR(20) not null,Designation CHAR(20),Points INTEGER)'
        self.cur.execute(command)

    def insert_player_records(self):
        records = pd.read_csv(r'/home/himanshuchauhan/Desktop/Python-Fantasy-Cricket-Game/PlayerData.csv')
        recordList = records.values.tolist()
        for record in recordList:
            self.cur.execute('insert into players values(?,?,?)', (record[0], record[1], record[2]))
            self.conn.commit()

    def create_match_table(self):
        command = 'create table match (Player CHAR(20), Scored INTEGER,Faced INTEGER,Sixes INTEGER,Bowled INTEGER,' \
                  'Maiden INTEGER,Given INTEGER, Wkts INTEGER, Catches INTEGER, Stumping INTEGER, RunOut INTEGER) '
        self.cur.execute(command)

    def create_stat_table(self):
        command = "create table stats (Player CHAR(20), Matches INTEGER, Runs INTEGER, Balls INTEGER, '100s' INTEGER, '50s' INTEGER," \
                  "SR INTEGER, BatAvg INTEGER, Wickets INTEGER,BowlAvg INTEGER,Designation CHAR(3))"
        self.cur.execute(command)

    def insert_stat_records(self):
        records = pd.read_csv(r'/home/himanshuchauhan/Desktop/Python-Fantasy-Cricket-Game/StatData.csv')
        recordsList = records.values.tolist()
        for record in recordsList:
            self.cur.execute('insert into stats values(?,?,?,?,?,?,?,?,?,?,?)', (record[0], record[1], record[2],
                                                                                 record[3], record[4], record[5],
                                                                                 record[6], record[7], record[8],
                                                                                 record[9], record[10]
                                                                                 ))
            self.conn.commit()


if __name__ == '__main__':
    dbObject = DbFiles()
    dbObject.create_connection()
    dbObject.create_teams_table()
    dbObject.create_players_table()
    dbObject.insert_player_records()
    dbObject.create_match_table()
    dbObject.create_stat_table()
    dbObject.insert_stat_records()
