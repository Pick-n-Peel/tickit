<p align="center">
<img alt="tickit" src="docs/assets/logo-transparent.png" width="400">
</p>

---

TickIt is a simple to-do list application built by the Pick'n Peel team (Anna B. Banana and Dillon P. Pickle).

## Frontend

There are two frontend folders: the `frontend` folder contains the react version, and `frontend-vue` contains the vue version. Both of these versions are built using the [Vite](https://vite.dev) build tool, and can be spun up locally with the `npm run dev` command.

### React

- Routing: [Tanstack Router](https://tanstack.com/router/latest) for file-based routing
- Styling & Components: [TailwindCSS](https://tailwindcss.com) + [DaisyUI](daisyui.com)

### Vue

- Routing: [Vue Router](https://router.vuejs.org)
- Styling & Components: [TailwindCSS](https://tailwindcss.com) + [DaisyUI](daisyui.com)

## Backend Stack

The backend was created using Django and Django Rest Framework (DRF) and the database currently uses SQL lite. It can be spun up locally with the 'python backend/manage.py runserver' command.

- Django: [Django]https://docs.djangoproject.com/en/5.2/
- Django rest [Django Rest Framework]Framework: https://www.django-rest-framework.org/

## Pre-commit

Pre-commit has been setup for this repo. Pre-commit hooks can be setup to be run on every commit by running 'pre-commit install'.
