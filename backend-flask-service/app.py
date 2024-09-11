<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poof! Vanishing Whitepaper</title>
    <style>
        body { text-align: center; margin-top: 50px; font-family: Arial, sans-serif; }
        .content { width: 80%; margin: 0 auto; }
    </style>
</head>
<body>
    <h1>Poof! Vanishing Whitepaper</h1>
    <div class="content" id="endpoint">Загружаем магию...</div>
    <button onclick="loadWhitepaper()">Обновить Whitepaper</button>
    <script>
        async function loadWhitepaper() {
            const response = await fetch('http://localhost:3000/endpoint');
            const data = await response.text();
            document.getElementById('endpoint').textContent = data;
        }
        loadWhitepaper(); // Load whitepaper on page load
    </script>
</body>
</html>
