from app import app, db, User, Post

# Data to restore
assets = [
    {"u": "Rohit", "t": "ULTIMATE HORROR SYSTEM", "f": "DOOR 1.mp4", "p": 1500, "d": "Full jumpscare logic."},
    {"u": "Harvar", "t": "ADVANCED CAR PHYSICS", "f": "car.mp4", "p": 2500, "d": "Drifting and suspension."},
    {"u": "Dinesh", "t": "RPG INVENTORY UI", "f": "human.mp4", "p": 899, "d": "Drag and drop inventory."},
    {"u": "Bhargav", "t": "DRONE AI SWARM", "f": "drone.mp4", "p": 1200, "d": "Autonomous pathfinding."},
    {"u": "Bora", "t": "FPS WEAPON PACK", "f": "tuuent.mp4", "p": 3000, "d": "10 High-fidelity weapons."},
    {"u": "Tarun", "t": "OPEN WORLD MAP", "f": "damage taker cube.mp4", "p": 4500, "d": "8x8km Landscape."},
    {"u": "Vinay", "t": "MULTIPLAYER CHAT", "f": "up jumping portal.mp4", "p": 600, "d": "Global voice chat."},
    {"u": "Charan", "t": "PARKOUR SYSTEM V2", "f": "human.mp4", "p": 1800, "d": "Climbing and vaulting."}
]

with app.app_context():
    print("🔧 STARTING REPAIR...")
    
    count = 0
    for a in assets:
        # Check if video exists
        if not Post.query.filter_by(title=a['t']).first():
            # Find the creator
            creator = User.query.filter_by(username=a['u']).first()
            if creator:
                post = Post(title=a['t'], filename=a['f'], price=a['p'], desc=a['d'], author=creator, sold_count=a['p']//10)
                db.session.add(post)
                count += 1
                print(f"   + Restored: {a['t']}")
            else:
                print(f"   ⚠️ User {a['u']} missing. Cannot create post.")
    
    db.session.commit()
    print(f"✅ REPAIR COMPLETE. Restored {count} videos.")