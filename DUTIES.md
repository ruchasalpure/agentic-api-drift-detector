# Duties and Responsibilities for Agentic API Drift Detector Agent

## Dual-Control Architecture
Maker:
payload-profiler

Checker:
breaking-change-checker

## Operational Workflow
1. The Maker (payload-profiler) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (breaking-change-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
