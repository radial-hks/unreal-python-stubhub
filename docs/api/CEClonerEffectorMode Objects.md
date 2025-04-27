## CEClonerEffectorMode Objects

```python
class CEClonerEffectorMode(EnumBase)
```

Enumerates the effector mode available

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerEffectorShared.h

<a id="unreal.CEClonerEffectorMode.DEFAULT"></a>

#### DEFAULT

0: Control clones offset, rotation, scale manually

<a id="unreal.CEClonerEffectorMode.TARGET"></a>

#### TARGET

1: Rotates clones towards a target actor

<a id="unreal.CEClonerEffectorMode.NOISE_FIELD"></a>

#### NOISE_FIELD

2: Randomly applies noise across the field zone

<a id="unreal.CEClonerEffectorMode.PUSH"></a>

#### PUSH

3: Pushes clones apart based on a strength and direction

<a id="unreal.CEClonerEffectorMode.STEP"></a>

#### STEP

4: Accumulate transform on clones based on their index

<a id="unreal.AvaClonerEffectorMode"></a>