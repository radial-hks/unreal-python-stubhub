## RemoveEntityByTypesParams Objects

```python
class RemoveEntityByTypesParams(ParamsBase)
```

Remove Entity by Types Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``types`` (Array[str]):  [Read-Write]

<a id="unreal.RemoveEntityByTypesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(types: Array[str] = []) -> None
```

<a id="unreal.RemoveEntityByTypesParams.types"></a>

#### types

```python
@property
def types() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RemoveEntityByTypesParams.types"></a>

#### types

```python
@types.setter
def types(value: Array[str]) -> None
```

<a id="unreal.EntityUpdatedEventArgs"></a>