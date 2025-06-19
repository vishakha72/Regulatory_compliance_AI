import os

class Config:
    LLM_MODEL = "gpt-4"
    MAX_CONCURRENT_TASKS = 5
    COMPLIANCE_DB_URI = os.getenv("COMPLIANCE_DB")
    NOTIFICATION_WEBHOOK = os.getenv("SLACK_WEBHOOK")
