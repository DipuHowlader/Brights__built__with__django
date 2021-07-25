document.addEventListener('DOMContentLoaded',() => {
	const menu = document.querySelector('.menu');
	const nav = document.querySelector('.dummy-nav');
	const exit = document.querySelector('.exit');

	menu.addEventListener('click', () =>{
		nav.style.right = '0'
	})

	exit.addEventListener('click',() =>{
		nav.style.right = '-120%'
	})
	
});


