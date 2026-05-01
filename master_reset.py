from app import app, db, User, Post
from werkzeug.security import generate_password_hash

# 1. Define the Missing Team (UPDATED with Harsha and Sumanth)
team_data = [
    {"u": "Rohit", "bio": "Lead Systems Architect.", "lvl": 99},
    {"u": "Harvar", "bio": "Visual Architect.", "lvl": 50},
    {"u": "Dinesh", "bio": "UI/UX Magician.", "lvl": 45},
    {"u": "Bhargav", "bio": "AI Logic Master.", "lvl": 40},
    {"u": "harsha", "bio": "Weapon Artist.", "lvl": 35},
    {"u": "sumanth", "bio": "Environment Artist.", "lvl": 20},
    {"u": "Vinay", "bio": "Networking Engineer.", "lvl": 15},
    {"u": "Charan", "bio": "Gameplay Programmer.", "lvl": 10},
]

# 2. Define the Missing Assets (ADDED the missing comma)
assets = [
    {"u": "Rohit", "t": "ULTIMATE HORROR SYSTEM", "f": "DOOR 1.mp4", "p": 1500, "d": "Full jumpscare logic."},
    {"u": "Harvar", "t": "ADVANCED CAR PHYSICS", "f": "car.mp4", "p": 2500, "d": "Drifting and suspension."},
    {"u": "Dinesh", "t": "RPG INVENTORY UI", "f": "human.mp4", "p": 899, "d": "Drag and drop inventory."},
    {"u": "Bhargav", "t": "DRONE AI SWARM", "f": "drone.mp4", "p": 1200, "d": "Autonomous pathfinding."},
    {"u": "harsha", "t": "FPS WEAPON PACK", "f": "tuuent.mp4", "p": 3000, "d": "10 High-fidelity weapons."},
    {"u": "sumanth", "t": "OPEN WORLD MAP", "f": "damage taker cube.mp4", "p": 4500, "d": "8x8km Landscape."},
    {"u": "Vinay", "t": "MULTIPLAYER CHAT", "f": "up jumping portal.mp4", "p": 600, "d": "Global voice chat."},
    {"u": "Charan", "t": "PARKOUR SYSTEM V2", "f": "human.mp4", "p": 1800, "d": "Climbing and vaulting."}
]

with app.app_context():
    print("🔧 STARTING MASTER RESET...")

    # --- PHASE 1: RESTORE USERS ---
    print("\n👤 Checking Users...")
    for member in team_data:
        user = User.query.filter_by(username=member['u']).first()
        if not user:
            new_user = User(
                username=member['u'], 
                display_name=member['u'],
                email=f"{member['u'].lower()}@voidhub.com", # Updated to Void Hub
                password=generate_password_hash("123", method='pbkdf2:sha256'),
                is_premium=True,
                premium_type='seller',
                level=member['lvl'],
                bio=member['bio'],
            )
            db.session.add(new_user)
            print(f"   [+] Created User: {member['u']}")
        else:
            print(f"   [OK] Found User: {member['u']}")
    
    try:
        db.session.commit() # Save users so we can link videos to them
    except Exception as e:
        db.session.rollback()
        print("\n❌ DATABASE ERROR: Table schema is outdated!")
        print("👉 FIX: You must run 'python nuke_db.py' first to apply the latest database changes.")
        print(f"Details: {str(e)}")
        exit(1)

    # --- PHASE 2: RESTORE VIDEOS ---
    print("\n🎬 Checking Assets...")
    for a in assets:
        post = Post.query.filter_by(title=a['t']).first()
        if not post:
            creator = User.query.filter_by(username=a['u']).first()
            if creator:
                new_post = Post(title=a['t'], filename=a['f'], price=a['p'], desc=a['d'], author=creator, sold_count=a['p']//10)
                db.session.add(new_post)
                print(f"   [+] Restored Video: {a['t']}")
            else:
                print(f"   [ERROR] Could not find creator for {a['t']}")
        else:
            print(f"   [OK] Found Video: {a['t']}")

    try:
        db.session.commit()
        print("\n✅ MASTER RESET COMPLETE. RESTART YOUR SERVER.")
    except Exception as e:
        db.session.rollback()
        print(f"\n❌ ERROR during video restoration: {str(e)}")