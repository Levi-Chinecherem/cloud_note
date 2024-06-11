
# Cloud-Based Note-Taking System

A modern cloud-based note-taking system built with Django and styled using Tailwind CSS. This application allows users to create, edit, view, and delete notes after logging in.

## Features

- User Authentication (Login, Logout, Signup)
- Create, Edit, View, and Delete Notes
- User-specific notes
- Responsive and modern UI

## Technologies Used

- Django
- Tailwind CSS
- SQLite (default for development, can be configured for other databases)
- Python 3.12.2

## Installation

### Prerequisites

- Python 3.12.2
- Node.js and npm

### Clone the Repository

```bash
git clone https://github.com/Levi-Chinecherem/cloud_note.git
cd cloud_note
```

### Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Install Node.js Dependencies

```bash
npm install
```

### Tailwind CSS Setup

```bash
python manage.py tailwind init
python manage.py tailwind install
python manage.py tailwind build
```

## Configuration

### Database Migration

```bash
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

## Running the Application

### Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

### User Authentication

- **Signup**: Create a new account.
- **Login**: Access your account.
- **Logout**: Log out of your account.

### Notes Management

- **Create Note**: Add a new note.
- **View Notes**: See a list of your notes.
- **Edit Note**: Modify an existing note.
- **Delete Note**: Remove a note from your list.

## Directory Structure

```
.
├── .venv/                      # Virtual environment
├── myproject/                  # Django project folder
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL configuration
│   └── ...
├── notes/                      # Notes app folder
│   ├── models.py               # Note model
│   ├── views.py                # Views for notes
│   ├── forms.py                # Forms for notes
│   ├── urls.py                 # URL configuration for notes
│   ├── templates/              # Templates folder
│   │   ├── base.html           # Base template
│   │   ├── notes/              # Notes templates
│   │   │   ├── note_list.html  # List notes template
│   │   │   ├── note_detail.html# Note detail template
│   │   │   ├── note_form.html  # Create/edit note template
│   │   │   └── note_confirm_delete.html  # Delete note template
│   └── ...
├── templates/                  # Project-wide templates folder
│   ├── registration/           # Authentication templates
│   │   ├── login.html          # Login template
│   │   ├── logout.html         # Logout template
│   │   └── signup.html         # Signup template
├── static/                     # Static files folder
│   └── ...
├── tailwind.config.js          # Tailwind CSS configuration
├── package.json                # Node.js dependencies
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Custom Template Filters

A custom template filter is used to add CSS classes to form fields.

### Define the Filter

Create `templatetags/custom_filters.py`:

```python
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})
```

Load the filter in your template:

```html
{% load custom_filters %}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries, please reach out to [lchinecherem2018@gmail.com].
