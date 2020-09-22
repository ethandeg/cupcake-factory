const cupcakeBlock = document.querySelector('#cupcake-block');
const addForm = document.querySelector('#addForm');

async function getAllCupcakes() {
	res = await axios.get('/api/cupcakes');
	cupcakes = res.data.cupcakes;
	for (let cupcake of cupcakes) {
		const newDiv = document.createElement('div');
		newDiv.classList.add('flex-div');
		newDiv.innerHTML = `<h5>${cupcake.flavor}</h5>
                                <img src = "${cupcake.image}" class = "top-image">
                                <h3>${cupcake.size}</h3>
                                <h3>${cupcake.rating}</h3>
                                <button class = "editButton" data-id = ${cupcake.id}>Edit</button>
                                <button class = "deleteButton" data-id = ${cupcake.id}>Delete</button>
                                `;

		newDiv.setAttribute('data-id', `${cupcake.id}`);
		cupcakeBlock.appendChild(newDiv);
	}
}

function handleButtonHandler(e) {
	document.addEventListener('click', (e) => {
		if (e.target.className === 'editButton') {
			let target = Number(e.target.dataset.id);
			console.log(target);
			return target;
			// create edit function
		}
		if (e.target.className === 'deleteButton') {
			let target = Number(e.target.dataset.id);
			console.log(e.path);
			removeDiv = e.path[1];
			deleteCupcake(target);
			removeDiv.remove();
		}
		if (e.target.innerText === 'Add Cupcake') {
			const addForm = document.querySelector('#addForm');
			cupcakeBlock.classList.toggle('no-display');
			addForm.classList.toggle('no-display');
		}

		if (e.target.innerText === 'Cancel') {
			const addForm = document.querySelector('#addForm');
			cupcakeBlock.classList.toggle('no-display');
			addForm.classList.toggle('no-display');
		}
	});
}

async function deleteCupcake(id) {
	res = await axios.delete(`/api/cupcakes/${id}`);
}

addForm.addEventListener('submit', async function(e) {
	e.preventDefault();
	let flavor = document.querySelector('#flavor').value;
	let size = document.querySelector('#size').value;
	let rating = Number(document.querySelector('#rating').value);
	let image = document.querySelector('#image').value;
	let token = document.querySelector('#csrf_token').value;
	const res = await axios.post('api/cupcakes', {
		flavor,
		rating,
		size,
		image,
		csrf_token: token
	});

	console.log(res);
});

handleButtonHandler();

getAllCupcakes();
