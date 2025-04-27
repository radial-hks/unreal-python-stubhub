## AnimNode_MakeDynamicAdditive Objects

```python
class AnimNode_MakeDynamicAdditive(AnimNode_Base)
```

Anim Node Make Dynamic Additive

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_MakeDynamicAdditive.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive`` (PoseLink):  [Read-Write] Pose to make additive
- ``base`` (PoseLink):  [Read-Write] Reference pose for additive delta calculation
- ``mesh_space_additive`` (bool):  [Read-Write] Do additive delta calculation in mesh space

<a id="unreal.AnimNode_MakeDynamicAdditive.__init__"></a>

#### __init__

```python
def __init__(base: PoseLink = [],
             additive: PoseLink = [],
             mesh_space_additive: bool = False) -> None
```

<a id="unreal.AnimNode_MakeDynamicAdditive.base"></a>

#### base

```python
@property
def base() -> PoseLink
```

(PoseLink):  [Read-Write] Reference pose for additive delta calculation

<a id="unreal.AnimNode_MakeDynamicAdditive.base"></a>

#### base

```python
@base.setter
def base(value: PoseLink) -> None
```

<a id="unreal.AnimNode_MakeDynamicAdditive.additive"></a>

#### additive

```python
@property
def additive() -> PoseLink
```

(PoseLink):  [Read-Write] Pose to make additive

<a id="unreal.AnimNode_MakeDynamicAdditive.additive"></a>

#### additive

```python
@additive.setter
def additive(value: PoseLink) -> None
```

<a id="unreal.AnimNode_MakeDynamicAdditive.mesh_space_additive"></a>

#### mesh_space_additive

```python
@property
def mesh_space_additive() -> bool
```

(bool):  [Read-Write] Do additive delta calculation in mesh space

<a id="unreal.AnimNode_MakeDynamicAdditive.mesh_space_additive"></a>

#### mesh_space_additive

```python
@mesh_space_additive.setter
def mesh_space_additive(value: bool) -> None
```

<a id="unreal.AnimNode_MirrorBase"></a>