## PCGPinStatus Objects

```python
class PCGPinStatus(EnumBase)
```

EPCGPin Status

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPin.h

<a id="unreal.PCGPinStatus.NORMAL"></a>

#### NORMAL

0: Normal usage pin.

<a id="unreal.PCGPinStatus.REQUIRED"></a>

#### REQUIRED

1: Only for input pins, mark this pin as required.If set on an output pin, behave as Normal.

<a id="unreal.PCGPinStatus.ADVANCED"></a>

#### ADVANCED

2: Advanced pin will be hidden by default in the UIand will be shown only if the user extends the node(in the UI) to see advanced pins.Pins can't be required and advanced at the same time.

<a id="unreal.ScriptCollisionShapeType"></a>