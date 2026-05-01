from app import app, db

with app.app_context():
    print("⚠️ DROPPING OLD TABLES...")
    db.drop_all()  # This deletes the old schema that doesn't have void_id
    
    print("✅ CREATING NEW TABLES...")
    db.create_all() # This builds the new schema WITH void_id
    
    print("🚀 DATABASE READY FOR MASTER RESET!")