## PBIKEffector Objects

```python
class PBIKEffector(StructBase)
```

PBIKEffector

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: PBIK
- **File**: RigUnit_PBIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The bone that this effector will pull on.
- ``chain_depth`` (int32):  [Read-Write] Range 0-inf (default is 0). Explicitly set the number of bones up the hierarchy to consider part of this effector's 'chain'.
  The "chain" of bones is used to apply Preferred Angles, Pull Chain Alpha and "Sub Solve" iterations.
  If left at 0, the solver will attempt to determine the root of the chain by searching up the hierarchy until it finds a branch or another effector, whichever it finds first.
- ``pin_rotation`` (float):  [Read-Write] Range 0-1 (default is 1.0).
  Blends the effector bone rotation between the rotation of the effector transform (1.0) and the rotation of the input bone (0.0).
- ``position_alpha`` (float):  [Read-Write] Range 0-1, default is 1. Blend between the input bone position (0.0) and the current effector position (1.0).
- ``pull_chain_alpha`` (float):  [Read-Write] Range 0-1 (default is 1.0). When enabled (greater than 0.0), the solver internally partitions the skeleton into 'chains' which extend from the effector to the nearest fork in the skeleton.
  These chains are pre-rotated and translated, as a whole, towards the effector targets.
  This can improve the results for sparse bone chains, and significantly improve convergence on dense bone chains.
  But it may cause undesirable results in highly constrained bone chains (like robot arms).
- ``rotation_alpha`` (float):  [Read-Write] Range 0-1, default is 1. Blend between the input bone rotation (0.0) and the current effector rotation (1.0).
- ``strength_alpha`` (float):  [Read-Write] Range 0-1 (default is 1.0). The strength of the effector when pulling the bone towards it's target location.
  At 0.0, the effector does not pull at all, but the bones between the effector and the root will still slightly resist motion from other effectors.
  This can thus act as a "stabilizer" of sorts for parts of the body that you do not want to behave in a pure FK fashion.
- ``transform`` (Transform):  [Read-Write] The target location and rotation for this effector. The solver will try to get the specified bone to reach this location.

<a id="unreal.PBIKEffector.__init__"></a>

#### __init__

```python
def __init__(chain_depth: int = 0) -> None
```

<a id="unreal.PBIKEffector.chain_depth"></a>

#### chain_depth

```python
@property
def chain_depth() -> int
```

(int32):  [Read-Write] Range 0-inf (default is 0). Explicitly set the number of bones up the hierarchy to consider part of this effector's 'chain'.
The "chain" of bones is used to apply Preferred Angles, Pull Chain Alpha and "Sub Solve" iterations.
If left at 0, the solver will attempt to determine the root of the chain by searching up the hierarchy until it finds a branch or another effector, whichever it finds first.

<a id="unreal.PBIKEffector.chain_depth"></a>

#### chain_depth

```python
@chain_depth.setter
def chain_depth(value: int) -> None
```

<a id="unreal.RigUnit_PBIK"></a>