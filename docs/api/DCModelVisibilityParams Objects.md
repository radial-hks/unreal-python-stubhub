## DCModelVisibilityParams Objects

```python
class DCModelVisibilityParams(EidParams)
```

DCModel Visibility Params

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPModelAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``is_visible`` (bool):  [Read-Write]

<a id="unreal.DCModelVisibilityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(is_visible: bool = False) -> None
```

<a id="unreal.DCModelVisibilityParams.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCModelVisibilityParams.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.DCPModelActiveParams"></a>