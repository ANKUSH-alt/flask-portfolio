from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    technologies = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'technologies': self.technologies,
            'link': self.link,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.Integer, default=75)  # 0-100

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'proficiency': self.proficiency
        }


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


# Routes
@app.route('/')
def index():
    return render_template('portfolio.html')


@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        data = request.get_json()
        project = Project(
            title=data.get('title'),
            description=data.get('description'),
            technologies=data.get('technologies'),
            link=data.get('link')
        )
        db.session.add(project)
        db.session.commit()
        return jsonify(project.to_dict()), 201

    projects_list = Project.query.all()
    return jsonify([p.to_dict() for p in projects_list])


@app.route('/api/projects/<int:project_id>', methods=['GET', 'PUT', 'DELETE'])
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)

    if request.method == 'GET':
        return jsonify(project.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        project.title = data.get('title', project.title)
        project.description = data.get('description', project.description)
        project.technologies = data.get('technologies', project.technologies)
        project.link = data.get('link', project.link)
        db.session.commit()
        return jsonify(project.to_dict())

    if request.method == 'DELETE':
        db.session.delete(project)
        db.session.commit()
        return '', 204


@app.route('/api/skills', methods=['GET', 'POST'])
def skills():
    if request.method == 'POST':
        data = request.get_json()
        skill = Skill(
            category=data.get('category'),
            name=data.get('name'),
            proficiency=data.get('proficiency', 75)
        )
        db.session.add(skill)
        db.session.commit()
        return jsonify(skill.to_dict()), 201

    skills_list = Skill.query.all()
    return jsonify([s.to_dict() for s in skills_list])


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    contact = Contact(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message')
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.to_dict()), 201


@app.route('/api/contact-messages', methods=['GET'])
def contact_messages():
    messages = Contact.query.order_by(Contact.created_at.desc()).all()
    return jsonify([m.to_dict() for m in messages])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
