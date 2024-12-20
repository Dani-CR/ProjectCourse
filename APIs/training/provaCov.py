import coverage

cov = coverage.Coverage(source=['openlibrary', 'infogami'])
cov.start()

print("Running test code...")
# Simulate code execution
def test_function():
    print("This is a test.")

test_function()

cov.stop()
cov.save()

print("Coverage should now be saved.")

