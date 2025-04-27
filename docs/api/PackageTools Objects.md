## PackageTools Objects

```python
class PackageTools(Object)
```

Package Tools

**C++ Source:**

- **Module**: UnrealEd
- **File**: PackageTools.h

<a id="unreal.PackageTools.sanitize_package_name"></a>

#### sanitize_package_name

```python
@classmethod
def sanitize_package_name(cls, package_name: str) -> str
```

X.sanitize_package_name(package_name) -> str
Replaces all invalid package name characters with _

Args:
    package_name (str): 

Returns:
    str:

<a id="unreal.PackageTools.package_name_to_filename"></a>

#### package_name_to_filename

```python
@classmethod
def package_name_to_filename(cls,
                             package_name: str,
                             extension: str = "") -> str
```

X.package_name_to_filename(package_name, extension="") -> str
Converts a long package name to a file name.
This can be called on package paths as well, provide no extension in that case.
Will return an empty string if it fails.

Args:
    package_name (str): Long Package Name
    extension (str): Package extension.

Returns:
    str: Package filename, or empty if it failed.

<a id="unreal.PackageTools.filename_to_package_name"></a>

#### filename_to_package_name

```python
@classmethod
def filename_to_package_name(cls, filename: str) -> str
```

X.filename_to_package_name(filename) -> str
Tries to convert a given relative or absolute filename to a long package name or path starting with a root like /Game
This works on both package names and directories, and it does not validate that it actually exists on disk.

Args:
    filename (str): Filename to convert.

Returns:
    str: Resulting long package name if the supplied filename properly maps to a long package root, empty string otherwise.

<a id="unreal.PackFactory"></a>