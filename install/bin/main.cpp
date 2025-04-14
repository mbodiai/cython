#include <Python.h>  
#include <iostream>  
#include <filesystem>  
#include <string>

// Helper to check if a file exists
bool file_exists(const std::string& path) {
    std::filesystem::path p(path);
    return std::filesystem::exists(p);
}

int main(int argc, char *argv[]) {
    // Setup environment
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        std::cerr << "Fatal error: cannot decode program name" << std::endl;
        return 1;
    }
  
    // Create Python configuration with optimized settings
    PyConfig config;  
    PyConfig_InitPythonConfig(&config);  
    
    // Fast startup optimizations
    config.isolated = 1;                // Skip site.py for faster startup
    config.use_environment = 0;         // Ignore environment variables
    config.parse_argv = 0;              // Don't parse command line
    config.configure_c_stdio = 0;       // Don't configure C stdio
    config.install_signal_handlers = 0; // Skip signal handlers
    
    // Set Python home directory  
    std::string prefix = "/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12";  
    printf("Setting Python home to: %s\n", prefix.c_str());
    
    config.home = Py_DecodeLocale(prefix.c_str(), NULL);  
    if (config.home == NULL) {  
        std::cerr << "Fatal error: cannot decode Python home path" << std::endl;  
        return 1;  
    }  
    
    // Explicitly specify the Python program name
    config.program_name = program;
    
    // Initialize Python  
    PyStatus status = Py_InitializeFromConfig(&config);  
    if (PyStatus_Exception(status)) {  
        std::cerr << "Error initializing Python: " << status.err_msg << std::endl;  
        PyConfig_Clear(&config);  
        return 1;  
    }  
    
    // Add the installation directory to Python's sys.path  
    PyObject* sys_path = PySys_GetObject("path");  
    if (sys_path != NULL) {  
        // Debug: print the current sys.path
        std::cout << "Initial sys.path entries:" << std::endl;
        for (Py_ssize_t i = 0; i < PyList_Size(sys_path); i++) {
            PyObject* path = PyList_GetItem(sys_path, i);
            const char* path_str = PyUnicode_AsUTF8(path);
            std::cout << "  " << path_str << std::endl;
        }
    
        // Clear existing paths for faster imports (optional - only do this if we're sure we're adding all needed paths)
        // for (Py_ssize_t i = PyList_Size(sys_path) - 1; i >= 0; i--) {
        //     PyList_SetSlice(sys_path, i, i + 1, NULL);
        // }
        
        // Add the packages directory to the path first
        std::string packages_dir = "/Users/sebastianperalta/simply/corp/projects/cython/install/packages";
        std::cout << "Adding to sys.path: " << packages_dir << std::endl;
        PyObject* packages_path = PyUnicode_FromString(packages_dir.c_str());  
        PyList_Insert(sys_path, 0, packages_path);  
        Py_DECREF(packages_path);
        
        // Add the installation directory to the path  
        std::cout << "Adding to sys.path: " << "/Users/sebastianperalta/simply/corp/projects/cython/install" << std::endl;
        PyObject* install_path = PyUnicode_FromString("/Users/sebastianperalta/simply/corp/projects/cython/install");  
        PyList_Insert(sys_path, 0, install_path);  
        Py_DECREF(install_path);
        
        // Add standard library path if needed
        std::string stdlib_path = prefix + "/lib/python3.12";
        if (file_exists(stdlib_path)) {
            std::cout << "Adding stdlib to sys.path: " << stdlib_path << std::endl;
            PyObject* stdlib_path_obj = PyUnicode_FromString(stdlib_path.c_str());
            PyList_Append(sys_path, stdlib_path_obj);
            Py_DECREF(stdlib_path_obj);
        }
        
        // Debug: print the updated sys.path
        std::cout << "Updated sys.path entries:" << std::endl;
        for (Py_ssize_t i = 0; i < PyList_Size(sys_path); i++) {
            PyObject* path = PyList_GetItem(sys_path, i);
            const char* path_str = PyUnicode_AsUTF8(path);
            std::cout << "  " << path_str << std::endl;
        }
    }  
    
    // Import the module directly
    std::cout << "Importing module: mbcore.main" << std::endl;
    PyObject* module = PyImport_ImportModule("mbcore.main");  
    if (module == NULL) {  
        std::cerr << "Failed to import module 'mbcore.main'" << std::endl;  
        if (PyErr_Occurred()) {  
            PyErr_Print();  
        }  
        PyConfig_Clear(&config);  
        Py_Finalize();  
        return 1;  
    }  
    
    std::cout << "Successfully imported module 'mbcore.main'" << std::endl;
    
    // Clean up  
    Py_DECREF(module);  
    PyConfig_Clear(&config);  
    Py_Finalize();  
    return 0;  
}  
