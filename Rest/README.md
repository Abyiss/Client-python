# Get Started

For a basic product overview, check out our [setup and use documentation](https://github.com/Abyiss/Client-python/blob/production/README.md) or go to our website [Abyiss.com](https://abyiss.com/documentation)

# Simple REST API Demo

```python
import requests

s = requests.Session()

print(s.get('http://169.63.179.247/v1/exchanges').json())
```

# Notes

Make sure to have python installed and initialized to run the code above
