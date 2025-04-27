## ToolShutdownType Objects

```python
class ToolShutdownType(EnumBase)
```

Passed to UInteractiveTool::Shutdown to indicate how Tool should shut itself down

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InteractiveTool.h

<a id="unreal.ToolShutdownType.COMPLETED"></a>

#### COMPLETED

0: Tool cleans up and exits. Pass this to tools that do not have Accept/Cancel options.

<a id="unreal.ToolShutdownType.ACCEPT"></a>

#### ACCEPT

1: Tool commits current preview to scene

<a id="unreal.ToolShutdownType.CANCEL"></a>

#### CANCEL

2: Tool discards current preview without modifying scene

<a id="unreal.XRDeviceConnectionResult"></a>