from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
    <html>
    <head>
        <title>¿Laurita bella quieres ser mi novia?</title>
        <script>
            function onNoClick() {
            
                const noButton = document.getElementById('noButton');
                const titlePosition = document.querySelector('h1').getBoundingClientRect();
                const minX = titlePosition.left - 200;  // Rango horizontal de 400 píxeles alrededor del título
                const maxX = titlePosition.right + 200;
                const minY = titlePosition.top - 200;   // Rango vertical de 400 píxeles alrededor del título
                const maxY = titlePosition.bottom + 200;

                const newPositionX = Math.max(minX, Math.min(maxX - noButton.clientWidth, Math.random() * (maxX - minX)));
                const newPositionY = Math.max(minY, Math.min(maxY - noButton.clientHeight, Math.random() * (maxY - minY)));

                noButton.style.left = newPositionX + 'px';
                noButton.style.top = newPositionY + 'px';
            }
        </script>
        <style>
            body {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }

            h1 {
                margin-bottom: 30px;
            }

            .button-container {
                display: flex;
                align-items: center;
                gap: 20px;
                position: relative;
            }

            .button {
                font-size: 24px;
                cursor: pointer;
                width: 150px;
                height: 50px;
                position: relative;
            }
        </style>
    </head>
    <body>
        <h1>¿Quieres ser mi novia?</h1>
        <div class="button-container">
            <button class="button" onclick="alert('¡Muchas gracias por aceptar! Me haces el hombre más feliz del mundo, que bueno que estemos tan enamorados.');">Sí</button>
            <button id="noButton" class="button" onclick="onNoClick()">No</button>
        </div>
    </body>
    </html>
    ''')


if __name__ == '__main__':
    app.run(debug=True)







