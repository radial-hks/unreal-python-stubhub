## DrawGeometryParams Objects

```python
class DrawGeometryParams(ParamsBase)
```

Draw Geometry Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: ApiParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_z`` (float):  [Read-Write]
- ``draw`` (bool):  [Read-Write]
- ``eids`` (Array[str]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.DrawGeometryParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(draw: bool = False,
             default_z: float = 0.000000,
             eids: Array[str] = []) -> None
```

<a id="unreal.DrawGeometryParams.draw"></a>

#### draw

```python
@property
def draw() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DrawGeometryParams.draw"></a>

#### draw

```python
@draw.setter
def draw(value: bool) -> None
```

<a id="unreal.DrawGeometryParams.default_z"></a>

#### default\_z

```python
@property
def default_z() -> float
```

(float):  [Read-Write]

<a id="unreal.DrawGeometryParams.default_z"></a>

#### default\_z

```python
@default_z.setter
def default_z(value: float) -> None
```

<a id="unreal.DrawGeometryParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.DrawGeometryParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.CreateGeometryEntitiesParams"></a>