const myDiv = document.createElement(tagName:'div');
myDiv.className = 'buttons';
myDiv.style.background = 'coral';
myDiv.style.textAlign = 'center';
let i=0;

['Додати в друзі', 'Написати повідомлення', 'Запропонувати роботу'].map(buttonName => {
    let button = document.createElement(tagName:'button');
   // button.className = "col-md-8";
    button.innerText = buttonName;
    button.style.margin = '5px'
    myDiv.appendChild(button);
})

document.getElementsByTagName(qualifiedName:'body')[0].appendChild(myDiv);