## MetasoundFrontendClassName Objects

```python
class MetasoundFrontendClassName(StructBase)
```

Name of a Metasound class

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] Name of class.
- ``namespace`` (Name):  [Read-Write] Namespace of class.
- ``variant`` (Name):  [Read-Write] Variant of class. The Variant is used to describe an equivalent class which performs the same operation but on differing types.

<a id="unreal.MetasoundFrontendClassName.__init__"></a>

#### __init__

```python
def __init__(namespace: Name = "None",
             name: Name = "None",
             variant: Name = "None") -> None
```

<a id="unreal.MetasoundFrontendClassName.namespace"></a>

#### namespace

```python
@property
def namespace() -> Name
```

(Name):  [Read-Write] Namespace of class.

<a id="unreal.MetasoundFrontendClassName.namespace"></a>

#### namespace

```python
@namespace.setter
def namespace(value: Name) -> None
```

<a id="unreal.MetasoundFrontendClassName.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Name of class.

<a id="unreal.MetasoundFrontendClassName.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.MetasoundFrontendClassName.variant"></a>

#### variant

```python
@property
def variant() -> Name
```

(Name):  [Read-Write] Variant of class. The Variant is used to describe an equivalent class which performs the same operation but on differing types.

<a id="unreal.MetasoundFrontendClassName.variant"></a>

#### variant

```python
@variant.setter
def variant(value: Name) -> None
```

<a id="unreal.MetaSoundOutput"></a>