from crewai import Agent

agentic_api_drift_detector = Agent(
    role="Agentic Api Drift Detector",
    goal="Deliver high-precision autonomous Agentic Api Drift Detector operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
