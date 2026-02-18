import sqlite3
from database import DB_NAME


# ---------------------------
# LEVEL CALCULATION
# ---------------------------

def calculate_level(total_xp):
    level = 1
    xp_needed = 100

    while total_xp >= xp_needed:
        total_xp -= xp_needed
        level += 1
        xp_needed = int(xp_needed * 1.5)

    return level


def current_level_progress(total_xp):
    level = 1
    xp_needed = 100
    remaining_xp = total_xp

    while remaining_xp >= xp_needed:
        remaining_xp -= xp_needed
        level += 1
        xp_needed = int(xp_needed * 1.5)

    progress_percent = (remaining_xp / xp_needed) * 100

    return {
        "level": level,
        "current_xp": remaining_xp,
        "xp_needed": xp_needed,
        "progress_percent": round(progress_percent, 2)
    }


# ---------------------------
# XP UPDATE FUNCTION
# ---------------------------

def add_xp(user_id, xp_amount, track=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT total_xp FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return None

    current_total_xp = result[0]
    new_total_xp = current_total_xp + xp_amount

    new_level = calculate_level(new_total_xp)

    # Update total XP + level
    cursor.execute("""
        UPDATE users 
        SET total_xp = ?, level = ?
        WHERE id = ?
    """, (new_total_xp, new_level, user_id))

    # Update specific track XP
    if track:
        cursor.execute(f"""
            UPDATE users
            SET {track}_xp = {track}_xp + ?
            WHERE id = ?
        """, (xp_amount, user_id))

    conn.commit()
    conn.close()

    return current_level_progress(new_total_xp)
