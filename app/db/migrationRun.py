from app.db.migrations import movies
from core.db.migration import migrationRun

migrations=[
    movies()
]

MR=migrationRun(migrations);
MR.migrate()

