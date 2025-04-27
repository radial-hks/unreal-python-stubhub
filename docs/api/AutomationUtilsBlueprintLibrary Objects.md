## AutomationUtilsBlueprintLibrary Objects

```python
class AutomationUtilsBlueprintLibrary(BlueprintFunctionLibrary)
```

Automation Utils Blueprint Library

**C++ Source:**

- **Plugin**: AutomationUtils
- **Module**: AutomationUtils
- **File**: AutomationUtilsBlueprintLibrary.h

<a id="unreal.AutomationUtilsBlueprintLibrary.take_gameplay_automation_screenshot"></a>

#### take_gameplay_automation_screenshot

```python
@classmethod
def take_gameplay_automation_screenshot(cls,
                                        screenshot_name: str,
                                        max_global_error: float = 0.020000,
                                        max_local_error: float = 0.120000,
                                        map_name_override: str = "") -> None
```

X.take_gameplay_automation_screenshot(screenshot_name, max_global_error=0.020000, max_local_error=0.120000, map_name_override="") -> None
Take Gameplay Automation Screenshot

Args:
    screenshot_name (str): 
    max_global_error (float): 
    max_local_error (float): 
    map_name_override (str):

<a id="unreal.ChaosSolverFactory"></a>