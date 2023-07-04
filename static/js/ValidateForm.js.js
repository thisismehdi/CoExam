const form=document.getElementById("form");
const username=document.getElementById("username");
const email=document.getElementById("email");
const password=document.getElementById("password");
const password2=document.getElementById("password2");
const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
const passwordPAtter=/^[a-zA-Z0-9]{8,}$/;
const eyes=document.querySelectorAll("i");
////
function ShowErr(input,message)
{
  const father=input.parentElement;
  const small=father.querySelector("small");
  father.classList.add("error");
  small.textContent=message;
  
}
/*/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(myForm.emailAddr.value)*/
function showSucces(input){
  const father=input.parentElement;
  father.classList.add("succes");
}
form.addEventListener("submit",(e)=>{
  e.preventDefault();
  /////validtation of username
  ////validation of email
  if(email.value==='')
  {
    ShowErr(email,'Email is required');
  }else if(!emailPattern.test(email.value)){
    ShowErr(email,'Invalid email')
  }else{
    showSucces(email);
  }
  ///validation of password
  if(password.value==='')
  {
    ShowErr(password,'password is required');
  }else if(password.value.length < 8){
    ShowErr(password,'Password should have at least 8 caracters')
  }else if(!passwordPAtter.test(password.value)){
    ShowErr(password,'Password should contains digits and symblos')
  }else{
    showSucces(password);
  }
  ///second password part
  if(password2.value==='')
  {
    ShowErr(password2,'password2 is required');
  }else if(password2.value!==password.value){
    ShowErr(password2,"Passwords doesn't match");
    ShowErr(password,"Passwords doesn't match")
  }else{
    showSucces(password2);
  }
  form.submit()
});

Array.from(eyes).forEach((item)=>{
  
  item.addEventListener("click",()=>{
    const father=item.parentElement;
    if(father.querySelector("input").getAttribute("type")==='password')
    {
      father.querySelector("input").type="text";
    }
    else{
      father.querySelector("input").type="password";
    }
  })
})
 