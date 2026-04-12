## OnWdpMaterialHitEventArgs Objects

```python
class OnWdpMaterialHitEventArgs(EventArgsBase)
```

On Wdp Material Hit Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (int64):  [Read-Write]
- ``material_index`` (int32):  [Read-Write]
- ``mesh_name`` (Name):  [Read-Write]

<a id="unreal.OnWdpMaterialHitEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: int = 0,
             mesh_name: Name = "None",
             material_index: int = 0) -> None
```

<a id="unreal.OnWdpMaterialHitEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.OnWdpMaterialHitEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: int) -> None
```

<a id="unreal.OnWdpMaterialHitEventArgs.mesh_name"></a>

#### mesh\_name

```python
@property
def mesh_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.OnWdpMaterialHitEventArgs.mesh_name"></a>

#### mesh\_name

```python
@mesh_name.setter
def mesh_name(value: Name) -> None
```

<a id="unreal.OnWdpMaterialHitEventArgs.material_index"></a>

#### material\_index

```python
@property
def material_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.OnWdpMaterialHitEventArgs.material_index"></a>

#### material\_index

```python
@material_index.setter
def material_index(value: int) -> None
```

<a id="unreal.EntitySlotParams"></a>