



According to the given instructions, I have to base my work on the feedback I've made in the first part. The code I produced works with Python2.7 up to 3.7.3.

I was willing to imitate the structure of the current algolia-search API in Python.
I think I had an issue with my URL being modified [maybe by this code](https://github.com/algolia/algoliasearch-client-python/blob/master/algoliasearch/http/transporter.py#L67).
during my attemps to use `status.algolia.com` instead of the usual domains. 


Since I already took a lot of time on source analysis and the first part, I decided to move ahead and don't use the `Transporter` and `Requester` as seen in your code. 

This case looks way simpler since we don't have any "writes" to handle, only reads, so I'm not too upset about not using the whole HTTP layer that `algoliasearch.http` provides.



## How to use it

you can clone this repository, add `algolia_minimal` to your PYTHON_PATH, or _pip install it_.

```
git clone git@github.com:slashdevsda/minimal_client_api.git
cd minimal_client_api/ && pip install .
# you are good to go
```

### testing

from the root directory:

`python -m unittest tests.test_healthclient`


# About implementation:

I decided to use a variadic list of arguments to match the design of the underlying HTTP API - since the list of servers can be specified in a comma-separated list directly into the URL.


```python
from algolia_minimal.health import HealthClient


h = HealthClient.create('', '')
print(h.status())
print(h.status("c10-eu", "c4-eu"))
print(h.incidents())
print(h.incidents("c10-eu", "c4-eu"))
```

I did not implement asynchronous operations. If I had to, I'll choose aiohttp and overide 
my `HealthClient` class to redefine `try_http_query` with asynchronous features.

Also, I did not use any sort of HTTP session (`Request.Session`). Using persistent sessions and HTTP keepalive could eventually reduce latency if needed. 
