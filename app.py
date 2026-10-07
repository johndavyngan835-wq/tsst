from flask import Flask

app = Flask(name)

PAGE = """
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mon service en ligne</title>
  <style>
    body { font-family: sans-serif; text-align: center; padding: 15vh 1rem; background: #0f172a; color: #f8fafc; }
    p { color: #94a3b8; }
  </style>
</head>
<body>
  <h1>Mon premier service est en ligne 🚀</h1>
  <p>Déployé sur Render avec Flask.</p>
</body>
</html>
"""

@app.route("/")
def home():
    return PAGE
