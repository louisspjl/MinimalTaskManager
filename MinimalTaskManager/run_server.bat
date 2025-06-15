@echo off
python app.py
if ERRORLEVEL 1 (
    echo.
    echo Une erreur est survenue.
    echo Appuie sur une touche pour fermer la fenêtre...
    pause >nul
) else (
    echo Serveur arrêté normalement.
    pause
)
