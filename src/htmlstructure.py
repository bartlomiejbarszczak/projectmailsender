def htmltext(text):
    htmltextmessage = """\
    <!DOCTYPE html>
    <html>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Meow+Script&display=swap" rel="stylesheet">
        <body style = "background-image: url('http://lotgrafix.com/wp-content/uploads/2019/04/34-asana-color-gradient.jpg'); border-radius: 25px; margin-top: 25px; margin-bottom: 25px; margin-left: 25px; margin-right: 25px; text-align: center;">
            <h1 style = "font-size: 75px; font-family: 'Courier New', cursive; color: rgb(255, 255, 255); border-bottom: 1.5px solid; text-align: center;"></h1>
            <div style = "font-size: 50px; font-family: 'Courier New', cursive; color: rgb(255, 255, 255);">""" + text + """</div>
            <div style = "padding-top: 40px; font-size: 25px; font-family: 'Meow Script', cursive; color: rgb(255, 255, 255);"> ~Ktoś mądry</div>
            <h1 style = "font-size: 75px; font-family: 'Courier New', cursive; color: rgb(255, 255, 255); border-bottom: 1.5px solid; text-align: center;"></h1>
        </body>
    </html>
    """
    return htmltextmessage
