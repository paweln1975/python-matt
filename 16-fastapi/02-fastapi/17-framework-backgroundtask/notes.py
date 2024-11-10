#!/usr/bin/env python3

# Reference:
# https://python3.info/fastapi/fastapi/framework-backgroundtask.html

#%% FastAPI Background Tasks
# The class BackgroundTasks comes directly from starlette.background.
# It is imported/included directly into FastAPI so that you can import it from fastapi and avoid accidentally importing the alternative BackgroundTask (without the s at the end) from starlette.background.
# Background tasks are run after the response has been sent. So there's no way to raise an HTTPException because there's not even a way to change the response that is already sent.
# But if a background task creates a DB error, at least you can rollback or cleanly close the session in the dependency with yield, and maybe log the error or report it to a remote tracking system.
# Only one response will be sent to the client.
# After one of those responses is sent, no other response can be sent.