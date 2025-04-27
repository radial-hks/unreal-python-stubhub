## IKRig_FBIKEffector Objects

```python
class IKRig_FBIKEffector(Object)
```

IKRig FBIKEffector

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_FBIKSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Only] The bone that this effector will pull on.
- ``chain_depth`` (int32):  [Read-Write] Range 0-inf (default is 0). Explicitly set the number of bones up the hierarchy to consider part of this effector's 'chain'.
  The "chain" of bones is used to apply Preferred Angles, Pull Chain Alpha and Chain "Sub Solves".
  If left at 0, the solver will attempt to determine the root of the chain by searching up the hierarchy until it finds a branch or another effector, whichever it finds first.
- ``goal_name`` (Name):  [Read-Only] The Goal that is driving this effector's transform.
- ``pin_rotation`` (float):  [Read-Write] Range 0-1 (default is 1.0).
  Blends the effector bone rotation between the rotation of the effector transform (1.0) and the rotation of the input bone (0.0).
- ``pull_chain_alpha`` (float):  [Read-Write] Range 0-1 (default is 1.0). When enabled (greater than 0.0), the solver internally partitions the skeleton into 'chains' which extend
  from the effector up the hierarchy by "Chain Depth". If Chain Depth is 0, the chain root is set to the nearest fork in the skeleton.
  These chains are pre-rotated and translated, as a whole, towards the effector targets.
  This can improve the results for sparse bone chains, and significantly improve convergence on dense bone chains.
  But it may cause undesirable results in highly constrained bone chains (like robot arms).
- ``strength_alpha`` (float):  [Read-Write] Range 0-1 (default is 1.0). The strength of the effector when pulling the bone towards it's target location.
  At 0.0, the effector does not pull at all, but the bones between the effector and the root will still slightly resist motion from other effectors.
  This can thus act as a "stabilizer" for parts of the body that you do not want to behave in a pure FK fashion.

<a id="unreal.IKRig_FBIKEffector.goal_name"></a>

#### goal_name

```python
@property
def goal_name() -> Name
```

(Name):  [Read-Only] The Goal that is driving this effector's transform.

<a id="unreal.IKRig_FBIKEffector.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only] The bone that this effector will pull on.

<a id="unreal.IKRig_FBIKEffector.chain_depth"></a>

#### chain_depth

```python
@property
def chain_depth() -> int
```

(int32):  [Read-Write] Range 0-inf (default is 0). Explicitly set the number of bones up the hierarchy to consider part of this effector's 'chain'.
The "chain" of bones is used to apply Preferred Angles, Pull Chain Alpha and Chain "Sub Solves".
If left at 0, the solver will attempt to determine the root of the chain by searching up the hierarchy until it finds a branch or another effector, whichever it finds first.

<a id="unreal.IKRig_FBIKEffector.chain_depth"></a>

#### chain_depth

```python
@chain_depth.setter
def chain_depth(value: int) -> None
```

<a id="unreal.IKRig_FBIKEffector.strength_alpha"></a>

#### strength_alpha

```python
@property
def strength_alpha() -> float
```

(float):  [Read-Write] Range 0-1 (default is 1.0). The strength of the effector when pulling the bone towards it's target location.
At 0.0, the effector does not pull at all, but the bones between the effector and the root will still slightly resist motion from other effectors.
This can thus act as a "stabilizer" for parts of the body that you do not want to behave in a pure FK fashion.

<a id="unreal.IKRig_FBIKEffector.strength_alpha"></a>

#### strength_alpha

```python
@strength_alpha.setter
def strength_alpha(value: float) -> None
```

<a id="unreal.IKRig_FBIKEffector.pull_chain_alpha"></a>

#### pull_chain_alpha

```python
@property
def pull_chain_alpha() -> float
```

(float):  [Read-Write] Range 0-1 (default is 1.0). When enabled (greater than 0.0), the solver internally partitions the skeleton into 'chains' which extend
from the effector up the hierarchy by "Chain Depth". If Chain Depth is 0, the chain root is set to the nearest fork in the skeleton.
These chains are pre-rotated and translated, as a whole, towards the effector targets.
This can improve the results for sparse bone chains, and significantly improve convergence on dense bone chains.
But it may cause undesirable results in highly constrained bone chains (like robot arms).

<a id="unreal.IKRig_FBIKEffector.pull_chain_alpha"></a>

#### pull_chain_alpha

```python
@pull_chain_alpha.setter
def pull_chain_alpha(value: float) -> None
```

<a id="unreal.IKRig_FBIKEffector.pin_rotation"></a>

#### pin_rotation

```python
@property
def pin_rotation() -> float
```

(float):  [Read-Write] Range 0-1 (default is 1.0).
Blends the effector bone rotation between the rotation of the effector transform (1.0) and the rotation of the input bone (0.0).

<a id="unreal.IKRig_FBIKEffector.pin_rotation"></a>

#### pin_rotation

```python
@pin_rotation.setter
def pin_rotation(value: float) -> None
```

<a id="unreal.IKRig_FBIKBoneSettings"></a>