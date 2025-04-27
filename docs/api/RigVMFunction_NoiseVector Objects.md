## RigVMFunction_NoiseVector Objects

```python
class RigVMFunction_NoiseVector(RigVMFunction_MathBase)
```

Generates a vector through a noise fluctuation process between a min and a max through speed

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Noise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency`` (Vector):  [Read-Write]
- ``maximum`` (float):  [Read-Write]
- ``minimum`` (float):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``speed`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector.__init__"></a>

#### __init__

```python
def __init__(position: Vector = [0.000000, 0.000000, 0.000000],
             speed: Vector = [0.000000, 0.000000, 0.000000],
             frequency: Vector = [0.000000, 0.000000, 0.000000],
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_NoiseVector.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.RigVMFunction_NoiseVector.speed"></a>

#### speed

```python
@property
def speed() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector.speed"></a>

#### speed

```python
@speed.setter
def speed(value: Vector) -> None
```

<a id="unreal.RigVMFunction_NoiseVector.frequency"></a>

#### frequency

```python
@property
def frequency() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: Vector) -> None
```

<a id="unreal.RigVMFunction_NoiseVector.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseVector.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_NoiseVector"></a>