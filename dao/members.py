TABLE_NAME = "members"
# 0 - guild
# 1 - id
# 2 - nickname
# 3 - points
# 4 - last_submission_time
# 5 - last_submission

# The nickname column is only used for looking at the database directly, it will never be used in the business
def insert(cursor, guild, member_id, nickname, points, last_submission_time, last_submission):
    cursor.execute(f"INSERT INTO {TABLE_NAME} (guild, id, nickname, points, last_submission_time, last_submission) values(%s, %s, %s, %s, %s, %s)",
        [guild, member_id, nickname, points, last_submission_time, last_submission])

def update(cursor, guild, member_id, nickname, points, last_submission_time, last_submission):
    cursor.execute(f"UPDATE {TABLE_NAME} SET nickname=%s, points=%s, last_submission_time=%s, last_submission=%s WHERE guild=%s AND id=%s",
        [nickname, points, last_submission_time, last_submission, guild, member_id])

def select(cursor, guild_id, member_id):
    cursor.execute(f"SELECT guild, id, nickname, points, last_submission_time, last_submission FROM {TABLE_NAME} where  guild=%s AND id=%s",
        [guild_id, member_id])
    return cursor.fetchone()

def all(cursor):
    cursor.execute(f"SELECT guild, id, nickname, points, last_submission_time, last_submission FROM {TABLE_NAME}")
    return cursor.fetchone()

def rank(cursor, guild_id, member_id):
    cursor.execute(f"SELECT guild, id, ROW_NUMBER() OVER(ORDER BY points DESC) FROM {TABLE_NAME} where guild=%s AND id=%s",
        [guild_id, member_id])
    return cursor.fetchone()