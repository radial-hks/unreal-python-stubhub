## ModelerFloorAtom Objects

```python
class ModelerFloorAtom(EntityAtomBase)
```

Modeler Floor Atom

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: WdpModelerEntity
- **File**: ModelerFloorAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``align_z`` (bool):  [Read-Only]
- ``corner_radius`` (float):  [Read-Only]
- ``corner_split_num`` (int32):  [Read-Only]
- ``inner_brightness`` (float):  [Read-Only]
- ``inner_height`` (float):  [Read-Only]
- ``inner_mat_name`` (AssetName):  [Read-Only] original attrs
- ``inner_normal`` (float):  [Read-Only]
- ``inner_roughness`` (float):  [Read-Only]
- ``inner_uv_transform`` (Transform):  [Read-Only]
- ``inverse_normal`` (bool):  [Read-Only]
- ``outer_brightness`` (float):  [Read-Only]
- ``outer_height`` (float):  [Read-Only]
- ``outer_mat_name`` (AssetName):  [Read-Only]
- ``outer_normal`` (float):  [Read-Only]
- ``outer_roughness`` (float):  [Read-Only]
- ``outer_uv_transform`` (Transform):  [Read-Only]
- ``outer_width`` (float):  [Read-Only]
- ``use_vertex_corner`` (bool):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inner_mat_name"></a>

#### inner\_mat\_name

```python
@property
def inner_mat_name() -> AssetName
```

(AssetName):  [Read-Only] original attrs

<a id="unreal.ModelerFloorAtom.outer_mat_name"></a>

#### outer\_mat\_name

```python
@property
def outer_mat_name() -> AssetName
```

(AssetName):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inner_height"></a>

#### inner\_height

```python
@property
def inner_height() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.outer_height"></a>

#### outer\_height

```python
@property
def outer_height() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.outer_width"></a>

#### outer\_width

```python
@property
def outer_width() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.corner_split_num"></a>

#### corner\_split\_num

```python
@property
def corner_split_num() -> int
```

(int32):  [Read-Only]

<a id="unreal.ModelerFloorAtom.outer_uv_transform"></a>

#### outer\_uv\_transform

```python
@property
def outer_uv_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inner_uv_transform"></a>

#### inner\_uv\_transform

```python
@property
def inner_uv_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.ModelerFloorAtom.use_vertex_corner"></a>

#### use\_vertex\_corner

```python
@property
def use_vertex_corner() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ModelerFloorAtom.align_z"></a>

#### align\_z

```python
@property
def align_z() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inverse_normal"></a>

#### inverse\_normal

```python
@property
def inverse_normal() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inner_roughness"></a>

#### inner\_roughness

```python
@property
def inner_roughness() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.outer_roughness"></a>

#### outer\_roughness

```python
@property
def outer_roughness() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inner_normal"></a>

#### inner\_normal

```python
@property
def inner_normal() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.outer_normal"></a>

#### outer\_normal

```python
@property
def outer_normal() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.inner_brightness"></a>

#### inner\_brightness

```python
@property
def inner_brightness() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorAtom.outer_brightness"></a>

#### outer\_brightness

```python
@property
def outer_brightness() -> float
```

(float):  [Read-Only]

<a id="unreal.ModelerFloorPolygonAtom"></a>