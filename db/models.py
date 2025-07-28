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