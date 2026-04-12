## DCPSectionTransformParams Objects

```python
class DCPSectionTransformParams(StructBase)
```

DCPSection Transform Params

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPSectionAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``size`` (Vector):  [Read-Write]

<a id="unreal.DCPSectionTransformParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Rotator = [0.000000, 0.000000, 0.000000],
             size: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPSectionTransformParams.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.DCPSectionTransformParams.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.DCPSectionTransformParams.size"></a>

#### size

```python
@property
def size() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.DCPSectionParam"></a>