## SmartObjectUserCapsuleParams Objects

```python
class SmartObjectUserCapsuleParams(StructBase)
```

Struct defining Smart Object user capsule size.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``height`` (float):  [Read-Write] Full height of the capsule
- ``radius`` (float):  [Read-Write] Radius of the capsule
- ``step_height`` (float):  [Read-Write] Step up height. This space is ignored when testing collisions.

<a id="unreal.SmartObjectUserCapsuleParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(radius: float = 0.000000,
             height: float = 0.000000,
             step_height: float = 0.000000) -> None
```

<a id="unreal.SmartObjectUserCapsuleParams.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Radius of the capsule

<a id="unreal.SmartObjectUserCapsuleParams.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.SmartObjectUserCapsuleParams.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] Full height of the capsule

<a id="unreal.SmartObjectUserCapsuleParams.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.SmartObjectUserCapsuleParams.step_height"></a>

#### step\_height

```python
@property
def step_height() -> float
```

(float):  [Read-Write] Step up height. This space is ignored when testing collisions.

<a id="unreal.SmartObjectUserCapsuleParams.step_height"></a>

#### step\_height

```python
@step_height.setter
def step_height(value: float) -> None
```

<a id="unreal.SmartObjectSlotDefinition"></a>