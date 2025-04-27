## _Logger Objects

```python
class _Logger(_io.BufferedIOBase)
```

<a id="unreal._Logger.__init__"></a>

#### __init__

```python
def __init__(encoding, log_func, flush_func)
```

<a id="unreal._Logger.writable"></a>

#### writable

```python
def writable()
```

<a id="unreal._Logger.write"></a>

#### write

```python
def write(b)
```

<a id="unreal._Logger.flush"></a>

#### flush

```python
def flush()
```

<a id="unreal._Logger.detach"></a>

#### detach

```python
def detach()
```

<a id="unreal._Logger.close"></a>

#### close

```python
def close()
```

<a id="unreal._unbuffered_stdout"></a>

#### _unbuffered_stdout

<a id="unreal._redirect_warning"></a>

#### _redirect_warning

```python
def _redirect_warning(message,
                      category,
                      filename,
                      lineno,
                      file=None,
                      line=None)
```

<a id="unreal.uclass"></a>

#### uclass

```python
def uclass()
```

decorator used to define UClass types from Python

<a id="unreal.ustruct"></a>

#### ustruct

```python
def ustruct()
```

decorator used to define UStruct types from Python

<a id="unreal.uenum"></a>

#### uenum

```python
def uenum()
```

decorator used to define UEnum types from Python

<a id="unreal.uvalue"></a>

#### uvalue

```python
def uvalue(val, meta=None)
```

function used to define constant values from Python

<a id="unreal.uproperty"></a>

#### uproperty

```python
def uproperty(type, meta=None, getter=None, setter=None)
```

function used to define UProperty fields from Python

<a id="unreal.ufunction"></a>

#### ufunction

```python
def ufunction(meta=None,
              ret=None,
              params=None,
              override=None,
              static=None,
              pure=None,
              getter=None,
              setter=None)
```

decorator used to define UFunction fields from Python

<a id="unreal.AutomationScheduler"></a>