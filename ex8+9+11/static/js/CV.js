function printMyName(){
    console.log("Roee Feldman");
}


function Namevalidation() {
    var check = 0;
    for ( let i=1; i<4; i++){
        var x = "id"+i;
        console.log(x);
        var inpObj = document.getElementById(x);
        if (!inpObj.checkValidity()) {
            check = check +1 ;
            inpObjBAD = document.getElementById(x);
            console.log(check) 
        //  document.getElementById("demo").innerHTML = inpObj.validationMessage;
        } 
        // else {
        //  document.getElementById("demo").innerHTML = "Input OKK";
        // }

        // const inpObj2 = document.getElementById("id2");
        // if (!inpObj2.checkValidity()) {
        //  document.getElementById("demo2").innerHTML = inpObj2.validationMessage;
        // } 
        // else {
        //  document.getElementById("demo2").innerHTML = "Input OKK";
        // }
    }
    console.log("check is" ,check);
    if (check == 0 ){
        document.getElementById("demo").innerHTML = "Input OKK";
    }
    else{
        document.getElementById("demo").innerHTML = inpObjBAD.validationMessage;
        console.log("got into else");
    }

}


// ex 11

function return_users(){
    let id = document.getElementById("frontend").value;

    fetch('https://reqres.in/api/users/'+id).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {

    const p = document.querySelector("p");
    p.innerHTML = `
    <img src="${response_obj_data.avatar}" alt="Profile Picture"/><br>
    id: ${response_obj_data.id}<br>
    email: ${response_obj_data.email}<br>
    ${response_obj_data.first_name} ${response_obj_data.last_name}<br>
    url: ${response_obj_data.support}<br>
    <a href="mailto:${response_obj_data.email}">Send Email</a>
    `;

}