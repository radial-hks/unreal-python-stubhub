## GLTFExportMessages Objects

```python
class GLTFExportMessages(StructBase)
```

GLTFExport Messages

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFExporter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``errors`` (Array[str]):  [Read-Write]
- ``suggestions`` (Array[str]):  [Read-Write]
- ``warnings`` (Array[str]):  [Read-Write]

<a id="unreal.GLTFExportMessages.__init__"></a>

#### __init__

```python
def __init__(suggestions: Array[str] = [],
             warnings: Array[str] = [],
             errors: Array[str] = []) -> None
```

<a id="unreal.GLTFExportMessages.suggestions"></a>

#### suggestions

```python
@property
def suggestions() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.GLTFExportMessages.suggestions"></a>

#### suggestions

```python
@suggestions.setter
def suggestions(value: Array[str]) -> None
```

<a id="unreal.GLTFExportMessages.warnings"></a>

#### warnings

```python
@property
def warnings() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.GLTFExportMessages.warnings"></a>

#### warnings

```python
@warnings.setter
def warnings(value: Array[str]) -> None
```

<a id="unreal.GLTFExportMessages.errors"></a>

#### errors

```python
@property
def errors() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.GLTFExportMessages.errors"></a>

#### errors

```python
@errors.setter
def errors(value: Array[str]) -> None
```

<a id="unreal.GLTFMaterialBakeSize"></a>