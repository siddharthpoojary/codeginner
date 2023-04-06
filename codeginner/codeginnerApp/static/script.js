function login(){
    document.getElementById("login").style.display="block";
    document.getElementById("body-cntr").style.opacity=0.5;
}

function signUp(){
    document.getElementById("signup").style.display="block";
    document.getElementById("body-cntr").style.opacity=0.5;
}

function createChapter(){
    document.getElementById("course_content").style.display="block";
    document.getElementById("body-cntr").style.opacity=0.5;
}

function cancel(){
    var login_container = document.getElementById('login');
    var signup_container = document.getElementById('signup');
    var back = document.getElementById('body-cntr');
    login_container.style.display = 'none';
    signup_container.style.display = 'none';
    back.style.opacity=1;
}

function cancel_courseForm(){
    var course = document.getElementById("course_content");
    var back = document.getElementById('body-cntr');
    course.style.display = 'none';
    back.style.opacity=1;
}
function scrolltop(){
    window.scrollTo(0, 0);
}