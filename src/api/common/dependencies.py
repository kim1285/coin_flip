from contextlib import asynccontextmanager


def get_lifecycle():
    @asynccontextmanager
    async def lifecycle():
        # connect to db, start db session pool
        yield
        # clean up db session pool and any connections
        raise NotImplementedError
    return lifecycle
