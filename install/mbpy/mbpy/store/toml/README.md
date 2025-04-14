# Structure
[app]
    dependencies = ["A"]

[A]
    target_type         = "static library"
    dependencies        = ["B"]
    public_dependencies = ["C"]

[B]
    target_type                = "shared library"
    public_include_directories = ["src/B/include"]

[C]
    target_type                = "shared library"
    public_include_directories = ["src/C/include"]