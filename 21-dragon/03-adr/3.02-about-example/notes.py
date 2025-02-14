#!/usr/bin/env python3
# https://python3.info/dragon/adr/about-example.html


# %% ADR Example
# - Decision: Python backend web framework
# - Status: accepted
# - Decision Date: 2000-01-02
# - Release Date: 2000-01-05
# - Deciders: Mark Watney, Melissa Lewis, Rick Martinez
# %%



# %% Problem
# - Python backend web framework is needed
# %%



# %% Motivation
# - Codebase become unmaintainable
# - Current documentation in old
# - Need API documentation auto-generation
# - Need REST/JSON API
# - Need authorization and authentication
# - Need auto-generated admin panel
# - Need tests
# - Need ORM
# - Need auto-generated database migrations
# - Need async code
# - Need more time-effective way for on-boarding of new employees
# - Onboarding takes too much time
# - ORM makes refactoring easier
# - ORM standardizes data model
# %%



# %% Considerations
# - FastAPI
# - Flask
# - Django + Ninja
# %%



# %% Option 1 - FastAPI
# - Good: Easy
# - Good: Fast onboarding
# - Good: Async
# - Good: API documentation auto-generation
# - Good: Worldwide adoption (on hype)
# - Bad: New project
# - Bad: No ORM
# - Bad: No DB schema migration
# - Bad: No admin
# - Bad: Single-person driven project (single point of failure)
# - Bad: No steering committee
# - Bad: Slowed down recently
# - Decision: rejected, no ORM
# %%



# %% Option 2 - Flask
# - Good: Easy
# - Good: Fast onboarding
# - Good: ORM (as separate package)
# - Good: Mature project
# - Good: Async since 2.0
# - Bad: FastAPI took his hype
# - Bad: No DB schema migration
# - Bad: No admin
# - Bad: No API documentation auto-generation
# - Decision: rejected, obsolete?
# %%



# %% Option 3 - Django + Ninja
# - Good: Async
# - Good: ORM
# - Good: DB schema migration
# - Good: Admin
# - Good: API documentation auto-generation (Ninja)
# - Good: FastAPI style REST/JSON views (Ninja)
# - Good: Steering committee (no single point of failure)
# - Bad: Intermediate
# - Bad: More complex than FastAPI and Flask
# - Decision: candidate
# %%



# %% Decision
# - Django + Ninja
# %%



