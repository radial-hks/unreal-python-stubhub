## RuntimeOptionsBase Objects

```python
class RuntimeOptionsBase(Object)
```

URuntimeOptionsBase: Base class designed to be subclassed in your game.

Supports checking at runtime whether features are enabled/disabled, and changing
configuration parameters via console cheats or startup commands.

Add new config properties to your subclasses which default to the desired normal state
This can be adjusted via the development-only tools (command line or cvar) or via an
override in the config hierarchy to adjust it as needed (e.g., via a hotfix).

In non-Shipping builds, each property will be exposed both as a console variable and as a
command-line argument for easy testing during development.

Debug console syntax (disabled in Shipping configurations):
  prefix.PropertyName Value
Command line syntax (disabled in Shipping configurations):
  -prefix.PropertyName=Value
DefaultRuntimeOptions.ini syntax (note that there is no prefix for these):
  [/Script/YourModule.YourRuntimeOptionsSubclass]
  PropertyName=Value

Where the prefix is set by the value of OptionCommandPrefix (defaults to "ro" but can be overridden)

You can also change the name of the ini file that settings are gathered from in your derived
UCLASS() declaration

**C++ Source:**

- **Module**: Engine
- **File**: RuntimeOptionsBase.h

<a id="unreal.SkinnedAsset"></a>