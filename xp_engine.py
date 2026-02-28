import sqlite3
from database import DB_NAME

# -----------------------------------
# LEVEL CALCULATION SYSTEM
# -----------------------------------

def calculate_level(total_xp):
    level = 1
    xp_needed = 100

    total_xp = int(total_xp)

    while total_xp >= xp_needed:
        total_xp -= xp_needed
        level += 1
        xp_needed = int(xp_needed * 1.5)

    return level


def current_level_progress(total_xp):
    level = 1
    xp_needed = 100

    remaining_xp = int(total_xp)

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


# -----------------------------------
# XP UPDATE SYSTEM
# -----------------------------------

def add_xp(user_id, xp_amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT total_xp FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return None

    current_xp = int(result[0])
    new_total = current_xp + int(xp_amount)

    print("USER ID:", user_id)
    print("CURRENT XP:", current_xp)
    print("XP ADDING:", xp_amount)
    print("NEW TOTAL:", new_total)

    cursor.execute(
        "UPDATE users SET total_xp = ? WHERE id = ?",
        (new_total, user_id)
    )

    conn.commit()
    conn.close()

    return new_total