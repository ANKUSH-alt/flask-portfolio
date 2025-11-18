#!/usr/bin/env python3
"""
Database initialization script to populate sample data
"""

import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db, Project, Skill, Contact

def init_db():
    """Initialize the database with sample data"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database tables created")

        # Clear existing data
        db.session.query(Project).delete()
        db.session.query(Skill).delete()
        print("✓ Cleared existing data")

        # Add sample projects
        projects = [
            Project(
                title="E-Commerce Platform",
                description="A full-stack e-commerce solution with product catalog, shopping cart, and payment integration. Built with React and Flask.",
                technologies="React, Flask, SQLAlchemy, Stripe",
                link="https://github.com/example/ecommerce"
            ),
            Project(
                title="Task Management App",
                description="A collaborative task management tool with real-time updates and user authentication. Built with Vue.js and Node.js.",
                technologies="Vue.js, Node.js, MongoDB, Socket.io",
                link="https://github.com/example/taskmanager"
            ),
            Project(
                title="Weather Dashboard",
                description="A responsive weather application using OpenWeather API with 5-day forecast and geolocation features. Built with vanilla JavaScript.",
                technologies="JavaScript, OpenWeather API, HTML5 Geolocation",
                link="https://github.com/example/weather"
            ),
            Project(
                title="Portfolio Website",
                description="Modern portfolio website with animations, database integration, and contact form. Built with Flask and SQLAlchemy.",
                technologies="Flask, SQLAlchemy, HTML5, CSS3, JavaScript",
                link="https://github.com/example/portfolio"
            )
        ]

        for project in projects:
            db.session.add(project)
        db.session.commit()
        print(f"✓ Added {len(projects)} sample projects")

        # Add sample skills
        skills = [
            Skill(category="Frontend", name="HTML5", proficiency=95),
            Skill(category="Frontend", name="CSS3", proficiency=90),
            Skill(category="Frontend", name="JavaScript", proficiency=85),
            Skill(category="Frontend", name="React", proficiency=80),
            Skill(category="Frontend", name="Vue.js", proficiency=75),
            Skill(category="Backend", name="Python", proficiency=90),
            Skill(category="Backend", name="Flask", proficiency=85),
            Skill(category="Backend", name="Node.js", proficiency=80),
            Skill(category="Backend", name="REST APIs", proficiency=85),
            Skill(category="Database", name="SQLAlchemy", proficiency=85),
            Skill(category="Database", name="PostgreSQL", proficiency=80),
            Skill(category="Database", name="MongoDB", proficiency=75),
            Skill(category="Tools", name="Git", proficiency=90),
            Skill(category="Tools", name="Docker", proficiency=75),
            Skill(category="Tools", name="AWS", proficiency=70),
        ]

        for skill in skills:
            db.session.add(skill)
        db.session.commit()
        print(f"✓ Added {len(skills)} sample skills")

        print("\n✓ Database initialization complete!")
        print(f"  - Projects: {db.session.query(Project).count()}")
        print(f"  - Skills: {db.session.query(Skill).count()}")

if __name__ == '__main__':
    init_db()
