# Servfolio

**Servfolio** is a Django-powered web application that enables users to create and manage a personal portfolio of services and projects without having the knowledge in programming. Designed for freelancers, professionals, or entrepreneurs, Servfolio allows users to showcase the services they offer and visually present the work they’ve done via an intuitive and customizable interface.

The application features full user authentication, service and project creation, image uploads, and a responsive layout for both desktop and mobile devices. This makes it easy for users to promote their work online through a clean and professional portfolio page, hosted on a personal URL like `/servfolio/<username>/`.

---

## 💡 Distinctiveness and Complexity

### How Servfolio Stands Out

Servfolio is distinct from all of the CS50W projects due to its **core purpose, structure, and layered functionality**.

Unlike the social network project (Project 4) or the e-commerce platform (Project 2), Servfolio is neither social nor commercial in nature. It does not rely on user-to-user interactions or buying/selling flows. Instead, it focuses on **self-promotion, personal branding, and professional presentation**, filling a unique use-case niche.

This app was not derived from or inspired by any of the course projects. Rather, it is a personal solution to a real-world problem — the need for a structured and attractive way to showcase one’s work as a service provider or freelancer without having the knowledge in programming.

### Complexity

Servfolio involves multiple layers of relational data. Users can create multiple services, and each service can have multiple associated projects. Projects include images, descriptions, and belong to both a service and a user. This multi-model architecture introduces non-trivial complexity in handling:

- **Custom user filtering logic**: Users can only view or edit their own services and projects.
- **Django ORM relationships**: Projects are associated with specific services, which in turn are tied to a specific user.
- **Form customization**: Forms are dynamically filtered based on the logged-in user context.
- **Dynamic URL resolution**: Every user has a clean and predictable portfolio route, e.g., `/servfolio/Teng/service/28/projects/`.
- **Reusable templates**: Clean structure using Django’s template inheritance for maintainability.
- **Secure model access**: Users can only view or edit their own data, with ownership logic implemented in both views and templates.

### Frontend Complexity

On the frontend, Servfolio uses **TailwindCSS, DaisyUI, and JavaScript for interactivity**, particularly for form handling and modal management. For example:

- A modal dialog is used for adding/editing projects without navigating away from the page.
- JavaScript dynamically sets form actions and pre-fills fields when editing.
- Proper cleanup ensures no data leaks between form submissions.

The design is fully mobile-responsive using TailwindCSS, and interface components adapt fluidly to different screen sizes.

---

## 📁 File Breakdown

- `mysite/models.py`: Contains `Service`, `Project`, and `Social` models, all linked via `ForeignKey` relationships.
- `mysite/forms.py`: Contains custom `ModelForm`s.
- `mysite/views.py`: Contains class-based views for listing, creating, updating, and deleting services, projects, and socials.
- `mysite/urls.py`: URL configurations for user-specific and resource-specific routes.
- `mysite/templates/portfolio/`: Contains Django templates:
    - `project.html`: Lists all projects for a service.
    - `service.html`: Displays services owned by a user.
    - `social.html`: Lists social links with edit and delete controls.
- `mysite/templates/`: Contains Django templates:
    - `base_portfolio.html`: Base layout for portfolio inherited by other pages.
    - `base.html`: Base layout inherited by other pages.
- `mysite/static/`: Holds optional custom CSS , JavaScript files and SVGs.
- `mysite/templatetags/` : Contains custom template tags and filters used across the application's HTML templates. 
- `media/`: User-uploaded images for projects (served during development).
- `README.md`: This documentation.
- `requirements.txt`: Python dependencies required to run the project.
- `utils/context_processors.py` : Contains custom context processors that inject additional context variables globally into all templates.

---

## ▶️ How to Run the Application

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd servfolio
