<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='stylesheet.css') }}">
    
    
   
    <title>Search user's playlist!</title>
</head>
<body style="background-color: mediumseagreen !important;">
    <div class="header">
            <h1 class="word">Search user's playlist through search bar!</h1>
            <br><br><br>
            <div class="form_container">
                
                <form id = "myform" action="{{ url_for('index') }}" method="post">
                    <div class="test">
                        <div class="msg">{{ msg }}</div>
                      <input id="username" name="username" type="text" placeholder="Enter A Valid Profile Link" class="textbox"/></br></br>
                      <input id="check"  type="submit" class="btn" value="Search!"></br></br>
                    </div>
                    
                  </form>
            </div>
            
    </div>
    <script src="{{url_for('static', filename='functions.js')}}"></script>
</body>
</html>
