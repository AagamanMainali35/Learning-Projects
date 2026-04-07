function filter(type){
    let con = document.querySelectorAll('.filter');
    for (let i = 0; i < con.length; i++) {
        if (con[i].classList.contains(type)) {
            con[i].style.display = 'flex';
        } else {
            con[i].style.display = 'none';
        }
    }
}
function button(){
    let buton = document.querySelectorAll('.buton');
    let con = document.querySelectorAll('.filter');

    for (let i = 0; i < buton.length; i++) {
        buton[i].onclick = () => {
            let value = buton[i].id;
            if (value === 'back') {
                // Show all filters
                for (let j = 0; j < con.length; j++) {
                    con[j].style.display = 'flex';
                }
            } else {
                filter(value);
            }
        };
    }
}

button();