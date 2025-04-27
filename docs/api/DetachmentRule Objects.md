## DetachmentRule Objects

```python
class DetachmentRule(EnumBase)
```

Rules for detaching components - needs to be kept synced to EAttachmentRule

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.DetachmentRule.KEEP_RELATIVE"></a>

#### KEEP_RELATIVE

0: Keeps current relative transform.

<a id="unreal.DetachmentRule.KEEP_WORLD"></a>

#### KEEP_WORLD

1: Automatically calculates the relative transform such that the detached component maintains the same world transform.

<a id="unreal.AttachmentRule"></a>