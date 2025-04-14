

def pytest_configure(config):
    config.addinivalue_line("markers", "asyncio: mark test as using asyncio")


pytest_plugins = ["pytest_asyncio"]

# Let pytest-asyncio handle the event loop configuration
