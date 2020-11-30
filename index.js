// const quanity = 4;
// let b = 3;
// console.log("hello");
// fetch("/file");
// console.log("i am here");
// console.log("document", document);
function nameSubmitted() {
  console.log("submit pressed");
  let inputName = $("#name");
  let mainTitle = $(".main-title");
  console.log('mainTitle', mainTitle)
  for(let i=0;i<mainTitle.length;i++){
       mainTitle[i].innerText = "Good Morning, " + inputName[0].value;
  }

  console.log("inputName[0]", inputName[0].value);
}

function printName(){
    let inputName = $("#name");
    console.log("inputName[0]", inputName[0].value);
}

let submitBtn = $("#submit");
submitBtn[0].addEventListener("click", nameSubmitted);

// submitBtn.addEventListener("mouseover", function () {
//   console.log("mouse over submit");
// });
