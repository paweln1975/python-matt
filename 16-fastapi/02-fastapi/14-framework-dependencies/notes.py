#!/usr/bin/env python3

# Reference:
# https://python3.info/fastapi/fastapi/framework-dependencies.html

#%% FastAPI Dependencies
# CDI - Content Dependency Injection
# Used when you have functions which takes the same thing (for example parameters)
# If one of your dependencies is declared multiple times for the same path operation, for example, multiple dependencies have a common sub-dependency, FastAPI will know to call that sub-dependency only once per request.
# And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific request, instead of calling the dependency multiple times for the same request.



#%% Function



#%% Class



#%% Shortcut
# FastAPI provides a shortcut injecting classes
# commons: CommonQueryParams = Depends()



#%% Dependencies in path operation decorators
# In some cases you don't really need the return value of a dependency inside your path operation function.
# Or the dependency doesn't return a value.
# But you still need it to be executed/solved.
# For those cases, instead of declaring a path operation function parameter with Depends, you can add a list of dependencies to the path operation decorator.



#%% Global Dependencies
# For some types of applications you might want to add dependencies to the whole application.



#%% Router Based Dependencies



#%% Dependencies with yield
# FastAPI supports dependencies that do some extra steps after finishing.*
# To do this, use yield instead of return, and write the extra steps after.
# It might be tempting to raise an HTTPException or similar in the exit code, after the yield. But it won't work.
# The exit code in dependencies with yield is executed after the response is sent
# Only one response will be sent to the client.
# After one of those responses is sent, no other response can be sent.