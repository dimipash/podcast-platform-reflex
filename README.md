# Podcast Platform Reflex

This is a web application built with Reflex, designed to serve as a podcast platform. The project is currently in progress.

## Project Structure

- `rxconfig.py`: Configuration file for the Reflex application.
- `podcast_platform_reflex/podcast_platform_reflex.py`: Main application file, defining the home page and basic state.
- `podcast_platform_reflex/layout.py`: Defines the root layout of the application, including the navigation bar.
- `podcast_platform_reflex/ui/nav.py`: Contains the implementation of the navigation bar component.
- `podcast_platform_reflex/pages/`: Directory for different pages of the application (e.g., `about.py`, `pricing.py`, `contact/page.py`).
- `assets/`: Static assets like `favicon.ico` and `logo.jpg`.

## Features (Planned/In Progress)

- **Home Page**: A welcoming page with a dynamic title.
- **Navigation Bar**: Responsive navigation for desktop and mobile.
- **Contact Page**: Implemented with a form to allow users to submit messages, including their name and message content. Submitted messages are stored in a database.
- **About Page**: 
- **Pricing Page**: 

## Getting Started

To run this project locally:

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Reflex app**:
    ```bash
    reflex run
    ```

This will start the development server, and you can access the application in your browser.
