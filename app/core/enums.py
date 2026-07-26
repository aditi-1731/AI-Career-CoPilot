from enum import Enum

class UserRole(str, Enum):
    STUDENT = "STUDENT"
    FRESHER = "FRESHER"
    PROFESSIONAL = "PROFESSIONAL"


class ExperienceLevel(str, Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"


class WorkMode(str, Enum):
    REMOTE = "REMOTE"
    HYBRID = "HYBRID"
    ONSITE = "ONSITE"


class JobType(str, Enum):
    INTERNSHIP = "INTERNSHIP"
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"