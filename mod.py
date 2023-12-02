from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print("BASE_DIR: ", BASE_DIR)

db_file = BASE_DIR / 'db.sqlite3'

# # Check file permissions
print(f'Original permissions: {oct(db_file.stat().st_mode)[-3:]}') 

# # Set permissions to allow read and write  
import stat
db_file.chmod(db_file.stat().st_mode | stat.S_IRUSR | stat.S_IWUSR)

# # Verify permissions changed
print(f'New permissions: {oct(db_file.stat().st_mode)[-3:]}')