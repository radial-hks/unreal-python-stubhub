# Unreal Python StubHub

This project aims to use the `pydoc-markdown` tool to convert Python code (primarily Unreal Engine Python API stubs) in the `UnrealPythonAPI` directory into Markdown format documentation.

## Project Goals

Provide type stubs for Unreal Engine's Python API and automatically generate clear, navigable Markdown documentation using `pydoc-markdown`. When using [**Context7**](https://context7.com/libraries) to parse the documentation, along with [**Context7 MCP Server**](https://context7.com/radial-hks/unreal-python-stubhub), users can quickly generate correct and reliable code.

**Usage Example**:

The following demonstrates how to use Context7 to quickly implement the functionality of retrieving the World Outliner directory tree:

```python
# Prompt
use unreal python to create a script that retrieves the world outliner directory tree information use context7

# Generated Path: Example/get_world_outliner_tree.py
# Execution Result (Basic.level):
- None
  - Floor
  - PlayerStart_0
- Lighting
  - DirectionalLight_0
  - SkyAtmosphere_0
  - SkyLight_0
  - ExponentialHeightFog_0
  - VolumetricCloud_0
  - StaticMeshActor_1
```

Through this approach, developers can quickly obtain code implementations that follow best practices, significantly improving Unreal Engine Python development efficiency.

## Project Rules

To ensure the project runs smoothly and generates high-quality documentation, please follow these rules:

### 1. Code Style

- **Consistency**: Maintain consistent code style. Although stub files may not fully follow PEP 8, new or modified code should strive to be concise and readable.
- **Stub Implementation**: Function and method bodies can use `pass` or `...` as placeholders.

### 2. Docstrings

- **Necessity**: All public modules, classes, functions, and methods must include docstrings.
- **Format**: Google-style docstrings are recommended for proper parsing by `pydoc-markdown`.
- **Content**: Docstrings should clearly describe the object's functionality, parameters, return values, and possible exceptions.

### 3. Directory Structure

- **Code Location**: All Unreal Engine Python API stub files must be placed in the `UnrealPythonAPI` directory.
- **Module Organization**: Maintain a module structure similar to the official Unreal Engine Python API (e.g., all content under the `unreal` module). **Note: When the Python plugin is enabled, an `unreal.py` file will be generated in the project cache directory.**
- **Documentation Output**: Generated Markdown documentation is located in the `docs/api/` directory.

### 4. Dependency Management

- **Core Dependency**: The project's core dependency is `pydoc-markdown`, defined in `pyproject.toml`.
- **Environment**: Using a virtual environment (like `.venv`) is recommended for managing project dependencies.
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Linux/macOS
  # or
  .venv\Scripts\activate  # Windows
  pip install -e .
  ```

### 5. Documentation Generation

- **Tools**: Use `pydoc-markdown` with the custom script `main.py` to generate Markdown documentation, then use `split_md.py` to split larger Markdown files by "Class" into smaller files for easier updating and management.
- **Execution (Recommended)**: Run the `main.py` script in the project root directory. This script automatically processes the `unreal` module in the `UnrealPythonAPI` directory and generates separate Markdown files for each top-level class and function in the `docs/api/` directory, while creating a `docs/api/index.md` file as an entry index.
  ```bash
  python main.py
  python split_md.py
  ```
  After execution, check the `docs/api/` directory for the generated documentation.

- **Alternative Execution Methods**: 
    - **Using `pydoc-markdown` CLI**: Directly call the command-line tool. This is useful for quickly generating documentation for a single module or testing specific configurations, but using `main.py` is recommended for the split documentation structure.
      ```bash
      # Example: Generate complete documentation for the unreal module (unsplit)
      pydoc-markdown -I UnrealPythonAPI -m unreal --render-toc > unreal_module_full.md
      ```
    - **Using `pydoc-markdown` API**: Call its API in other Python scripts. `main.py` is an example of using the API.

### 6. Contribution and Maintenance

- **Accuracy**: Ensure added or modified API stubs match the actual Unreal Engine Python API signatures.
- **Completeness**: Encourage supplementing missing API stubs and docstrings.
- **Updates**: Maintain and supplement API stubs as Unreal Engine versions update.