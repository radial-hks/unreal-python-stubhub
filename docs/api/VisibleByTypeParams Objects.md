## VisibleByTypeParams Objects

```python
class VisibleByTypeParams(ParamsBase)
```

Visible by Type Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``types`` (Array[str]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.VisibleByTypeParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(types: Array[str] = [], visible: bool = False) -> None
```

<a id="unreal.VisibleByTypeParams.types"></a>

#### types

```python
@property
def types() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.VisibleByTypeParams.types"></a>

#### types

```python
@types.setter
def types(value: Array[str]) -> None
```

<a id="unreal.VisibleByTypeParams.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.VisibleByTypeParams.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.WdpPreserveScaleRatioParams"></a>