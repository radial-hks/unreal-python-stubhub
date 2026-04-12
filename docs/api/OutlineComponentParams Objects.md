## OutlineComponentParams Objects

```python
class OutlineComponentParams(EidParams)
```

Outline Component Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpInstanceEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_names`` (Array[str]):  [Read-Write]
- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``outline`` (bool):  [Read-Write]

<a id="unreal.OutlineComponentParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(component_names: Array[str] = [], outline: bool = False) -> None
```

<a id="unreal.OutlineComponentParams.component_names"></a>

#### component\_names

```python
@property
def component_names() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.OutlineComponentParams.component_names"></a>

#### component\_names

```python
@component_names.setter
def component_names(value: Array[str]) -> None
```

<a id="unreal.OutlineComponentParams.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write]

<a id="unreal.OutlineComponentParams.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.ComponentNameParams"></a>