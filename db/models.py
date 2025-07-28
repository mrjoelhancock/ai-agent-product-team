# db/models.py

from sqlalchemy import Column, String, Text, DateTime, Enum, ForeignKey, Table
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from datetime import datetime
from db.database import Base
from enum import Enum as PyEnum

class JobStatus(PyEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"
    BLOCKED = "blocked"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    
    project_id = Column(String, nullable=False, index=True)
    
    status = Column(Enum(JobStatus), nullable=False, default=JobStatus.PENDING)
    
    outcome = Column(Text, nullable=False)
    success_criteria = Column(Text)
    
    context = Column(JSONB)  # Arbitrary notes or inputs for the job
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    start_after = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    # List of job IDs that must be completed before this job can run
    requires_jobs = Column(ARRAY(String), default=[])

    def __repr__(self):
        return f"<Job(id='{self.id}', project='{self.project_id}', status='{self.status.value}')>"

class ProjectStatus(PyEnum):
    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    
    status = Column(Enum(ProjectStatus), default=ProjectStatus.ACTIVE, nullable=False)
    
    tech_stack = Column(JSONB, nullable=True)       # List or structured object
    documentation = Column(JSONB, nullable=True)    # Markdown or structured doc
    
    code_path = Column(String, nullable=True)
    tools = Column(JSONB, nullable=True)            # Adapters per tool

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Project(id='{self.id}', name='{self.name}', status='{self.status.value}')>"