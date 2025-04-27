## PyTestStructLibrary Objects

```python
class PyTestStructLibrary(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto the test struct in Python.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PyTest.h

<a id="unreal.PyTestStructLibrary.set_bool_mutable_via_ref"></a>

#### set_bool_mutable_via_ref

```python
@classmethod
def set_bool_mutable_via_ref(cls, struct: PyTestStruct) -> PyTestStruct
```

X.set_bool_mutable_via_ref(struct) -> PyTestStruct
Set Bool Mutable Via Ref

Args:
    struct (PyTestStruct): 

Returns:
    PyTestStruct: 

    struct (PyTestStruct):

<a id="unreal.PyTestStructLibrary.set_bool_mutable"></a>

#### set_bool_mutable

```python
@classmethod
def set_bool_mutable(cls, struct: PyTestStruct) -> None
```

X.set_bool_mutable(struct) -> None
Set Bool Mutable

Args:
    struct (PyTestStruct):

<a id="unreal.PyTestStructLibrary.legacy_is_bool_set"></a>

#### legacy_is_bool_set

```python
@classmethod
def legacy_is_bool_set(cls, struct: PyTestStruct) -> bool
```

X.legacy_is_bool_set(struct) -> bool
Legacy Is Bool Set
deprecated: LegacyIsBoolSet is deprecated. Please use IsBoolSet instead.

Args:
    struct (PyTestStruct): 

Returns:
    bool:

<a id="unreal.PyTestStructLibrary.is_bool_set"></a>

#### is_bool_set

```python
@classmethod
def is_bool_set(cls, struct: PyTestStruct) -> bool
```

X.is_bool_set(struct) -> bool
Is Bool Set

Args:
    struct (PyTestStruct): 

Returns:
    bool:

<a id="unreal.PyTestStructLibrary.clear_bool_mutable_via_ref"></a>

#### clear_bool_mutable_via_ref

```python
@classmethod
def clear_bool_mutable_via_ref(cls, struct: PyTestStruct) -> PyTestStruct
```

X.clear_bool_mutable_via_ref(struct) -> PyTestStruct
Clear Bool Mutable Via Ref

Args:
    struct (PyTestStruct): 

Returns:
    PyTestStruct: 

    struct (PyTestStruct):

<a id="unreal.PyTestStructLibrary.clear_bool_mutable"></a>

#### clear_bool_mutable

```python
@classmethod
def clear_bool_mutable(cls, struct: PyTestStruct) -> None
```

X.clear_bool_mutable(struct) -> None
Clear Bool Mutable

Args:
    struct (PyTestStruct):

<a id="unreal.PyTestStructLibrary.add_str"></a>

#### add_str

```python
@classmethod
def add_str(cls, struct: PyTestStruct, value: str) -> PyTestStruct
```

X.add_str(struct, value) -> PyTestStruct
Add Str

Args:
    struct (PyTestStruct): 
    value (str): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestStructLibrary.add_int"></a>

#### add_int

```python
@classmethod
def add_int(cls, struct: PyTestStruct, value: int) -> PyTestStruct
```

X.add_int(struct, value) -> PyTestStruct
Add Int

Args:
    struct (PyTestStruct): 
    value (int32): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestStructLibrary.add_float"></a>

#### add_float

```python
@classmethod
def add_float(cls, struct: PyTestStruct, value: float) -> PyTestStruct
```

X.add_float(struct, value) -> PyTestStruct
Add Float

Args:
    struct (PyTestStruct): 
    value (float): 

Returns:
    PyTestStruct:

<a id="unreal.PyTestObject"></a>