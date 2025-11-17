


def __invoke():
    async def foo():
                yield
                return 123
            
    return locals()
            