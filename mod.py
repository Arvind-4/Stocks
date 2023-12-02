import stat
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_DIR = BASE_DIR / 'database'
db_file = DATABASE_DIR / 'db.sqlite3'

# Check file permissions
print(f'Original permissions for {db_file}: {oct(db_file.stat().st_mode)[-3:]}')
print(f'Original permissions  for {BASE_DIR}: {oct(BASE_DIR.stat().st_mode)[-3:]}')
print(f'Original permissions for {DATABASE_DIR}: {oct(DATABASE_DIR.stat().st_mode)[-3:]}') 

# Set permissions to allow read and write  
db_file.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  
BASE_DIR.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
DATABASE_DIR.chmod(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

# Verify permissions changed
print(f"New Permissions for {db_file}: {oct(db_file.stat().st_mode)[-3:]}")
print(f"New Permissions for {BASE_DIR}: {oct(BASE_DIR.stat().st_mode)[-3:]}")
print(f"New Permissions for {DATABASE_DIR}: {oct(DATABASE_DIR.stat().st_mode)[-3:]}")