<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/4a5f59fc5b.js" crossorigin="anonymous"></script> 
    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}"/>
    <title>TRAVEL WEBSITE</title>
</head>

<body>

<header class='header'>
        
    <nav class='navbar'>
            
        <div class="container">
                
            <div class="logo">
                <img src="./static/img/logo.png">
            </div>
                
            <ul class='nav-items'>
                <li class="nav-item"><a href="./indexhome.html">Home</a></li>
                
                <li class="nav-item"><a href="#about">About</a></li>
                
                <li class="nav-item"><a href="international">Your Trip</a></li>
                
                <li class="nav-item"><a href="#Helpline">Helpline</a></li>
                
                <li class="nav-item"><a href="signin">Sign up/in</a></li>

                <li class="nav-item"><a href="" onclick="alert('You are in Admin page.')">Admin</a></li>
            </ul>
            
        </div>
        
    </nav>

</header>

<div class="maindata">
    
<table><tr>
    
    <td class="table_row">Name</td>
    <td class="table_row">Email</td>
    <td class="t_row_lst">Password</td>

</table>

<table>

	<td class="table_col"><a href="" class="btn btn-primary table_btn">delete</a></td>
    <td class="table_col"><a href="" class="btn btn-primary table_btn">edit</a></td>
    <td class="table_col"><a href="" class="btn btn-primary table_btn">insert</a></td> 
    

</table>

</div>

</body>

</html>