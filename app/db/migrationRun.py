from app.db.migrations import movies,stars,starsinmovies,series
from core.db.migration import migrationRun

migrations=[
    movies(),
    stars(),
    starsinmovies(),
    series()
]

MR=migrationRun(migrations);
MR.migrate()

