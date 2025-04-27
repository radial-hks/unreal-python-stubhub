## AnimLinkMethod Objects

```python
class AnimLinkMethod(EnumBase)
```

Supported types of time for a linked element

**C++ Source:**

- **Module**: Engine
- **File**: AnimLinkableElement.h

<a id="unreal.AnimLinkMethod.ABSOLUTE"></a>

#### ABSOLUTE

0: Element stays at a specific time without moving.

<a id="unreal.AnimLinkMethod.RELATIVE"></a>

#### RELATIVE

1: Element moves with its segment, but not when the segment changes size.

<a id="unreal.AnimLinkMethod.PROPORTIONAL"></a>

#### PROPORTIONAL

2: Element moves with its segment and will stay at a certain proportion through the segment.

<a id="unreal.MontageNotifyTickType"></a>