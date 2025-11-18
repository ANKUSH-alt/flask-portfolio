# Flask Portfolio with SQL Database

A modern, animated portfolio website built with Flask and SQLAlchemy, featuring a complete SQL database backend for managing projects, skills, and contact messages.

## Features

- ✨ Smooth animations and transitions
- 📱 Fully responsive design
- 🗄️ SQL database integration (SQLite)
- 📧 Contact form with database storage
- 🎨 Modern gradient design
- 🚀 RESTful API endpoints
- 📊 Project and skills management

## Project Structure

```
flask2026/
├── app.py                 # Main Flask application with database models
├── init_db.py            # Database initialization script
├── requirements.txt      # Python dependencies
├── templates/
│   └── portfolio.html    # Main portfolio template
├── static/
│   └── portfolio.html    # Static backup of portfolio
└── portfolio.db          # SQLite database (created after first run)
```

## Installation

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install Flask==2.3.3
pip install Flask-SQLAlchemy==3.0.5
pip install SQLAlchemy==2.0.20
```

### 3. Initialize Database

```bash
python init_db.py
```

This will:
- Create the SQLite database file (`portfolio.db`)
- Create all necessary tables
- Populate sample projects and skills

### 4. Run the Application

```bash
python app.py
```

The application will start at `http://127.0.0.1:5000/`

## Database Models

### Project
```python
- id: Integer (Primary Key)
- title: String (100)
- description: String (500)
- technologies: String (200)
- link: String (200)
- created_at: DateTime
```

### Skill
```python
- id: Integer (Primary Key)
- category: String (50)
- name: String (100)
- proficiency: Integer (0-100)
```

### Contact
```python
- id: Integer (Primary Key)
- name: String (100)
- email: String (100)
- message: Text
- created_at: DateTime
```

## API Endpoints

### Projects
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Create a new project
- `GET /api/projects/<id>` - Get a specific project
- `PUT /api/projects/<id>` - Update a project
- `DELETE /api/projects/<id>` - Delete a project

### Skills
- `GET /api/skills` - Get all skills
- `POST /api/skills` - Create a new skill

### Contact
- `POST /api/contact` - Submit a contact message
- `GET /api/contact-messages` - Get all contact messages

## Usage Examples

### Add a Project
```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Project",
    "description": "A cool project",
    "technologies": "Flask, React",
    "link": "https://github.com/example/project"
  }'
```

### Add a Skill
```bash
curl -X POST http://localhost:5000/api/skills \
  -H "Content-Type: application/json" \
  -d '{
    "category": "Frontend",
    "name": "React",
    "proficiency": 85
  }'
```

### Submit Contact Message
```bash
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello!"
  }'
```

## Frontend Features

- **Smooth Animations**: Fade-in, slide-in, and bounce effects
- **Form Validation**: HTML5 validation with visual feedback
- **API Integration**: JavaScript fetch for seamless database interaction
- **Responsive Grid**: Auto-adjusting layout for all screen sizes
- **Interactive Elements**: Hover effects and transitions throughout

## Database Queries

### View all projects
```python
from app import db, Project
projects = Project.query.all()
for p in projects:
    print(f"{p.title}: {p.description}")
```

### View skills by category
```python
from app import Skill
frontend_skills = Skill.query.filter_by(category="Frontend").all()
```

### View contact messages
```python
from app import Contact
messages = Contact.query.order_by(Contact.created_at.desc()).all()
```

## Customization

### Change Database
To use PostgreSQL instead of SQLite, update `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/portfolio'
```

### Add New Fields
Add fields to a model and run:
```python
with app.app_context():
    db.create_all()
```

## Troubleshooting

### Database locked error
Delete `portfolio.db` and run `python init_db.py` again

### Import errors
Make sure all dependencies are installed: `pip install -r requirements.txt`

### Port already in use
Change the port in `app.py`: `app.run(debug=True, port=5001)`

## License

MIT License - Feel free to use this template for your own portfolio!

## Credits

Built with Flask, SQLAlchemy, and modern web technologies.
