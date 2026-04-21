document.addEventListener("DOMContentLoaded", () => {
	const form = document.querySelector("form");
	const action = form ? form.getAttribute("action") : "";

	setupButtonNavigation();
	highlightCurrentSection();

	if (!form) {
		return;
	}

	if (action === "/create") {
		setupCreateValidation(form);
	}

	if (action === "/edit") {
		setupEditValidation(form);
	}

	if (action === "/del") {
		setupDeleteValidation(form);
	}
});

function setupButtonNavigation() {
	const buttons = document.querySelectorAll("button");

	buttons.forEach((button) => {
		const anchor = button.querySelector("a[href]");
		if (!anchor) {
			return;
		}

		button.addEventListener("click", () => {
			window.location.href = anchor.getAttribute("href");
		});
	});
}

function highlightCurrentSection() {
	const path = window.location.pathname;
	const mapping = {
		"/create": ".adicionar-post",
		"/create.html": ".adicionar-post",
		"/edit": ".editar-post",
		"/edit.html": ".editar-post",
		"/del": ".deletar-post",
		"/del.html": ".deletar-post"
	};

	const selector = mapping[path];
	if (!selector) {
		return;
	}

	const activeButton = document.querySelector(selector);
	if (activeButton) {
		activeButton.style.outline = "3px solid rgba(255, 255, 255, 0.85)";
		activeButton.style.outlineOffset = "2px";
	}
}

function setupCreateValidation(form) {
	const fields = ["titulo", "resumo", "conteudo", "autor"];
	const inputs = fields.map((name) => form.querySelector(`input[name="${name}"]`)).filter(Boolean);

	if (inputs.length > 0) {
		inputs[0].focus();
	}

	form.addEventListener("submit", (event) => {
		const emptyField = inputs.find((input) => input.value.trim().length < 3);
		if (emptyField) {
			event.preventDefault();
			alert("Preencha todos os campos com pelo menos 3 caracteres.");
			emptyField.focus();
			return;
		}
	});
}

function setupEditValidation(form) {
	const idInput = form.querySelector("#id") || form.querySelector("input[name='id']");
	const editableInputs = ["titulo", "resumo", "conteudo", "autor"]
		.map((name) => form.querySelector(`input[name="${name}"]`))
		.filter(Boolean);

	if (idInput) {
		idInput.focus();
	}

	form.addEventListener("submit", (event) => {
		if (!idInput || !/^\d+$/.test(idInput.value.trim())) {
			event.preventDefault();
			alert("Informe um ID valido (somente numeros).");
			if (idInput) {
				idInput.focus();
			}
			return;
		}

		const hasContentToUpdate = editableInputs.some((input) => input.value.trim().length > 0);
		if (!hasContentToUpdate) {
			event.preventDefault();
			alert("Preencha ao menos um campo para editar o post.");
		}
	});
}

function setupDeleteValidation(form) {
	const idInput = form.querySelector("input[name='id']");
	if (idInput) {
		idInput.focus();
	}

	form.addEventListener("submit", (event) => {
		if (!idInput || !/^\d+$/.test(idInput.value.trim())) {
			event.preventDefault();
			alert("Informe um ID valido (somente numeros).");
			if (idInput) {
				idInput.focus();
			}
			return;
		}

		const confirmed = window.confirm("Tem certeza que deseja excluir este post?");
		if (!confirmed) {
			event.preventDefault();
		}
	});
}
