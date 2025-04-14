


def __invoke():
    async def foo():
                if 0:
                    yield
                return 12
            
    return locals()
            